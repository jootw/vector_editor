from PySide6.QtWidgets import QFrame, QHBoxLayout

from ui.tool_button import ToolButton


class ToolBar(QFrame):
    def __init__(self, event_bus):
        super().__init__()
        self._event_bus = event_bus
        self._layout = QHBoxLayout(self)
        self._layout.addWidget(ToolButton(event_bus, "line", "Line /"))
        self._layout.addWidget(ToolButton(event_bus, "rect", "Rect □"))
        self._layout.addWidget(ToolButton(event_bus, "ellipse", "Ellipse ◯"))
