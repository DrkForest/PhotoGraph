from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
)


class Toolbar(QWidget):
    def __init__(self):
        super().__init__()

        self.select_button = QPushButton(
            "Select folder"
        )

        layout = QHBoxLayout()

        layout.addWidget(
            self.select_button
        )

        self.setLayout(layout)