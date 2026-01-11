from PySide6.QtWidgets import QPushButton, QFileDialog

from event.save_file_event import SaveFileEvent


class SaveFileButton(QPushButton):
    def __init__(self, event_bus):
        super().__init__("Save as")
        self._event_bus = event_bus
        self.clicked.connect(self._open_file_dialog)

    def _open_file_dialog(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save As...",
            "untitled.slop",
            "All Files (*)"
        )

        if path:
            self._event_bus.call_event(SaveFileEvent(path))
