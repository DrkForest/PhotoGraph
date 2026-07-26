from PySide6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from ui.graphics.photo_node import PhotoNode


class GraphView(QGraphicsView):

    THUMB_SPACING = 170
    COLUMNS = 6

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(
            400
        )

        self.scene = QGraphicsScene()

        self.setScene(
            self.scene
        )

        self.setAlignment(
            Qt.AlignLeft | Qt.AlignTop
        )

        self.scene.addText(
            "PhotoGraph Graph Area"
        )

    def clear(self):

        self.scene.clear()

    def show_images(self, images, thumbnails):

        self.scene.clear()

        for i, thumb in enumerate(thumbnails):

            node = PhotoNode(
                images[i],
                thumbnails[i]
            )

            x = (i % self.COLUMNS) * self.THUMB_SPACING
            y = (i // self.COLUMNS) * self.THUMB_SPACING

            node.setPos(x, y)

            self.scene.addItem(node)

        self.scene.setSceneRect(
            self.scene.itemsBoundingRect()
        )