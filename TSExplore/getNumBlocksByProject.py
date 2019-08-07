import json
import csv

def getBlockCountByProject(inFile,outFile):
    formatted_data = {}
    blockList = ["(playSound:", "(doPlaySoundAndWait", "(stopAllSounds", "(drum:duration:elapsed:from:", "(playDrum", "(rest:elapsed:from:", "(noteOn:duration:elapsed:from:", "(midiInstrument:", "(instrument:", "(changeVolumeBy:", "(setVolumeTo:", "(volume", "(changeTempoBy:", "(setTempoTo:", "(tempo", "(touching:", "(touchingColor:", "(color:sees:", "(doAsk", "(answer", "(mousePressed", "(mouseX", "(mouseY", "(timer", "(timerReset", "(keyPressed:", "(distanceTo:", "(getAttribute:of:", "(soundLevel", "(isLoud", "(timestamp", "(timeAndDate", "(getUserName", "(sensor:", "(sensorPressed:", "(showVariable:", "(hideVariable:", "(showList:", "(hideList:", "(+", "(-", "(*", "(/", "(randomFrom:to:", "(<", "(=", "(>", "(&", "(|", "(not", "(abs", "(sqrt", "(concatenate:with:", "(letter:of:", "(stringLength:", "(%", "(rounded", "(computeFunction:of:", "(createCloneOf", "(deleteClone", "(whenCloned", "(lookLike:", "(nextCostume", "(costumeIndex", "(costumeName", "(showBackground:", "(nextBackground", "(backgroundIndex", "(sceneName", "(nextScene", "(startScene", "(startSceneAndWait", "(say:duration:elapsed:from:", "(say:", "(think:duration:elapsed:from:", "(think:", "(changeGraphicEffect:by:", "(setGraphicEffect:to:", "(filterReset", "(changeSizeBy:", "(setSizeTo:", "(scale", "(show", "(hide", "(hideAll", "(comeToFront", "(goBackByLayers:", "(setVideoState", "(setVideoTransparency", "(scrollAlign", "(scrollRight", "(scrollUp", "(xScroll", "(yScroll", "(setRotationStyle", "(forward:", "(turnRight:", "(turnLeft:", "(heading:", "(pointTowards:", "(gotoX:y:", "(gotoSpriteOrMouse:", "(glideSecs:toX:y:elapsed:from:", "(changeXposBy:", "(xpos:", "(changeYposBy:", "(ypos:", "(bounceOffEdge", "(xpos", "(ypos", "(heading", "(clearPenTrails", "(putPenDown", "(putPenUp", "(penColor:", "(setPenHueTo:", "(changePenHueBy:", "(setPenShadeTo:", "(changePenShadeBy:", "(penSize:", "(changePenSizeBy:", "(stampCostume", "(append:toList:", "(deleteLine:ofList:", "(insert:at:ofList:", "(setLine:ofList:to:", "(getLine:ofList:", "(lineCountOfList:", "(list:contains:", "(doForeverIf", "(doForLoop", "(doIf", "(doIfElse", "(doWaitUntil", "(doWhile", "(doUntil", "(doReturn", "(stopAll", "(stopScripts", "(warpSpeed", "(wait:elapsed:from:", "(doForever", "(doRepeat", "(broadcast:", "(doBroadcastAndWait",  "EventHatMorph", "HatBlockMorph"]
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:#load each line in f
            try:
                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            lines = data["stack_squeak"]
            blockCount = 0
            for word in lines.split():#if a block found within a word
                for block in blockList:#within the line, blockCount++
                    if block in word:
                        blockCount += 1
                        break
            try:#update blockCounts by project
                formatted_data[str(data['project_id'])] += blockCount
            except:
                formatted_data.update({str(data['project_id']):blockCount})

    #save to csv
    with open(outFile, "w") as f:
        print("Writing to file: " + str(outFile))
        f.write("project_id,block_count\n")
        for project in formatted_data.keys():
            f.write(str(project)+","+str(formatted_data[project])+"\n")

