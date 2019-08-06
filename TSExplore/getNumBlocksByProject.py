import json
import csv

#Fails to deal with edge case where "(" ")" within string tokens
#Ignores conditional blocks entirely due to conditional statements use <>
#brackets instead of () parenthesis
def getBlockCountV1(inFile,outFile):
    formatted_data = {}
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        for line in f:
            try:

                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            bracketStack = 0
            calls = 0
            #quote   = True
            for word in data['stack_squeak'].strip("\"").split():
                for char in word:
                    if char in "(":
                        bracketStack += 1
                        if len(word) == 1 or word[-1] in ")":
                            calls -= 1
                    if char in ")" and bracketStack > 0:
                        bracketStack -= 1
                        calls += 1
            try:
                formatted_data[str(data['project_id'])] += calls
            except:
                formatted_data.update({str(data['project_id']):calls})

        #for key in formatted_data.keys():
            #print(str(key) + ": " + str(formatted_data[key]))

    with open(outFile, 'w') as f :
        f.write("project_id,block_count\n")
        for key in formatted_data.keys():
            f.write(str(key) + "," + str(formatted_data[key])+"\n")


#Edge case seems to be that only the outer block of nested conditionals are
#counted
def getBlockCountV2(inFile,outFile):
    formatted_data = {}
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        for line in f:
            try:

                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            calls = 0
        #Every time there is a new line character there is a block
            for char in data['stack_squeak']:
                if char in "\n":
                    calls += 1
            try:
                formatted_data[str(data['project_id'])] += calls
            except:
                formatted_data.update({str(data['project_id']):calls})



def getBlockCountV3(inFile,outFile):
    formatted_data = {}
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:
            try:

                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            calls = 0
            edgeCase = 0
            previousChar = "_"
            isQuote = False
            #numQuote = 0
            stack = 0
            for char in data['stack_squeak']:
                if isQuote:
                    if char in "\"" and previousChar not in "\\":
                        isQuote = False
                        #numQuote += 1
                else:
                    if char in "(":
                        stack += 1
                    if char in ")":
                        stack -= 1
                    if char in "(" and char not in previousChar:
                        #print(previousChar + char)
                        calls += 1
                    elif char in "\"":
                        isQuote = True
                        #numQuote += 1
                if char not in " ":
                    previousChar = char
            if stack != 0:
                edgeCaseLines += 1
                edgeCase += 1
                #if numQuote % 2 != 1:
                #print (str(data['project_id']))# +":"+ str(numQuote))

            print(str(data['project_id'])+":"+str(calls))
            try:
                formatted_data[str(data['project_id'])] += edgeCase
            except:
                formatted_data.update({str(data['project_id']):edgeCase})

        print("Edge Case Sprites: " + str(edgeCaseLines))


    with open(outFile, 'w') as f :
        f.write("project_id,block_count\n")
        for key in formatted_data.keys():
            f.write(str(key) + "," + str(formatted_data[key])+"\n")

"""def getBlockCountFromString(sprite):
    lines = sprite.split("\n")
    blockCount = 0
    for line in range(len(lines)):
        blockCount = getBlockCountFromLine(lines[line].strip())

def getBlockCountFromLine(line):
    if len(line) < 1:#case empty line
        return 0
    elif "\"" not in line:
        return 1
    elif "when I receive \"" in line:
        return 1
    elif "broadcast \"" in line:
        return 1
    elif "switch to costume \"" in line:
        return 1
    elif "switch to background \"" in line:
        return 1
    elif "play sound \"" in line:
        return 1
    elif "point towards " in line:
        return 1
    elif "when \"" in line and "\" key pressed" in line:
        return 1
    elif "set \"" in line and ("\" to " in line or "\" effect to" in line):
        return 2
    elif "change \"" in line and ("\" by " in line or "\" effect" in line):
        return 2
    elif "wait \"" in line and "\" secs" in line:
        return 2
    elif "say \"" in line:
        if "\" for" in line:
            return 2
        else:
            return 1
    elif "think \"" in line:
        if "\" for" in line:
            return 2
        else:
            return 1
    print(line)

def getBlockCountV4(inFile,outFile):
    formatted_data = {}
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:
            try:
                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            readable= data["stack_human_readable"]
            blockCount = getBlockCountFromString(readable)
            try:
                formatted_data[str(data['project_id'])] += blockCount
            except:
                formatted_data.update({str(data['project_id']):blockCount})
"""



