from core.clip.cache import (
    has_embedding,
    load_embedding,
    save_embedding,
)

from core.clip.embeddings import generate_embedding

from core.models.photo import Photo


def generate_embeddings(
    photos: list[Photo]
) -> list[Photo]:

    total = len(photos)

    for i, photo in enumerate(photos, start=1):

        print(
            f"[{i}/{total}] {photo.image.name}"
        )

        if has_embedding(photo.thumbnail):

            photo.embedding = load_embedding(
                photo.thumbnail
            )

            continue


        embedding = generate_embedding(
            photo.thumbnail
        )


        save_embedding(
            photo.thumbnail,
            embedding
        )


        photo.embedding = embedding


    return photos