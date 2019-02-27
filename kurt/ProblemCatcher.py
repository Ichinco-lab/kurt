#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return


    def hide_show_problem(self,fileName):
        project = kurt.Project.load(fileName, )
        for sprite in project.sprites:
            for script in sprite.scripts:
                for block in script.blocks:
                    if 'doIf' in block.__repr__():
                        for arg in block.args:
                            print block, "arg:", arg
                            instanceof(arg[0], kurt.Block)
        return project.name