"""def getQuoteCounts(sprite):
    lines = sprite.split("\n")
    quoteCounts = []
    for line in lines:
        quoteCounts.append(len(line.split("\""))-1)
        if len(line) <= 1:#at the end of scripts there is always
            #a double \n resulting in an empty lines
            #this marks those as such to differentiate with
            #blocks that have no potential input values
            quoteCounts[len(quoteCounts)-1] -= 1
    return quoteCounts


def getLines(sprite, quoteCounts):
    lines = []#will hold the split lines
    startIndex = 0
    endIndex = 0
    currIndex = 0
    numQuotes = 0
    for quoteCount in quoteCounts:
        while (currIndex < len(sprite)):
            #endIndex += 1
            #currIndex += 1
            if numQuotes == quoteCount:
                while
            if sprite[currIndex] in "\"":
                numQuotes += 1




    return lines


def getBlockCountV5(inFile,outFile):
    formatted_data = {}
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:
            try:
                data = json.loads(line,strict=False)
            except:
                datastring = str(line)
                for i in range(len(datastring)):
                    if ord(datastring[i]) > 127:
                        datastring = datastring[0:i] + '_' + datastring[i+1:]
                data = json.loads(datastring,strict=False)
            readable = data["stack_human_readable"]
            getQuoteCounts(readable)
            getLines(data["stack_squeak"], quoteCounts)"""


