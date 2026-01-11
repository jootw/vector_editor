from PySide6.QtWidgets import QPushButton, QFileDialog

from event.open_file_event import OpenFileEvent


class OpenFileButton(QPushButton):
    def __init__(self, event_bus):
        super().__init__("Open file")
        self._event_bus = event_bus
        self.clicked.connect(self._open_file_dialog)

    def _open_file_dialog(self):
        # Open the file picker
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "*.slop"
        )

        if path:
            self._event_bus.call_event(OpenFileEvent(path))