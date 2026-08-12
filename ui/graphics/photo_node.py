from PySide6.QtCore import Qt, QRectF, Signal
from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QPixmap,
)
from PySide6.QtWidgets import QGraphicsObject


class PhotoNode(QGraphicsObject):

    clicked = Signal(object)

    NORMAL_SIZE = 150
    MIN_SIZE = 150
    MAX_SIZE = 150

    def __init__(self, photo):

        super().__init__()

        self.photo = photo

        self.image_path = photo.image
        self.thumbnail_path = photo.thumbnail

        self.selected = False
        self.neighbor_highlighted = False

        self.pixmap = QPixmap(
            str(self.thumbnail_path)
        )

        self._update_pixmap()

        self.setAcceptHoverEvents(True)

    def boundingRect(self):

        return QRectF(
            0,
            0,
            self.NORMAL_SIZE,
            self.NORMAL_SIZE
        )

    def _update_pixmap(self):

        self.pixmap = self.pixmap.scaled(
            self.NORMAL_SIZE,
            self.NORMAL_SIZE,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.photo_rect = QRectF(
            0,
            0,
            self.pixmap.width(),
            self.pixmap.height()
        )

        self.photo_rect.moveCenter(
            self.boundingRect().center()
        )

    def set_size(self, size):

        # LOD більше не змінює геометричний розмір вузла.
        # Zoom робить сам QGraphicsView.
        return

    def paint(
        self,
        painter,
        option,
        widget=None
    ):

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform,
            True
        )

        # Саме фото, відцентроване всередині вузла.
        painter.drawPixmap(
            self.photo_rect.topLeft(),
            self.pixmap
        )

        # Рамка тільки навколо реального фото.
        if self.selected:

            pen = QPen(
                QColor("#2196F3"),
                3
            )

            painter.setPen(pen)

            painter.drawRect(
                self.photo_rect
            )

        elif self.neighbor_highlighted:

            pen = QPen(
                QColor("#777777"),
                2
            )

            painter.setPen(pen)

            painter.drawRect(
                self.photo_rect
            )

    def set_selected(self, selected):

        self.selected = selected

        self.update()

    def set_neighbor_highlighted(self, highlighted):

        self.neighbor_highlighted = highlighted

        self.update()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.clicked.emit(self)

            event.accept()

            return

        super().mousePressEvent(event)