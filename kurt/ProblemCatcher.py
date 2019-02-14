#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return


    def hide_show_problem(self,fileName):
        project = kurt.Project.load(fileName)
        for sprite in project.sprites:
            for script in sprite.scripts:
                for block in script:
                    print block.stringify()
        return project.name
