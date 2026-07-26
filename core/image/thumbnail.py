from PIL import Image

from core.image.storage import (
    get_thumbnail_path
)


THUMB_SIZE = 256


def create_thumbnail(image_path):

    output_path = get_thumbnail_path(
        image_path
    )

    if output_path.exists():
        return output_path


    image = Image.open(
        image_path
    )

    image.thumbnail(
        (
            THUMB_SIZE,
            THUMB_SIZE
        )
    )


    image.save(
        output_path,
        "WEBP",
        quality=85
    )

    return output_path