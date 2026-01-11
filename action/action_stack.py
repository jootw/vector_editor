
class ActionStack:
    def __init__(self):
        self._undoStack = []
        self._redoStack = []

    def do(self, action):
        action.redo()
        self._undoStack.append(action)
        self._redoStack = []

    def redo(self):
        if len(self._redoStack) == 0:
            return
        self._redoStack[-1].redo()
        self._undoStack.append(self._redoStack[-1])
        self._redoStack.pop()

    def undo(self):
        if len(self._undoStack) == 0:
            return
        self._undoStack[-1].undo()
        self._redoStack.append(self._undoStack[-1])
        self._undoStack.pop()
