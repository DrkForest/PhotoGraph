from PySide6.QtCore import Qt, QRectF, Signal
from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QPixmap,
)

from PySide6.QtWidgets import (
    QGraphicsObject,
)


class PhotoNode(QGraphicsObject):

    clicked = Signal(object)

    SIZE = 150

    def __init__(self, image_path, thumbnail_path):

        super().__init__()

        self.image_path = image_path
        self.thumbnail_path = thumbnail_path

        self.pixmap = QPixmap(str(thumbnail_path))

        self.pixmap = self.pixmap.scaled(
            self.SIZE,
            self.SIZE,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.selected = False

        self.setAcceptHoverEvents(True)

    def boundingRect(self):

        return QRectF(
            0,
            0,
            self.SIZE,
            self.SIZE
        )

    def paint(
        self,
        painter,
        option,
        widget=None
    ):

        painter.drawPixmap(
            0,
            0,
            self.pixmap
        )

        if self.selected:

            pen = QPen(
                QColor("#2196F3"),
                3
            )

            painter.setPen(pen)

            painter.drawRect(
                self.boundingRect()
            )

    def set_selected(self, selected):

        self.selected = selected
        self.update()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.clicked.emit(self)

        super().mousePressEvent(event)