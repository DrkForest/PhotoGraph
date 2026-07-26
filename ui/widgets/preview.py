from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class PreviewWidget(QLabel):

    def __init__(self):
        super().__init__()

        self.setText("Preview")

        self.setMinimumSize(
            250,
            180
        )

        self.setAlignment(
            Qt.AlignCenter
        )

        self.setScaledContents(False)

        self.current_pixmap = None


    def show_image(self, image_path):

        pixmap = QPixmap(str(image_path))

        self.current_pixmap = pixmap

        self._update_pixmap()


    def resizeEvent(self, event):

        super().resizeEvent(event)

        self._update_pixmap()


    def _update_pixmap(self):

        if self.current_pixmap is None:
            return

        pixmap = self.current_pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(pixmap)