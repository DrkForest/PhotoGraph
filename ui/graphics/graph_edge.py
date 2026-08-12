from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsLineItem


class GraphEdge(QGraphicsLineItem):

    NORMAL_WIDTH = 1.0
    HIGHLIGHT_WIDTH = 2.5

    def __init__(self, source, target, weight=0.0):

        super().__init__()

        self.source = source
        self.target = target
        self.weight = weight

        self.setZValue(-1)

        self.set_normal()

        self.update_position()

    def update_position(self):

        source_rect = self.source.boundingRect()
        target_rect = self.target.boundingRect()

        source_center = self.source.pos() + source_rect.center()
        target_center = self.target.pos() + target_rect.center()

        self.setLine(
            source_center.x(),
            source_center.y(),
            target_center.x(),
            target_center.y()
        )

    def set_normal(self):

        pen = QPen(
            QColor("#4a4a4a"),
            self.NORMAL_WIDTH
        )

        pen.setCosmetic(True)

        self.setPen(pen)

    def set_highlighted(self):

        pen = QPen(
            QColor("#7aa2f7"),
            self.HIGHLIGHT_WIDTH
        )

        pen.setCosmetic(True)

        self.setPen(pen)