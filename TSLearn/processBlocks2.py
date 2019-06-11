def process(myDict):
    operators = 0
    i = 0
    if_else = 0
    logical_thinking = 0


    sequence_of_blocks = 0
    repeat_forever = 0
    repear_until = 0
    flow_control = 0


    greenflag = 0
    mouse_key_events = 0
    webcam_microphone = 0
    user_interactivity = 0


    wait = 0
    broadcast = 0
    wait_until_when = 0
    synchronization = 0

    predef_vars = 0
    variables = 0
    lists = 0
    data_representation = 0

#This is the logical Thinking : CT Concept
#Logical Thinking: Operators + if_else + if
    if int(myDict["islessthan"]) >= 1 or int(myDict["and_operator"]) >= 1 or int(myDict["isequalto"]) >= 1 or int(myDict["isgreaterthan"]) >= 1 or int(myDict["or_operator"]) >= 1 or int(myDict["not"]) >= 1:
        operators = 1
    if int(myDict["doif"]) >= 1:
        i = 1
    if int(myDict["doifelse"]) >= 1:
        if_else = 1
    logical_thinking = operators + i + if_else
    #print(logical_thinking)

#This is the Flow Control : CT Concept
# Flow control: doforever + doforeverif + doifelse + doif + dorepeat + doreturn + dountil + dowaituntil
    for key in myDict.keys():
        if "project_id" not in key and "scratchcomment" not in key and "askyahoo" not in key and "wordoftheday" not in key and "jokeoftheday" not in key and "synonym" not in key and "info_fromzip" not in key and "scratchinfo_foruser" not in key and "other" not in key and int(myDict[key]) >= 1:
            sequence_of_blocks = 1
            break
    if int(myDict["doforever"]) >= 1 or int(myDict["doforeverif"]) >= 1 or int(myDict["doifelse"]) >= 1 or int(myDict["doif"]) >= 1 or int(myDict["dorepeat"]) >= 1:
        repeat_forever= 1
    if int(myDict["dountil"]) >= 1 or int(myDict["dowaituntil"]):
        repear_until = 1
    flow_control = sequence_of_blocks + repeat_forever + repear_until
    #print(flow_control)

#This is the User Interactivity : CT Concept
#User Interactivity: events
    if int(myDict["eventhatmorph_startclicked"]) >= 1:
        greenflag = 1
    if int(myDict["keyeventhatmorph"]) >= 1 or int(myDict["mouseclickeventhatmorph"]) >= 1 or int(myDict["doask"]) >= 1 or int(myDict["touching"]) >= 1 or int(myDict["touchingcolor"]) >= 1 or int(myDict["mousepressed"]) >= 1 or int(myDict["gotospriteormouse"]) >= 1 or int(myDict["gotox_y"]) >= 1 or int(myDict["gotox_y_duration_elapsed_from"]) >= 1:
        mouse_key_events = 1
    user_interactivity = greenflag + mouse_key_events + webcam_microphone

#This is the Synchronization : CT Concept
#Synchronisation: wait, broadcast, wait_until, when
    if int(myDict["wait_elapsed_from"]) >= 1:
        wait = 1
    if int(myDict["broadcast"]) >= 1 or int(myDict["dobroadcastandwait"]) >= 1:
        broadcast = 1
    if int(myDict["dowaituntil"]) >= 1 or int(myDict["whenhatblockmorph"]) >= 1:
        wait_until_when = 1
    synchronization = wait + broadcast + wait_until_when

#This is the Data Representation : CT Concept
#Data Representation: state change blocks, variables, lists
    if int(myDict["gotox_y"]) >= 1 or int(myDict["gotox_y_duration_elapsed_from"]) >= 1 or int(myDict["set_xpos"]) >= 1 or int(myDict["set_ypos"]) >= 1 or int(myDict["changexposby"]) >= 1 or int(myDict["changeyposby"]) >= 1 or int(myDict["changesizeby"]) >= 1 or int(myDict["setsizeto"]) >=1 or int(myDict["point_in_direction"]) >= 1 or int(myDict["pointtowards"]) >= 1 or int(myDict["turnright"]) >= 1 or int(myDict["turnleft"]) >= 1 or int(myDict["changecostumeindexby"]) >= 1 or int(myDict["nextcostume"]) >= 1 or int(myDict["show"]) >= 1 or int(myDict["hide"]) >= 1 or int(myDict["forward"]) >= 1:
        predef_vars = 1
    #print myDict.keys()
    for key in myDict.keys():
        try:
            value = int(myDict[key])
        except:
            value = 0
        if value >= 1:
            if "var" in key:
                variables = 1
            elif "list" in key:
                lists = 1
    data_representation = predef_vars + variables + lists



    return {
        "logical_thinking":logical_thinking,
        "flow_control":flow_control,
        "user_interactivity":user_interactivity,
        "synchronization":synchronization,
        "data_representation":data_representation
    }
