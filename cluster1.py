def process(myDict):
    logical_thinking = 0
    operators = 0
    i = 0
    if_else = 0
    sequence_of_blocks = 0
    repeat_forever = 0
    repear_until = 0
    flow_control = 0

#This is the logical Thinking : CT Concept
#Logical Thinking: Operators + if_else + if
    if myDict["islessthan"] >= 1 or myDict["and_operator"] >= 1 or myDict["isequalto"] >= 1 or myDict["isgreaterthan"] >= 1 or myDict["or_operator"] >= 1 or myDict["not"] >= 1:
        operators = 1
    if myDict["doif"] >= 1:
        i = 1
    if myDict["doifelse"] >= 1:
        if_else = 1
    logical_thinking = operators + i + if_else
    #print(logical_thinking)

#This is the Flow Control : CT Concept
# Flow control: doforever + doforeverif + doifelse + doif + dorepeat + doreturn + dountil + dowaituntil
    if myDict["doforever"] >= 1 or myDict["doforeverif"] >= 1 or myDict["doifelse"] >= 1 or myDict["doif"] >= 1:
        sequence_of_blocks = 1
    if myDict["dorepeat"] >= 1:
        repeat_forever= 1
    if myDict["dountil"] >= 1 or myDict["dowaituntil"]:
        repear_until = 1
    flow_control = sequence_of_blocks + repeat_forever + repear_until
    #print(flow_control)

    return [logical_thinking,flow_control]
