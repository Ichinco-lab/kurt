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
        @param blocks: 	an array of kurt blocks
        @returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in a control block
    					the second value in the array holds the number of empty
    						blocks within control blocks
        """
        @staticmethod
        def get_empty_counts(script):
            falseNullCounts = {0,0}# falseNullCounts = {falseCount, nullCount}
            subCounts = {0,0}
            for block in script:
                if "doIfElse" in block.repr():
                    subCounts = doIfElseEmptyCounter(block)
                elif "doIf" in block.repr():
                    subCounts = doIfEmptyCounter(block)
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
            falseNullCounts = {0,0}
            subCounts = {0,0}
            if block.args[0] != "False":#empty condition
            	subCounts[0] += 1
            if block.args[1] != "None":#empty if
                subCounts = get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            if block.args[2] != "None":#empty else
                subCounts = get_empty_counts(block.args[2])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1   
                
                
                
            return falseNullCounts    #stub function
    		
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
            falseNullCounts = {0,0}
            subCounts = {0,0}
            if block.args[0] != "False":#empty condition
            	subCounts[0] += 1
            if block.args[1] != "None":#empty if
                subCounts = get_empty_counts(block.args[1])
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
