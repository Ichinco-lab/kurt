# Abstraction
# Parallelism
# Logical Thinking: Operators + if_else + if
# Synchronization
# Flow control: doforever + doforeverif + doifelse + doif + dorepeat + doreturn + dountil + dowaituntil
# User Interactivity
# Data representation
#
# eventhatmorph_startclicked:

def process(myDict):
    logical_thinking = 0
    operators = 0
    i = 0
    if_else = 0
    sequence_of_blocks = 0
    repeat_forever = 0
    repear_until = 0
    flow_control = 0
    list_operations = 0
    data_representation = 0
    psocv = 0
    wait_condition = 0
    synchronization = 0
    #
    # for dicts in myDict:
    #     for keys in dicts:
    #         dicts[keys] = int(dicts[keys])

#This is the logical Thinking : CT Concept
#Logical Thinking: Operators + if_else + if
    if int(myDict["islessthan"]) >= 1 or int(myDict["and_operator"]) >= 1 or int(myDict["isequalto"]) >= 1 or int(myDict["isgreaterthan"]) >= 1 or int(myDict["or_operator"]) >= 1 or int(myDict["not"]) >= 1:
        operators = 1
    if int(myDict["doif"]) >= 1:
        i = 1
    if int(myDict["doifelse"]) >= 1:
        if_else = 1
    logical_thinking = operators + i + if_else
    print("Logical Thinking Value:")
    print(logical_thinking)

#This is the Flow Control : CT Concept
# Flow control: doforever + doforeverif + doifelse + doif + dorepeat + doreturn + dountil + dowaituntil
    if int(myDict["doforever"]) >= 1 or int(myDict["doforeverif"]) >= 1 or int(myDict["doifelse"]) >= 1 or int(myDict["doif"]) >= 1:
        sequence_of_blocks = 1
    if int(myDict["dorepeat"]) >= 1:
        repeat_forever= 1
    if int(myDict["dountil"]) >= 1 or int(myDict["dowaituntil"]) >=1:
        repear_until = 1
    flow_control = sequence_of_blocks + repeat_forever + repear_until
    print("Flow Control Value:")
    print(flow_control)

#This is the Data Representation
# Data Repesentation =Position + Size + Orientation + Costume + Visibility


# #POSITION: "gobackbylayers","gotospriteormouse","gotox_y","gotox_y_duration_elapsed_from","glidesecs_tox_y_elapsed_from","changebackgroundindexby",
    # "changeblurby","changebrightnessshiftby","changecostumeindexby","changefisheyeby",changegraphiceffect_by","changehueshiftby","changemosaiccountby","changepenhueby","changepenshadeby",
    # "changepensizeby","changepixelatecountby","changepointillizesizeby","changesaturationshiftby","changesizeby","changestretchby","changetempoby",
    # "changevarby","changevisibilityby","changevolumeby","changewaterrippleby","changewhirlby","changexposby","changeyposby",
#SIZE: changesizeby" changepensizeby changepointillizesizeby setsizeto setpointillizesizeto
#ORIENTATION: point_in_direction pointtowards
#TURN: turnawayfromedge turnleft turnright
#VISIBILITY: show","showbackground","showvariable "hide","hidevariable",
#COSTUME: nextbackground","nextcostume
#List: insert_at_of_list append_tolist contentsoflist deletelineoflist getline_of_list "linecountoflist" list_contains doask
    if int(myDict["gobackbylayers"]) >= 1 or int(myDict["gotospriteormouse"]) >= 1 or int(myDict["gotox_y"]) >= 1 or int(myDict["gotox_y_duration_elapsed_from"]) >= 1 or int(myDict["glidesecs_tox_y_elapsed_from"]) >= 1 or int(myDict["changebackgroundindexby"]) >= 1 or int(myDict["changeblurby"]) >= 1 or int(myDict["gotox_y_duration_elapsed_from"]) >= 1 or int(myDict["changebrightnessshiftby"]) >= 1 or int(myDict["changecostumeindexby"]) >= 1 or int(myDict["changefisheyeby"]) >= 1 or int(myDict["changegraphiceffect_by"]) >= 1 or int(myDict["changehueshiftby"]) >= 1 or int(myDict["changemosaiccountby"]) >= 1 or int(myDict["changepenhueby"]) >= 1 or int(myDict["changepenshadeby"]) >= 1 or int(myDict["changepensizeby"]) >= 1 or int(myDict["changepixelatecountby"]) >= 1 or int(myDict["changesaturationshiftby"]) >= 1 or int(myDict["changestretchby"]) >= 1 or int(myDict["changetempoby"]) >= 1 or int(myDict["changevarby"]) >= 1 or int(myDict["changevolumeby"]) >= 1 or int(myDict["changewaterrippleby"]) >= 1 or int(myDict["changexposby"]) >= 1 or int(myDict["changeyposby"]) >= 1 or int(myDict["changesizeby"]) >= 1 or int(myDict["changepensizeby"]) >= 1 or int(myDict["setsizeto"]) >= 1 or int(myDict["setpointillizesizeto"]) >= 1 or int(myDict["point_in_direction"]) >= 1 or int(myDict["pointtowards"]) >= 1 or int(myDict["turnawayfromedge"]) >= 1 or int(myDict["turnleft"]) >= 1 or int(myDict["turnright"]) >= 1 or int(myDict["show"]) >= 1 or int(myDict["showbackground"]) >= 1 or int(myDict["showvariable"]) >= 1 or int(myDict["hide"]) >= 1 or int(myDict["hidevariable"]) >= 1 or int(myDict["nextbackground"]) >= 1 or int(myDict["nextcostume"]) >= 1:
        psocv = 1
    if int(myDict["insert_at_of_list"]) >= 1 or int(myDict["list_contains"]) >= 1 or int(myDict["doask"]) >= 1 or int(myDict["linecountoflist"]) >= 1 or int(myDict["append_tolist"]) >= 1 or int(myDict["contentsoflist"]) >= 1 or int(myDict["deletelineoflist"]) >= 1 or int(myDict["getline_of_list"]) >= 1:
        list_operations = 1
    data_representation = psocv + list_operations

    # print("Data Representation Value:")
    # print(data_representation)

#SYNCHRONIZATION: wait + when
#WAIT:  dobroadcastandwait doplaysoundandwait dowaituntil wait_elapsed_from
#wHEN:
    if int(myDict["dobroadcastandwait"]) >= 1 or int(myDict["doplaysoundandwait"]) >= 1 or int(myDict["dowaituntil"]) >= 1 or int(myDict["wait_elapsed_from"]) >= 1:
        wait_condition = 1
    synchronization += wait_condition
    print("Synchronization Value:")
    print(synchronization)

#PARALLELISM : Clicks + Keys + When
#When the sprite is clicked: whenhatblockmorph
#nextbackground  timer timerreset isloud stopallsounds doplaysoundandwait
    #Returning all the 7 values
    return [logical_thinking,flow_control,data_representation,synchronization]
