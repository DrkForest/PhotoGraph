from pathlib import Path
import hashlib

import numpy as np


EMBEDDING_DIR = Path("data/embeddings")


def embedding_path(image: Path) -> Path:

    text = f"{image.resolve()}:{image.stat().st_mtime}"

    key = hashlib.sha256(
        text.encode()
    ).hexdigest()

    return EMBEDDING_DIR / f"{key}.npy"


def has_embedding(image: Path) -> bool:

    return embedding_path(image).exists()


def load_embedding(image: Path):

    return np.load(
        embedding_path(image)
    )


def save_embedding(image: Path, embedding):

    np.save(
        embedding_path(image),
        embedding
    )