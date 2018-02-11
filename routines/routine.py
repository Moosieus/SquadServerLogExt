"""
Auto Generate a google sheet with server performance graph.
"""


class Routine:
    title = "Base_Routine_Name"

    def __init__(self):
        self.run = True

    def operation(self, line):
        if self.run:
            return ''
