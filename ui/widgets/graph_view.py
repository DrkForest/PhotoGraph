from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
)

from ui.graphics.photo_node import PhotoNode


class GraphView(QGraphicsView):

    photo_selected = Signal(Path)

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(400)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.selected_node = None

        self.setAlignment(
            Qt.AlignLeft | Qt.AlignTop
        )

        self.setDragMode(
            QGraphicsView.NoDrag
        )

        self.setTransformationAnchor(
            QGraphicsView.AnchorUnderMouse
        )

        self.setResizeAnchor(
            QGraphicsView.AnchorUnderMouse
        )

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.scene.addText(
            "PhotoGraph Graph Area"
        )

    def clear(self):

        self.scene.clear()

    def show_graph(
        self,
        photos,
        positions,
    ):

        self.scene.clear()

        self.selected_node = None

        SCALE = 1000

        for photo in photos:

            node = PhotoNode(
                photo
            )

            node.clicked.connect(
                self.on_photo_clicked
            )

            x, y = positions[photo.image]

            node.setPos(
                x * SCALE,
                y * SCALE
            )

            self.scene.addItem(node)

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

        self.scale(
            factor,
            factor
        )