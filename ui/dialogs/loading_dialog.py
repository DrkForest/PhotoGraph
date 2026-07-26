from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout


class LoadingDialog(QDialog):

    def __init__(self, text="Loading..."):
        super().__init__()

        self.setWindowTitle("PhotoGraph")
        self.setModal(True)

        self.setWindowFlag(
            Qt.WindowContextHelpButtonHint,
            False
        )

        self.label = QLabel(text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setFixedSize(
            280,
            100
        )

    def set_text(self, text):
        self.label.setText(text)