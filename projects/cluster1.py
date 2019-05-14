
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
    sync_proficiency = 0
    sync_develop = 0
    variable_operations = 0
    ui_develop = 0
    green_flag = 0
    ui = 0
#This is the logical Thinking : CT Concept
#Logical Thinking: Operators + if_else + if
    if int(myDict["islessthan"]) >= 1 or int(myDict["and_operator"]) >= 1 or int(myDict["isequalto"]) >= 1 or int(myDict["isgreaterthan"]) >= 1 or int(myDict["or_operator"]) >= 1 or int(myDict["not"]) >= 1:
        operators = 1
    if int(myDict["doif"]) >= 1:
        i = 1
    if int(myDict["doifelse"]) >= 1:
        if_else = 1
    logical_thinking = operators + i + if_else
    # print("Logical Thinking Value:")
    # print(logical_thinking)

# Flow Control : CT Concept
# Flow control: doforever + doforeverif + doifelse + doif + dorepeat + doreturn + dountil + dowaituntil
    if myDict["doifelse"] >= 1 or myDict["doif"] >= 1:
        sequence_of_blocks = 1
    if myDict["dorepeat"] >= 1 or myDict["doforever"] >= 1 or myDict["doforeverif"] >= 1:
        repeat_forever= 1
    if myDict["dountil"] >= 1:
        repear_until = 1
    flow_control = sequence_of_blocks + repeat_forever + repear_until
    #print(flow_control)

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
    if int(myDict["readvariable"]) >= 1 or int(myDict["showvariable"]) >= 1 or int(myDict["hidevariable"]) >= 1:
        variable_operations = 1
    if int(myDict["insert_at_of_list"]) >= 1 or int(myDict["list_contains"]) >= 1 or  int(myDict["linecountoflist"]) >= 1 or int(myDict["append_tolist"]) >= 1 or int(myDict["contentsoflist"]) >= 1 or int(myDict["deletelineoflist"]) >= 1 or int(myDict["getline_of_list"]) >= 1:
        list_operations = 1
    data_representation = psocv + list_operations

    # print("Data Representation Value:")
    # print(data_representation)

#SYNCHRONIZATION: wait + when
#WAIT:  dobroadcastandwait doplaysoundandwait dowaituntil wait_elapsed_from
#wHEN:
    if int(myDict["wait_elapsed_from"]) >= 1:
        wait_condition = 1
    if  int(myDict["broadcast"]) >= 1 or int(myDict["dobroadcastand"]) >= 1 or int(myDict["stopall"]) >= 1:
        sync_develop = 1
    if  int(myDict["dobroadcastandwait"]) >= 1 or int(myDict["dowaituntil"]) >= 1:
        sync_proficiency = 1
    synchronization = wait_condition + sync_proficiency + sync_develop
    # print("Synchronization Value:")
    # # print(synchronization)

    #USER INTERACTIVITY
    if int(myDict["eventhatmorph_startclicked"]) >= 1:
        green_flag = 1
    if  int(myDict["keyeventhatmorph"]) >= 1 or int(myDict["keypressed"]) >= 1 or int(myDict["doask"]) >= 1 or int(myDict["mousex"]) >= 1 or int(myDict["mousey"]) >= 1 or int(myDict["mousepressed"]) >= 1:
        ui_develop = 1

    ui = ui_develop + green_flag
    # print("Synchronization Value:")
    # # print(synchronization)
    #Returning all the 7 values
    return [logical_thinking,flow_control,data_representation,synchronization,ui]
