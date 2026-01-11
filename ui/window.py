from PySide6.QtGui import QCloseEvent, QAction
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QHBoxLayout

from config import WINDOW_WIDTH, WINDOW_HEIGHT
from event.request_redo_event import RequestRedoEvent
from event.request_undo_event import RequestUndoEvent
from ui.side_bar import SideBar


class VectorEditorWindow(QMainWindow):
    def __init__(self, event_bus, canvas):
        super().__init__()
        self._event_bus = event_bus
        self._canvas = canvas

        self._setupUi()

    def _setupUi(self):
        self.setWindowTitle("Vector Editor")
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self._setupLayout()
        self._setupMenubar()

        self.statusBar().showMessage("UI initialized")

    def _setupLayout(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        side_bar = SideBar(self._event_bus)

        layout.addWidget(side_bar)
        layout.addWidget(self._canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _setupMenubar(self):
        self.menubar = self.menuBar()

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl + Q")
        exitAction.setStatusTip("Close the application")
        exitAction.triggered.connect(self.close)

        fileMenu = self.menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        undoAction = QAction("Undo", self)
        undoAction.setShortcut("Ctrl + Z")
        undoAction.setStatusTip("Undo last change")
        undoAction.triggered.connect(lambda: self._event_bus.call_event(RequestUndoEvent()))

        redoAction = QAction("Redo", self)
        redoAction.setShortcut("Ctrl + Shift + Z")
        redoAction.setStatusTip("Redo last undo")
        redoAction.triggered.connect(lambda: self._event_bus.call_event(RequestRedoEvent()))

        fileMenu = self.menubar.addMenu("&Actions")
        fileMenu.addAction(undoAction)
        fileMenu.addAction(redoAction)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(
            self, "Confirmation",
            "Are you sure you want to quit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
