from PySide6.QtWidgets import QFrame, QHBoxLayout

from ui.open_file_button import OpenFileButton
from ui.save_file_button import SaveFileButton


class FileBar(QFrame):
    def __init__(self, event_bus):
        super().__init__()
        self._event_bus = event_bus
        self._layout = QHBoxLayout(self)
        self._layout.addWidget(OpenFileButton(self._event_bus))
        self._layout.addWidget(SaveFileButton(self._event_bus))
