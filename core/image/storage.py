from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

THUMBNAILS_DIR = DATA_DIR / "thumbnails"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"
INDEX_DIR = DATA_DIR / "index"


def init_storage():
    """
    Create PhotoGraph data directories.
    """

    THUMBNAILS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    EMBEDDINGS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    INDEX_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def get_thumbnail_path(image_path):
    """
    Return thumbnail path for image.
    """

    image = Path(image_path)

    return THUMBNAILS_DIR / (
        image.stem + ".webp"
    )