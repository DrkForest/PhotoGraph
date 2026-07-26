from pathlib import Path

from core.clip.cache import (
    has_embedding,
    load_embedding,
    save_embedding,
)

from core.clip.embeddings import generate_embedding


def generate_embeddings(
    thumbnails: list[Path]
) -> dict[Path, object]:

    embeddings = {}

    total = len(thumbnails)

    for i, thumb in enumerate(thumbnails, start=1):

        print(
            f"[{i}/{total}] {thumb.name}"
        )

        if has_embedding(thumb):

            embeddings[thumb] = load_embedding(
                thumb
            )

            continue

        embedding = generate_embedding(
            thumb
        )

        save_embedding(
            thumb,
            embedding
        )

        embeddings[thumb] = embedding

    return embeddings