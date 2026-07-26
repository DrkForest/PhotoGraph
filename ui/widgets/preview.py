from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class PreviewWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setText(
            "Preview"
        )

        self.setMinimumSize(
            250,
            180
        )

        self.setAlignment(
            Qt.AlignCenter
        )