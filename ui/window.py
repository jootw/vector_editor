from PySide6.QtGui import QCloseEvent, QAction
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QHBoxLayout

from config import WINDOW_WIDTH, WINDOW_HEIGHT
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

        # picker = QPushButton()
        # picker.setStyleSheet(f"background-color: {CANVAS_INITIAL_COLOR.name()}")
        # picker.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # picker.clicked.connect(lambda: self.canvas.setColor(QColorDialog().getColor()))

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

        # undoAction = QAction("Undo", self)
        # undoAction.setShortcut("Ctrl + Z")
        # undoAction.setStatusTip("Undo last change")
        # undoAction.triggered.connect(self.canvas.undo())

        # redoAction = QAction("Redo", self)
        # redoAction.setShortcut("Ctrl + Shift + Z")
        # redoAction.setStatusTip("Redo last undo")
        # redoAction.triggered.connect(self.canvas.redo())

        fileMenu = self.menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

    # def changeTool(self, tool, clicked):
    #     for button in self._toolButtons:
    #         button.setChecked(False)
    #     clicked.setChecked(True)
    #     self.canvas.setTool(tool)

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
