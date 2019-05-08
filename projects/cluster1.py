def process(myDict):
    logical_thinking = 0
    operators = 0
    i = 0
    if_else = 0
    sequence_of_blocks = 0
    repeat_forever = 0
    repear_until = 0
    flow_control = 0
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

    return [logical_thinking,flow_control]