def getBlockCountV6(inFile,outFile):
    formatted_data = {}
    blockList = ["(playSound:", "(doPlaySoundAndWait", "(stopAllSounds", "(drum:duration:elapsed:from:", "(playDrum", "(rest:elapsed:from:", "(noteOn:duration:elapsed:from:", "(midiInstrument:", "(instrument:", "(changeVolumeBy:", "(setVolumeTo:", "(volume", "(changeTempoBy:", "(setTempoTo:", "(tempo", "(touching:", "(touchingColor:", "(color:sees:", "(doAsk", "(answer", "(mousePressed", "(mouseX", "(mouseY", "(timer", "(timerReset", "(keyPressed:", "(distanceTo:", "(getAttribute:of:", "(soundLevel", "(isLoud", "(timestamp", "(timeAndDate", "(getUserName", "(sensor:", "(sensorPressed:", "(showVariable:", "(hideVariable:", "(showList:", "(hideList:", "(+", "(-", "(*", "(/", "(randomFrom:to:", "(<", "(=", "(>", "(&", "(|", "(not", "(abs", "(sqrt", "(concatenate:with:", "(letter:of:", "(stringLength:", "(%", "(rounded", "(computeFunction:of:", "(createCloneOf", "(deleteClone", "(whenCloned", "(lookLike:", "(nextCostume", "(costumeIndex", "(costumeName", "(showBackground:", "(nextBackground", "(backgroundIndex", "(sceneName", "(nextScene", "(startScene", "(startSceneAndWait", "(say:duration:elapsed:from:", "(say:", "(think:duration:elapsed:from:", "(think:", "(changeGraphicEffect:by:", "(setGraphicEffect:to:", "(filterReset", "(changeSizeBy:", "(setSizeTo:", "(scale", "(show", "(hide", "(hideAll", "(comeToFront", "(goBackByLayers:", "(setVideoState", "(setVideoTransparency", "(scrollAlign", "(scrollRight", "(scrollUp", "(xScroll", "(yScroll", "(setRotationStyle", "(forward:", "(turnRight:", "(turnLeft:", "(heading:", "(pointTowards:", "(gotoX:y:", "(gotoSpriteOrMouse:", "(glideSecs:toX:y:elapsed:from:", "(changeXposBy:", "(xpos:", "(changeYposBy:", "(ypos:", "(bounceOffEdge", "(xpos", "(ypos", "(heading", "(clearPenTrails", "(putPenDown", "(putPenUp", "(penColor:", "(setPenHueTo:", "(changePenHueBy:", "(setPenShadeTo:", "(changePenShadeBy:", "(penSize:", "(changePenSizeBy:", "(stampCostume", "(append:toList:", "(deleteLine:ofList:", "(insert:at:ofList:", "(setLine:ofList:to:", "(getLine:ofList:", "(lineCountOfList:", "(list:contains:", "(doForeverIf", "(doForLoop", "(doIf", "(doIfElse", "(doWaitUntil", "(doWhile", "(doUntil", "(doReturn", "(stopAll", "(stopScripts", "(warpSpeed", "(wait:elapsed:from:", "(doForever", "(doRepeat", "(broadcast:", "(doBroadcastAndWait",  "EventHatMorph", "HatBlockMorph"]
    #Initialize each line of json file into dictionary form
    with open(inFile, encoding = "ISO-8859-1") as f:
        #'RawData/project_block_stacks.json'
        #'project_block_stacks_mini.json'
        edgeCaseLines = 0
        for line in f:
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
            for word in lines.split():
                for block in blockList:
                    if block in word:
                        blockCount += 1
                        break
            try:
                formatted_data[str(data['project_id'])] += blockCount
            except:
                formatted_data.update({str(data['project_id']):blockCount})

    with open(outFile, "w") as f:
        print("Writing to file: " + str(outFile))
        f.write("project_id,block_count\n")
        for project in formatted_data.keys():
            f.write(str(project)+","+str(formatted_data(project))+"\n")




            """if "EventHatMorph" in word or "HatBlockMorph" in word:
                    blockCount += 1
                elif "(=" in word or "(&" in word:
                    blockCount += 1
                elif "(>" in word or "(<" in word:
                    blockCount += 1
                elif "(+" in word or "(-" in word:
                    blockCount += 1
                elif "(|" in word or "(*" in word:
                    blockCount += 1
                elif "(/" in word:
                    blockCount += 1
                elif "(show)" in word or "(hide)" in word:
                    blockCount += 1
                elif "(gotoX:y:" in word or "(glideSecs" in word:
                    blockCount += 1
                elif "(forward" in word or "(lookLike" in word:
                    blockCount += 1
                elif "(think:" in word or "(say:" in word:
                    blockCount += 1
                elif "(pointTowards" in word or "(touching" in word:
                    blockCount += 1
                elif "(nextBackground)" in word or "(showBackground" in word:
                    blockCount += 1
                elif "(stopAll" in word or "(wait" in word:
                    blockCount += 1
                elif "(broadcast:" in word or "(heading" in word:
                    blockCount += 1
                elif "(changeVariable" in word or "(readVariable" in word:
                    blockCount += 1
                elif "createClone" in word or "deleteClone" in word:
                    blockCount += 1
                elif "(doIf" in word or "(doForever" in word:
                    blockCount += 1
                elif "(doRepeat" in word or "doBroadcastAndWait" in word:
                    blockCount += 1
                elif "(randomFrom:to:" in word or "(turnRight:" in word:
                    blockCount += 1
                elif "(keyPressed" in word or "(bounceOffEdge" in word:
                    blockCount += 1
                elif "(playSound" in word or "(color:sees" in word:
                    blockCount += 1
                elif "(xpos" in word or "(ypos" in word:
                    blockCount += 1
                elif "(not" in word or "(\\" in word:
                    blockCount += 1
                elif "(changeCostumeIndexBy:" in word or "(doReturn" in word:
                    blockCount += 1
                elif "(timer)" in word or "(timerReset)" in word:
                    blockCount += 1
                elif "(filterReset)" in word or "(doWaitUntil" in word:
                    blockCount += 1
                elif "(changeGraphicEffect" in word or "(setSizeTo" in word:
                    blockCount += 1
                elif "(mouseX" in word or "(mouseY" in word:
                    blockCount += 1
                elif "(nextCostume" in word or "(distanceTo" in word:
                    blockCount += 1
                elif "(gotoSpriteOrMouse" in word or "(clearPenTrails" in word:
                    blockCount += 1
                elif "(penColor:" in word or "(putPen" in word:
                    blockCount += 1
                elif "(setPenHue" in word or "(midiInstrument" in word:
                    blockCount += 1
                elif "(turnLeft" in word or "(setGraphicEffect" in word:
                    blockCount += 1
                elif "(changeXpos" in word or "(changeYpos" in word:
                    blockCount += 1
                elif "(changeBackgroundIndex" in word or "(changeSizeBy" in word:
                    blockCount += 1
                elif "duration:elapsed:from" in word or "(mousePressed)" in word:
                    blockCount += 1
                elif "(penSize" in word or "(comeToFront)" in word:
                    blockCount += 1
                elif "(doPlaySoundAndWait" in word or "(goBackByLayers" in word:
                    blockCount += 1
                elif "(abs" in word or "(stampCostume)" in word:
                    blockCount += 1
                elif "(soundLevel)" in word or "(setPenShadeTo:" in word:
                    blockCount += 1
                elif "(changePenHueBy" in word:
                    blockCount += 1
                elif "(doUntil" in word or "(changePenShadeBy" in word:
                    blockCount += 1
                elif "(sensorPressed" in word or "(scale)" in word:
                    blockCount += 1
                elif "(changePenSizeBy" in word or "(costumeIndex)" in word:
                    blockCount += 1
                elif "(doAsk" in word or "(answer)" in word:
                    blockCount += 1
                elif "(setVolumeTo:" in word or "(getAttribute:of:" in word:
                    blockCount += 1
                elif "(concatenate:with" in word or "(append:toList" in word:
                    blockCount += 1
                elif "(getLine:ofList" in word or "(getAttribute:of" in word:
                    blockCount += 1
                elif "(computeFunction:of" in word or "(rounded" in word:
                    blockCount += 1
                elif "(sensor" in word or "(hideVariable" in word:
                    blockCount += 1
                elif "(showVariable" in word or "(setVolumeTo:" in word:
                    blockCount += 1
                elif "(scratchComment" in word or "(comment:" in word:
                    blockCount += 0
                elif "(list:contains" in word or "(deleteLine:ofList" in word:
                    blockCount += 1
                elif "(lineCountOfList" in word or "(contentsOfList:" in word:
                    blockCount += 1
                elif "(insert:at:ofList" in word or "(setTempoTo:" in word:
                    blockCount += 1
                elif "(rest:elapsed:from" in word or "(backgroundIndex)" in word:
                    blockCount += 1
                elif "(changeVolumeBy:" in word or "(changeTempoTo:" in word:
                    blockCount += 1
                elif "(letter:of:" in word or "(stringLength:" in word:
                    blockCount += 1
                elif "(setLine:ofList" in word or "(changeTempoBy:" in word:
                    blockCount += 1
                elif "(motorOnFor:elapsed" in word or "(setMotorDirection" in word:
                    blockCount += 1
                elif "(volume)" in word or "(startMotorPower:" in word:
                    blockCount += 1
                elif "(allMotorsOn)" in word or "(allMotorsOff)" in word:
                    blockCount += 1
                elif "(rewindSound:" in word or "(turnAwayFromEdge)" in word:
                    blockCount += 1
                elif "(changeStretchBy:" in word or "(sayNothing)" in word:
                    blockCount += 1
                elif "(changeVisibilityBy:" in word or "(setVisibilityTo:" in word:
                    blockCount += 1
                elif "(changeHueTo:" in word or "(setHueShiftTo:" in word:
                    blockCount += 1
                elif "(changeFisheyeBy:" in word or "(changeWhirlBy:" in word:
                    blockCount += 1
                elif "(setWhirlTo:" in word or "(changePixelateCountBy:" in word:
                    blockCount += 1
                elif "(setPixelateCountTo:" in word or "(changeMosaicCountBy:" in word:
                    blockCount += 1
                elif "(setMosaicCountTo:" in word or "(changeBrightnessShiftBy:" in word:
                    blockCount += 1
                elif "(setBrightnessShiftTo:" in word or "(changeSaturationShiftBy:" in word:
                    blockCount += 1
                elif "(setSaturationShiftTo:" in word or "(changePointillizeSizeBy:" in word:
                    blockCount += 1
                elif "(setPointillizeSizeTo:" in word or "(changeWaterRippleBy:" in word:
                    blockCount += 1
                elif "(changeBlurBy:" in word or "(setBlurTo:" in word:
                    blockCount += 1
                elif "(sqrt" in word or "(setStretchTo:" in word:
                    blockCount += 1
                elif "(isLoud)" in word or "(mousePressed:" in word:
                    blockCount += 1
                elif "(getTime:" in word or "(isHidden)" in word:
                    blockCount += 1
                elif "(penShade)" in word or "(penHue)" in word:
                    blockCount += 1
                elif "(pointToX:y" in word or "(tempo)" in word:
                    blockCount += 1
                elif "(setWaterRippleTo:" in word:
                    blockCount += 1
                elif "(duplicateNoAttach)" in word or "(undoableDeleteSprite)" in word:
                    blockCount += 1
                elif "(changeHueShiftBy:" in word or "(setFisheyeTo:" in word:
                    blockCount += 1
                elif "(yourself)" in word or "(graphicEffect" in word:
                    blockCount += 1
                elif "(jokeOfTheDay:" in word or "(info:fromZip:" in word:
                    blockCount += 0
                elif "(synonym:" in word or "(wordOfTheDay:" in word:
                    blockCount += 0
                elif "(scratchrInfo:forUser:" in word or "(NOTE:" in word:
                    blockCount += 0
                elif "(obsolete)" in word or "(stopSound:" in word:
                    blockCount += 1
                elif "(penDown)" in word or "(penUp)" in word:
                    blockCount += 1
                elif "(senseAbsoluteX)" in word or "(senseAbsoluteY)" in word:
                    blockCount += 1
                elif "(senseMotion)" in word or "(changeSecondsBy:" in word:
                    blockCount += 1
                elif "(setSecondsTo:" in word or "(changeZoomBy:" in word:
                    blockCount += 1
                elif "(setZoomTo:" in word or "(changeHPanBy:" in word:
                    blockCount += 1
                elif "(setHPanTo:" in word or "(changeVPanBy:" in word:
                    blockCount += 1
                elif "(setVPanTo:" in word or "(setFadeTo:" in word:
                    blockCount += 1
                elif "(setFadeColor:" in word or "(trackMotion)" in word:
                    blockCount += 1
                elif "(trackColor)" in word or "(autoCalibrateRed)" in word:
                    blockCount += 1
                elif "(deleteVariable:" in word or "(addVariable:" in word:
                    blockCount += 1
                elif "(move:forward:" in word or "(positionVar:atX:y:" in word:
                    blockCount += 1
                elif "(playFrom:to:ofSound:" in word or "(layer:" in word:
                    blockCount += 1
                elif "(doForwards)" in word or "(doThis:on:" in word:
                    blockCount += 1
                elif "(nextInstanceName" in word or "(random:or:" in word:
                    blockCount += 1
                elif "(if:then:else:" in word or "(if:contains:" in word:
                    blockCount += 1
                elif "(asciiLetter:" in word or "(ascicodeof:" in word:
                    blockCount += 0
                elif "(changeFadeBy:" in word or "(senseDirection)" in word:
                    blockCount += 1
                elif "(senseRelativeX)" in word or "(senseRelativeY)" in word:
                    blockCount += 1
                elif "(hideList:" in word or "(showList:" in word:
                    blockCount += 1
                elif "(stringif:then:else" in word or "(flip)" in word:
                    blockCount += 1
                elif "(pointatx:y:" in word or "(costumeName)" in word:
                    blockCount += 1
                elif "(costumeWidth" in word or "(costumeHeight)" in word:
                    blockCount += 1
                elif "(setRotationCenterToX:y:" in word or "(openWebBrowserOn:" in word:
                    blockCount += 1
                elif "(isloud)" in word or "(setListBlockColorSelf:" in word:
                    blockCount += 1
                elif "(createListNamed:" in word or "(booleanRandom:Or:" in word:
                    blockCount += 1
                elif "(reportFalse)" in word or "(reportTrue)" in word:
                    blockCount += 1
                elif "(bounceOffSprite:" in word or "(addGlobalVariable)" in word:
                    blockCount += 1
                elif "(seesBroadcast:" in word or "(setSpeed)" in word:
                    blockCount += 1
                elif "\"" not in word and word[0] in "(" and len(word) > 1:
                    print(word)"""
            #print(str(data["project_id"]) + ":" + str(blockCount))
getBlockCountV6("RawData/project_block_stacks.json","RawData/project_blocks/blockCounts2.csv")#'RawData/project_block_stacks.json')

#getBlockCountV6("project_block_stacks_mini.json","RawData/project_blocks/blockCounts_mini.csv")#'RawData/project_block_stacks.json')
