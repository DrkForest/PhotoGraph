from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
    QPen,
    QPixmap
)
from PySide6.QtWidgets import (
    QGraphicsPixmapItem,
    QGraphicsRectItem
)


class PhotoNode(QGraphicsPixmapItem):

    def __init__(self, image_path, thumbnail_path):

        pixmap = QPixmap(str(thumbnail_path))

        pixmap = pixmap.scaled(
            150,
            150,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        super().__init__(pixmap)

        self.image_path = image_path
        self.thumbnail_path = thumbnail_path

        self.border = QGraphicsRectItem(
            self.boundingRect(),
            self
        )

        self.border.setPen(
            QPen(
                QColor("transparent"),
                3
            )
        )