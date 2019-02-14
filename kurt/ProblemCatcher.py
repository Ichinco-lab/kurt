#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return


    def hide_show_problem(self,fileName):
        project = kurt.Project.load(fileName)
        for sprite in project.sprites:
            hide_count = 0
            show_count = 0
            for script in sprite.scripts:
                for block in script:
                    print block.stringify()
                    if (block.stringify() == "hide"):
                        hide_count+=1
                    if (block.stringify() == "show"):
                        show_count+=1
            if ( hide_count >= 1 and show_count >= 1 or (hide_count == 0 and show_count == 0) ):
                print('Good')
            else:
                print('Bad')
        return project.name
