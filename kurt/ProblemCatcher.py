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
