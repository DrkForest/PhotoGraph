from pathlib import Path
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
)

from ui.graphics.photo_node import PhotoNode


class GraphView(QGraphicsView):

    THUMB_SPACING = 170
    COLUMNS = 6

    photo_selected = Signal(Path)

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(400)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.selected_node = None

        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.setDragMode(QGraphicsView.NoDrag)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scene.addText("PhotoGraph Graph Area")

    def clear(self):

        self.scene.clear()

    def show_images(self, images, thumbnails):

        self.scene.clear()

        self.selected_node = None

        for i, thumb in enumerate(thumbnails):

            node = PhotoNode(
                images[i],
                thumbnails[i]
            )

            node.clicked.connect(
                self.on_photo_clicked
            )

            x = (i % self.COLUMNS) * self.THUMB_SPACING
            y = (i // self.COLUMNS) * self.THUMB_SPACING

            node.setPos(x, y)

            self.scene.addItem(node)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())

        self.fitInView(
            self.scene.itemsBoundingRect(),
            Qt.KeepAspectRatio
        )

    def on_photo_clicked(self, node):

        if self.selected_node:
            self.selected_node.set_selected(False)

        self.selected_node = node
        self.selected_node.set_selected(True)

        self.photo_selected.emit(
            node.image_path
        )

    def wheelEvent(self, event):

        zoom_in = 1.15
        zoom_out = 1 / zoom_in

        if event.angleDelta().y() > 0:
            factor = zoom_in
        else:
            factor = zoom_out

        self.scale(factor, factor)