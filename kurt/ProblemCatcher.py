#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return

    """
        @param fileName: a scratch file name in string form
        @return the number of hide show problems within the program
            this should be a number from 0 to the number of sprites in
            the project. This accounts for deadcode which can
            never be called.
    """
    def hide_show_problem(self,fileName):
        project = kurt.Project.load(fileName)
        hide_show_problem_count = 0
        print "Finding Hide Show Problems"
        for sprite in project.sprites:
            hide_show_problem_count += ProblemCatcher.sprite_has_hide_show_problem(sprite)
                
        return hide_show_problem_count
            
            
            
    """
        @param sprite: a kurt sprite object
        @return: returns 1 if the sprite has a hide show problem
            and 0 otherwise. This accounts for deadcode which can
            never be called.
    """
    @staticmethod
    def sprite_has_hide_show_problem(sprite):
        hide_count = 0
        show_count = 0
        hide_show_problem_count = 0
        for script in sprite.scripts:
            #only care about script if script is not dead code
            deadCodeChecker = script[0].type.__repr__().split()[-1]
            if ("shape='hat')>" == deadCodeChecker): 
                if "hide" in script.__repr__():
                    hide_count += 1
                if "show" in script.__repr__():
                    show_count += 1      
          
        if ( hide_count >= 1 and show_count <= 0):
            print "Hide found without a Show: {0}".format(sprite.name)
            hide_show_problem_count += 1
        elif (hide_count <= 0 and show_count >= 1):
            print "Show found without a Hide: {0}".format(sprite.name)
            hide_show_problem_count += 1
        return  hide_show_problem_count
        
        

    class emptyConditionHandler:
        """
        @param scratchfile: the name of the scratch file to be tested with
            get_empty_counts()
        @return: the number 0 upon success
        """
        @staticmethod 
        def test_emptyConditionHandler(scratchfile):
            project = kurt.Project.load(scratchfile)
            counter = 0
            print "Testing Empty Condition Handler"
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
            foreverChecker = ["<('forever\\n", "\\n'", "shape='cap')>"]
            foreverIfChecker = ["<('forever", 'if', '\\n', "\\n'", "shape='cap')>"]
            repeatUntilChecker = ["<('repeat", 'until', '\\n', "\\n'", "shape='stack')>"]
            repeatNTimesChecker = ["<('repeat", '10\\n', "\\n'", "shape='stack')>"]
            waitUntilChecker = ["<('wait", 'until', "'", "shape='stack')>"]
            broadcastChecker = ['<(u"broadcast', '\'\'"', "shape='stack')>"]
            broadcastAndWaitChecker = ['<(u"broadcast', "''", 'and', 'wait"', "shape='stack')>"]#to do
            whenIRecieveChecker = ['<(u"when', 'I', 'receive', '\'\'"', "shape='hat')>"]


            found = True
            for block in script:
                blockType = block.type.__repr__().split()
                #print blockType


                #**************Find If***************
                for x in range(len(ifChecker)): 
                    if len(blockType) == len(ifChecker):
                        if ifChecker[x] != blockType[x]:
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
                    if len(blockType) == len(ifElseChecker):
                        if ifElseChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'forever' found
                    #print "Found If Else"
                    subCounts = ProblemCatcher.emptyConditionHandler.doIfElseEmptyCounter(block)
                else:
                    found = True
                
                    
                    
                #*************Find Forever*************  
                for x in range(len(foreverChecker)): 
                    if len(blockType) == len(foreverChecker):
                        if foreverChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'forever' found
                    #print "Found forever"
                    subCounts = ProblemCatcher.emptyConditionHandler.doForeverEmptyCounter(block)
                else:
                    found = True
                    
                    
                
                #***********Find Forever If***********  
                for x in range(len(foreverIfChecker)): 
                    if len(blockType) == len(foreverIfChecker):
                        if foreverIfChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'forever if' found
                    #print "Found forever if"
                    subCounts = ProblemCatcher.emptyConditionHandler.doForeverIfEmptyCounter(block)
                else:
                    found = True
                    
                #**********Find Repeat Until***********  
                for x in range(len(repeatUntilChecker)): 
                    if len(blockType) == len(repeatUntilChecker):
                        if repeatUntilChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'repeat until' found
                    #print "Found repeat until"
                    subCounts = ProblemCatcher.emptyConditionHandler.doRepeatUntilEmptyCounter(block)
                else:
                    found = True
                
                #**********Find Repeat Until***********  
                for x in range(len(repeatNTimesChecker)): 
                    if len(blockType) == len(repeatNTimesChecker):
                        if repeatNTimesChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'repeat until' found
                    #print "Found repeat until"
                    subCounts = ProblemCatcher.emptyConditionHandler.doRepeatNTimesEmptyCounter(block)
                else:
                    found = True
                
                
                
                #**********Find Wait Until***********  
                for x in range(len(waitUntilChecker)): 
                    if len(blockType) == len(waitUntilChecker):
                        if waitUntilChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'wait until' found
                    #print "Found wait until"
                    subCounts = ProblemCatcher.emptyConditionHandler.doWaitUntilEmptyCounter(block)
                else:
                    found = True
                
                
                #**********Find Broadcast***********  
                for x in range(len(broadcastChecker)): 
                    if len(blockType) == len(broadcastChecker):
                        if broadcastChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'broadcast' found
                    #print "Found broadcast"
                    subCounts = ProblemCatcher.emptyConditionHandler.doBroadcastEmptyCounter(block)
                else:
                    found = True
                
                
                #*******Find Broadcast And Wait******* 
                for x in range(len(broadcastAndWaitChecker)): 
                    if len(blockType) == len(broadcastAndWaitChecker):
                        if broadcastAndWaitChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'broadcast and wait' found
                    #print "Found broadcast and wait"
                    subCounts = ProblemCatcher.emptyConditionHandler.doBroadcastEmptyCounter(block)
                else:
                    found = True
                
                
                #*********Find When I Recieve********* 
                for x in range(len(whenIRecieveChecker)): 
                    if len(blockType) == len(whenIRecieveChecker):
                        if whenIRecieveChecker[x] != blockType[x]:
                            found = False
                    else:
                        found = False
                        
                if found:#case 'when I recieve' found
                    #print "Found when I recieve"
                    subCounts = ProblemCatcher.emptyConditionHandler.doWhenIRecieveEmptyCounter(block)
                else:
                    found = True
                
                
                
                
                #continue for all cases 
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
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            if block.args[1] != None:#case empty if
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
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
    						no condition is put in the doIf block
    					the second value in the array holds the number of empty
    						blocks within the doIf block
    	
    	"""
        @staticmethod
        def	doIfEmptyCounter(block):
            falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] == False:#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            if block.args[1] != None:#case empty if
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
            
        """
    		@param block: 	a kurt forever block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the forever block
    					the second value in the array holds the number of empty
    						blocks within the forever block
    	"""
        @staticmethod
        def doForeverEmptyCounter(block): 
            falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] != None:#case empty forever
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[0])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
            
        """
    		@param block: 	a kurt foreverIf block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the foreverIf block
    					the second value in the array holds the number of empty
    						blocks within the foreverIf block
    	"""
        @staticmethod
        def doForeverIfEmptyCounter(block):     
            falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] == False:#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            if block.args[1] != None:#case empty forever
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
    		
    		
    		
    	"""
    		@param block: 	a kurt repeat until block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the repeat until block
    					the second value in the array holds the number of empty
    						blocks within the repeat until block
    	"""
        @staticmethod	
        def doRepeatUntilEmptyCounter(block):
    	    falseNullCounts = [0,0]
            subCounts = [0,0]
            if block.args[0] == False:#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            if block.args[1] != None:#case empty repeat
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
    		
    		
    		
    		
    		
    		
    	"""
    		@param block: 	a kurt repeat n times block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the repeat n times block
    					the second value in the array holds the number of empty
    						blocks within the repeat n times block
    	"""
        @staticmethod	
        def doRepeatNTimesEmptyCounter(block):
    	    falseNullCounts = [0,0]
            subCounts = [0,0]
            #if block.args[0] == '':#empty condition
            #    falseNullCounts[0] += 1
            if block.args[1] != None:#case empty repeat
                subCounts = ProblemCatcher.emptyConditionHandler.get_empty_counts(block.args[1])
                falseNullCounts[0] += subCounts[0]
                falseNullCounts[1] += subCounts[1]
            else:
                falseNullCounts[1] += 1
            return falseNullCounts
    		    
    	
    	
    	
    	
    	"""
    		@param block: 	a kurt wait until block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the wait until block
    					the second value in the array holds the number of empty
    						blocks within the wait until block
    	"""
        @staticmethod	
        def doWaitUntilEmptyCounter(block):
            falseNullCounts = [0,0]
            if block.args[0] == False:#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            return falseNullCounts
        
        
        
        """
    		@param block: 	a kurt broadcast block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the broadcast block
    					the second value in the array holds the number of empty
    						blocks within the broadcast block
    	"""
    	@staticmethod
    	def doBroadcastEmptyCounter(block):
            falseNullCounts = [0,0]
            if block.args[0] == '':#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            return falseNullCounts
        
        
        
        
        
        """
    		@param block: 	a kurt when I recieve block
        	@returns: 		an array of length 2
    					the first value in the array holds the number of times
    						no condition is put in the when I recieve block
    					the second value in the array holds the number of empty
    						blocks within the when I recieve block
    	"""
        @staticmethod
        def doWhenIRecieveEmptyCounter(block):
            falseNullCounts = [0,0]
            if block.args[0] == '':#empty condition
                falseNullCounts[0] += 1
            else:
                falseNullCounts[0] += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(block.args[0])
            return falseNullCounts
        
        
        	
    	"""
    	    @param block: a Kurt conditional block
    	    @return the number of empty conditional blocks
    	    within the conditional block @param block
    	
    	"""
        @staticmethod
        def conditionalEmptyCounter(block):
            emptyCounter = 0
            if hasattr(block,'args'):
                for arg in block.args:
                    if arg == False or arg == '':
                        emptyCounter += 1
                    else:
                        emptyCounter += ProblemCatcher.emptyConditionHandler.conditionalEmptyCounter(arg)
            return emptyCounter


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
