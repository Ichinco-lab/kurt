import kurt
import os
import sys
import pdb
import csv
from plugins import HairballPlugin
from plugins import blocks
from hairball import Hairball

csvfile = open('data.csv', 'w')
writer = csv.writer(csvfile)
myList = ["Project_Name","Abstraction","Parallelization","Logic",
                "Synchronization","FlowControl","UserInteractivity",
                "DataRepresentation","Dead_Code_Instances","Deafult_Sprite_Names","Duplicate_Scripts","AttributeInitialization_State"]
writer.writerow(myList)
#To take in multiple files
files = ['../test/tmp.sb', '../test/testsj1.sb2', '../test/testsj2_empty_if.sb2']
#To iterate over all the files and analyze all the plugins on each one of them
for file in files:
    args = ['-p', 'masteryNEU.Mastery', '-p', 'blocks.DeadCode', '-p', 'convention.SpriteNaming','-p', 'duplicate.DuplicateScripts', '-p', 'initialization.AttributeInitialization', file]
    hairball1 = Hairball(args)
    hairball1.initialize_plugins()
    hairball1.process()
    # pdb.set_trace()
    myList2 = [file]
    for header in myList[1:8]:
        #Storing the whole dictionary
        # myList2.append(hairball1.plugins[0].concepts)
        #Stores individual value for each header value in myList2
        myList2.append(hairball1.plugins[0].concepts[header])
    #Stores the dead code instances from blocks.py
    for header in myList[8:9]:
        myList2.append(hairball1.plugins[1].dead_code_instances)
    #Stores the value for how often the default Sprite Names are Used from convention.py
    for header in myList[9:10]:
        myList2.append(hairball1.plugins[2].total_default)
    #To count the duplicate scripts in the project from duplicate.py
    for header in myList[10:11]:
        myList2.append(hairball1.plugins[3].total_duplicate)
    # Output whether or not each attribute was correctly initialized.
    # Attributes that were not modified at all are considered to be properly
    # initialized. IF not modified then the state_not_modified=0
    for header in myList[11:12]:
        myList2.append(hairball1.plugins[4].STATE_NOT_MODIFIED)
    # for header in myList[12:13]:
    #     myList2.append(hairball1.plugins[5].STATE_NOT_MODIFIED)
    writer.writerow(myList2)
    hairball1.finalize()
# writeFile.close()
