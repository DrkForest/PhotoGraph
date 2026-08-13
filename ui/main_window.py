from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QLabel,
)
from PySide6.QtCore import Qt

from ui.widgets.graph_view import GraphView
from ui.widgets.preview import PreviewWidget
from ui.widgets.toolbar import Toolbar
from ui.dialogs.loading_dialog import LoadingDialog

from core.pipeline import process_folder
from core.image.storage import init_storage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "PhotoGraph"
        )

        self.resize(
            1200,
            800
        )

        self.toolbar = Toolbar()
        self.graph = GraphView()
        self.preview = PreviewWidget()

        self.graph.photo_selected.connect(self.preview.show_image)

        self.info = QLabel("Folder not selected")

        self.info.setMinimumHeight(180)
        self.info.setMinimumWidth(400)
        self.info.setAlignment(Qt.AlignCenter)

        self.toolbar.select_button.clicked.connect(self.select_folder)

        bottom = QHBoxLayout()

        bottom.addWidget(self.info)
        bottom.addWidget(self.preview)

        layout = QVBoxLayout()

        layout.addWidget(self.toolbar)
        layout.addWidget(
            self.graph,
            stretch=1
        )
        layout.addLayout(bottom)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)

        # STORAGE
        init_storage()


    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select photo folder"
        )

        if folder:

            loading = LoadingDialog("Scanning images...")
            loading.show()

            QApplication.processEvents()

            try:
                result = process_folder(folder)

                photos = result["photos"]

                print()
                print("Photos:", len(photos))

                first_photo = photos[0]

                print(
                    first_photo.image
                )

                print(
                    first_photo.embedding.shape
                )

                similar = result["similar"]

                scores = []

                for neighbours in similar.values():

                    for _, score in neighbours:
                        scores.append(score)

                if scores:

                    scores.sort()

                    print()
                    print("Similarity statistics:")
                    print("Count:", len(scores))
                    print("Min:", round(min(scores), 3))
                    print("Max:", round(max(scores), 3))
                    print("Mean:", round(sum(scores) / len(scores), 3))

                    print()
                    print("=== Similarity Graph ===")

                    for image, neighbours in similar.items():

                        print()
                        print(image.name)

                        for neighbour, score in neighbours:

                            print(
                                f"  -> {neighbour.image.name}: "
                                f"{score:.3f}"
                            )

                    # print()
                    # print("Sorted scores:")

                    # for score in scores:
                    #     print(round(score, 3))

                print()

                first = next(iter(similar))

                print(first.name)

                for photo, score in similar[first]:

                    print(
                        photo.image.name,
                        round(score, 3)
                    )


            finally:
                loading.close()


            self.graph.show_graph(
                photos,
                result["graph"],
                result["positions"]
            )


            self.info.setText(
                f"Folder:\n{folder}\n\n"
                f"Images: {len(photos)}"
            )