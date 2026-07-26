from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PhotoGraph")
        self.resize(900, 600)

        self.label = QLabel("Folder not selected")

        self.button = QPushButton("Select folder")
        self.button.clicked.connect(self.select_folder)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select photo folder"
        )

        if folder:
            self.label.setText(folder)