def getBlockCountBySprite(inFile,outFile):
    formatted_data = {}
    blockList = ["(playSound:", "(doPlaySoundAndWait", "(stopAllSounds", "(drum:duration:elapsed:from:", "(playDrum", "(rest:elapsed:from:", "(noteOn:duration:elapsed:from:", "(midiInstrument:", "(instrument:", "(changeVolumeBy:", "(setVolumeTo:", "(volume", "(changeTempoBy:", "(setTempoTo:", "(tempo", "(touching:", "(touchingColor:", "(color:sees:", "(doAsk", "(answer", "(mousePressed", "(mouseX", "(mouseY", "(timer", "(timerReset", "(keyPressed:", "(distanceTo:", "(getAttribute:of:", "(soundLevel", "(isLoud", "(timestamp", "(timeAndDate", "(getUserName", "(sensor:", "(sensorPressed:", "(showVariable:", "(hideVariable:", "(showList:", "(hideList:", "(+", "(-", "(*", "(/", "(randomFrom:to:", "(<", "(=", "(>", "(&", "(|", "(not", "(abs", "(sqrt", "(concatenate:with:", "(letter:of:", "(stringLength:", "(%", "(rounded", "(computeFunction:of:", "(createCloneOf", "(deleteClone", "(whenCloned", "(lookLike:", "(nextCostume", "(costumeIndex", "(costumeName", "(showBackground:", "(nextBackground", "(backgroundIndex", "(sceneName", "(nextScene", "(startScene", "(startSceneAndWait", "(say:duration:elapsed:from:", "(say:", "(think:duration:elapsed:from:", "(think:", "(changeGraphicEffect:by:", "(setGraphicEffect:to:", "(filterReset", "(changeSizeBy:", "(setSizeTo:", "(scale", "(show", "(hide", "(hideAll", "(comeToFront", "(goBackByLayers:", "(setVideoState", "(setVideoTransparency", "(scrollAlign", "(scrollRight", "(scrollUp", "(xScroll", "(yScroll", "(setRotationStyle", "(forward:", "(turnRight:", "(turnLeft:", "(heading:", "(pointTowards:", "(gotoX:y:", "(gotoSpriteOrMouse:", "(glideSecs:toX:y:elapsed:from:", "(changeXposBy:", "(xpos:", "(changeYposBy:", "(ypos:", "(bounceOffEdge", "(xpos", "(ypos", "(heading", "(clearPenTrails", "(putPenDown", "(putPenUp", "(penColor:", "(setPenHueTo:", "(changePenHueBy:", "(setPenShadeTo:", "(changePenShadeBy:", "(penSize:", "(changePenSizeBy:", "(stampCostume", "(append:toList:", "(deleteLine:ofList:", "(insert:at:ofList:", "(setLine:ofList:to:", "(getLine:ofList:", "(lineCountOfList:", "(list:contains:", "(doForeverIf", "(doForLoop", "(doIf", "(doIfElse", "(doWaitUntil", "(doWhile", "(doUntil", "(doReturn", "(stopAll", "(stopScripts", "(warpSpeed", "(wait:elapsed:from:", "(doForever", "(doRepeat", "(broadcast:", "(doBroadcastAndWait",  "EventHatMorph", "HatBlockMorph"]
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:#load each line in f
            try:
                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            lines = data["stack_squeak"]
            blockCount = 0
            for word in lines.split():#if a block found within a word
                for block in blockList:#within the line, blockCount++
                    if block in word:
                        blockCount += 1
                        break
            try:#update blockCounts by sprite
                formatted_data[str(data['project_id'])].update(
                    {
                        str(data['sprite_id']):blockCount
                    })
            except:
                formatted_data.update(
                    {
                        str(data['project_id']):{
                            str(data['sprite_id']):blockCount
                        }
                    })

    #save to csv
    with open(outFile, "w") as f:
        print("Writing to file: " + str(outFile))
        f.write("project_id,sprite_id,block_count\n")
        for project in formatted_data.keys():
            for sprite in formatted_data[project].keys():
                f.write(str(project) + "," + str(sprite) + "," + str(formatted_data[project][sprite]) + "\n")

#getBlockCountByProject("RawData/project_block_stacks.json","RawData/project_blocks/blockCountsByProjects.csv")#'RawData/project_block_stacks.json')
getBlockCountBySprite("RawData/project_block_stacks.json","RawData/project_blocks/blockCountsBySprites.csv")
#getBlockCountByProject("project_block_stacks_mini.json","RawData/project_blocks/blockCounts_mini.csv")#'RawData/project_block_stacks.json')
