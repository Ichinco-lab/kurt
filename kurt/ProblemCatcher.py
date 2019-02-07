#in this file, we look for problematic code

import kurt


class ProblemCatcher:

    """Default Constructor"""
    def __init__(self):
        return


    def hide_show_problem(self,fileName):
        project = kurt.Project.load(fileName)
        return project.name
