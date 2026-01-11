from action.action import Action

class ActionGroup(Action):
    def __init__(self, canvas, actions):
        super().__init__(canvas)
        self._actions = actions

    def redo(self):
        for action in self._actions:
            action.redo()

    def undo(self):
        for action in self._actions[::-1]:
            action.undo()
