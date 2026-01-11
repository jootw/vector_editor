from PySide6.QtWidgets import QFrame, QVBoxLayout

from config import SIDE_BAR_WIDTH, SIDE_BAR_COLOR
from ui.pen_bar import PenBar
from ui.tool_bar import ToolBar


class SideBar(QFrame):
    def __init__(self, event_bus):
        super().__init__()
        self._event_bus = event_bus
        self._layout = QVBoxLayout(self)
        self.setFixedWidth(SIDE_BAR_WIDTH)
        self.setStyleSheet(f"background-color: {SIDE_BAR_COLOR};")
        self._layout.addWidget(ToolBar(self._event_bus))
        self._layout.addWidget(PenBar(self._event_bus))
        self._layout.addStretch()
