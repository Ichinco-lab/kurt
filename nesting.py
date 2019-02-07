import os
import csv
rootdir = '../../official-data'
global participant_id
global condition
global phase
global lines
global responses
global nesting_writer

def print_and_reset():
    global participant_id
    global condition
    global phase
    global responses
    global nesting_writer
    if phase == "BASELINE" or phase=="OPEN":

        #nesting_writer.writerow([participant_id+';'+condition])
        answer=""
        shouldPrint = False
        foundOuter = None
        for i in range(0,len(lines)):
            answer += lines[i].split(('['))[0]+'\n'
            if 'do together' in lines[i] and foundOuter == None:
                foundOuter = 'do together'
            if 'count' in lines[i] and foundOuter == None:
                foundOuter = 'count'
            if 'do together' in lines[i]and foundOuter != None and foundOuter!= 'do together':
                shouldPrint = True
            if 'count' in lines[i]and foundOuter != None and foundOuter!= 'count':
                shouldPrint = True
            if '}' in lines[i]:
                foundOuter = None
        if shouldPrint:
            print(participant_id, condition, phase)
            print(answer)
        #nesting_writer.writerow([answer])


def setup():
    global participant_id
    global condition
    global phase
    global lines
    global responses
    lines = []
    responses = []
    participant_id = ""
    condition = ""
    phase = ""


with open('csvs/nesting.csv', 'w') as nestingFile:
    global nesting_writer
    nesting_writer = csv.writer(nestingFile, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for subdir, dirs, files in os.walk(rootdir):
        setup()
        for file in files:
            if 'clean-studyall' in os.path.join(subdir, file):
                filename = os.path.join(subdir, file)
                file = open(filename, "r")
                shouldPrint=False
                for line in file.readlines():
                    if "participant id" in line:
                        participant_id = line.split("participant id: ")[1].strip()
                    elif "study condition:" in line:
                        condition = line.split("study condition: ")[1].strip()
                    elif "study phase" in line:
                        phase = line.split("study phase: ")[1].strip()
                    if phase=="BASELINE" or phase=="OPEN":
                        if line[0] == '2':
                            shouldPrint = False
                        if shouldPrint:
                            lines.append(line)
                        if " info; active user method: Scene::My Story" in line:
                            shouldPrint=True
                            lines = []
                        if 'timer stopped' in line.lower():
                            responses.append(lines)
                            print_and_reset()
