from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
)

from ui.graphics.photo_node import PhotoNode
from ui.graphics.graph_edge import GraphEdge


class GraphView(QGraphicsView):

    photo_selected = Signal(Path)

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(400)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.selected_node = None

        self.nodes = {}
        self.edges = []

        self.setAlignment(
            Qt.AlignCenter
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

        self.scene.setBackgroundBrush(
            QBrush(
                QColor("#1e1e1e")
            )
        )

    def clear(self):

        self.scene.clear()

        self.selected_node = None
        self.zoom_level = 1.0

        self.nodes.clear()
        self.edges.clear()

    def show_graph(
        self,
        photos,
        graph,
        positions,
    ):

        SCALE = 1000

        self.clear()

        # -------------------------------------------------
        # NODES
        # -------------------------------------------------

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

            self.nodes[
                photo.image
            ] = node

            self.scene.addItem(
                node
            )

        # -------------------------------------------------
        # EDGES
        # -------------------------------------------------

        for source, target, data in graph.edges(
            data=True
        ):

            source_node = self.nodes.get(
                source
            )

            target_node = self.nodes.get(
                target
            )

            if source_node is None:
                continue

            if target_node is None:
                continue

            edge = GraphEdge(
                source_node,
                target_node,
                data.get(
                    "weight",
                    0.0
                )
            )

            self.scene.addItem(
                edge
            )

            self.edges.append(
                edge
            )

        # -------------------------------------------------
        # SCENE
        # -------------------------------------------------

        rect = self.scene.itemsBoundingRect()

        rect.adjust(
            -100,
            -100,
            100,
            100
        )

        self.scene.setSceneRect(
            rect
        )

        if not rect.isEmpty():

            self.fitInView(
                rect,
                Qt.KeepAspectRatio
            )

    def on_photo_clicked(
        self,
        node
    ):


        if self.selected_node:

            self.selected_node.set_selected(
                False
            )


        self.selected_node = node

        self.selected_node.set_selected(
            True
        )


        self.update_highlights()


        self.photo_selected.emit(
            node.image_path
        )

    def update_highlights(self):

        if self.selected_node is None:

            for edge in self.edges:

                edge.set_normal()

            return

        selected_image = (
            self.selected_node.image_path
        )

        neighbor_images = set()

        for edge in self.edges:

            source_image = (
                edge.source.image_path
            )

            target_image = (
                edge.target.image_path
            )

            if source_image == selected_image:

                neighbor_images.add(
                    target_image
                )

            elif target_image == selected_image:

                neighbor_images.add(
                    source_image
                )

        # -------------------------------------------------
        # EDGES
        # -------------------------------------------------

        for edge in self.edges:

            source_image = (
                edge.source.image_path
            )

            target_image = (
                edge.target.image_path
            )

            if (
                source_image == selected_image
                or
                target_image == selected_image
            ):

                edge.set_highlighted()

            else:

                edge.set_normal()

        # -------------------------------------------------
        # NODES
        # -------------------------------------------------

        for image, node in self.nodes.items():

            if image == selected_image:

                node.set_selected(
                    True
                )

            elif image in neighbor_images:

                node.set_neighbor_highlighted(
                    True
                )

            else:

                node.set_neighbor_highlighted(
                    False
                )

    def wheelEvent(
        self,
        event
    ):

        zoom_in = 1.15
        zoom_out = 1 / zoom_in

        if event.angleDelta().y() > 0:

            factor = zoom_in

        else:

            factor = zoom_out

        self.zoom_level *= factor

        self.zoom_level = max(
            0.15,
            min(
                self.zoom_level,
                5.0
            )
        )

        self.scale(
            factor,
            factor
        )

        self.update_lod()

    def update_lod(self):

        if self.zoom_level < 0.4:

            size = PhotoNode.MIN_SIZE

        elif self.zoom_level < 1.2:

            size = PhotoNode.NORMAL_SIZE

        else:

            size = PhotoNode.MAX_SIZE

        for node in self.nodes.values():

            node.set_size(
                size
            )

        for edge in self.edges:

            edge.update_position()