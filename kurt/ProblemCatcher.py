#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return

    #
    # def hide_show_problem(self,fileName):
    #     project = kurt.Project.load(fileName)
    #     for sprite in project.sprites:
    #         hide_count = 0
    #         show_count = 0
    #         for script in sprite.scripts:
    #             for block in script:
    #                 print block.stringify()
    #                 if (block.stringify() == "hide"):
    #                     hide_count+=1
    #                 if (block.stringify() == "show"):
    #                     show_count+=1
    #         if ( hide_count >= 1 and show_count >= 1 or (hide_count == 0 and show_count == 0) ):
    #             print('Good')
    #         else:
    #             print('Bad')
    #     return project.name




    class emptyConditionHandler:
        """
        @param scratchfile: the name of the scratch file to be tested with
            get_empty_counts()
        @return: tbd (nothing for now)
        """
        @staticmethod 
        def test_emptyConditionHandler(scratchfile):
            project = kurt.Project.load(scratchfile)
            counter = 0
            for sprite in project.sprites:
                for script in sprite.scripts: 
                    print ProblemCatcher.emptyConditionHandler.get_empty_counts(script)
                    counter += 1
        
            return 0
    	
        """
        @param blocks: 	an array of kurt blocks
        @returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in a control block
    					the second value in the array holds the number of empty
    						blocks within control blocks
        """
        @staticmethod
        def get_empty_counts(script):
            falseNullCounts = [0,0]# falseNullCounts = {falseCount, nullCount}
            subCounts = [0,0]
            #****************Control Block Split Array************************
            ifChecker = ["<('if", 'then\\n', "\\n'", "shape='stack')>"]
            ifElseChecker = ["<('if", 'then\\n', '\\nelse\\n', "\\n'", "shape='stack')>"]
            found = True
            for block in script:
                temp = block.type.__repr__().split()



                #**************Find If***************
                for x in range(len(ifChecker)): 
                    if len(temp) == len(ifChecker):
                        if ifChecker[x] != temp[x]:
                            found = False
                    else:
                        found = False
                if found:#case 'if' found
                    #print "Found If"
                    subCounts = ProblemCatcher.emptyConditionHandler.doIfEmptyCounter(block)
                else:
                    found = True
                    
                    
                    
                    
                #**************Find Else***************  
                for x in range(len(ifElseChecker)): 
                    if len(temp) == len(ifElseChecker):
                        if ifElseChecker[x] != temp[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'if else' found
                    #print "Found If Else"
                    subCounts = ProblemCatcher.emptyConditionHandler.doIfElseEmptyCounter(block)
                else:
                    found = True
                    
                    
                    
                #continue for all necessary cases
                #only doIfElse and doIf here for proof of concept
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            return falseNullCounts    
    		
    		
    	"""
    		@param block: 	a kurt doIfElse block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the doIfElse block
    					the second value in the array holds the number of empty
    						blocks within the doIfElse block
    	
    	"""
        @staticmethod
        def	doIfElseEmptyCounter(block):
            falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] == False:#empty condition
            	falseNullCounts[0] += 1
            if block.args[1] != None:#case empty if
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            if len(block.args) > 2:
                if block.args[2] != None:#case empty else
                    subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[2])
                    falseNullCounts[0] += subCounts[0]
                    falseNullCounts[1] += subCounts[1]
                else:
                    falseNullCounts[1] += 1   
                
                
                
            return falseNullCounts    
    		
    	"""
    		@param block: 	a kurt doIf block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the doIfElse block
    					the second value in the array holds the number of empty
    						blocks within the doIf block
    	
    	"""
        @staticmethod
        def	doIfEmptyCounter(block):
            falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] == False:#empty condition
            	falseNullCounts[0] += 1
            if block.args[1] != None:#case empty if
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
    		
    		


    def multiple_if(self,fileName):
        project = kurt.Project.load(fileName)
        for sprite in project.sprites:
            count_if = 0
            for script in sprite.scripts:
                for block in script:
                    if "doIfElse" in block.__repr__():
                        print block.__repr__()
                        print block.args
                        print block.args[0]
                        for arg in block.args:
                            print block.args
                            # block.args = block.args.split(',')
                            # print block.args
                            #eval(block.args)
                        #
                        #     print list[0]
                            #instanceof(arg,kurt.block)

                    # print block.__repr__()
                    # if ("doIfElse" in block.__repr__() and '[' not in block.__repr__()) or "doIf" in block.__repr__() and '(' in block.__repr__():
                    #     #print block.__repr__()
                    #     print('The block is empty')
                    # #The if statement checks if their is an 'if' statement and if their is starting paranthesis to it. If yes, then it should print the entire block.
                    # if "doIf" in block.__repr__() and '[' in block.__repr__():
                    # #     print block.__repr__()
                    #     #if block.__repr__() is None:
                    #     print('The block is not empty')

                #     if "if" in block.stringify() :
                #          if "if" in self.:
                #                  count_if+=1
                # if (count_if >= 1):
                #     print count_if
                # else:
                #     print('No ifs')
        return project.name

# def if_noelse(self,fileName):
#     project = kurt.Project.load(fileName)
#     for sprite in project.sprites:
#         count_if_noelse = 0
#         for script in sprite.scripts:
#             for block in script:
#                 print block.stringify()
#                 if "if" in block.stringify() :
#                      if "else" not in block.stringify():
#                              count_if_noelse+=1
#             if (count_if_noelse >= 1):
#                 print ('if but no elses exist')
#             else:
#                 print('if and else both exist')
#     return project.name
#
#     def if_nocode(self,fileName):
#         project = kurt.Project.load(fileName)
#         for sprite in project.sprites:
#             count_if_nocode = 0
#             for script in sprite.scripts:
#                 for block in script:
#                     print block.stringify()
#                     if "if" in block.stringify() :
#                          if block.stringify() is null:
#                                  count_if_nocode+=1
#                 if (count_if_noelse >= 1):
#                     print ('if but no code exits')
#                 else:
#                     print('if and code both exist')
#         return project.name
