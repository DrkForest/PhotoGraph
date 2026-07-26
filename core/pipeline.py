from core.image.scanner import scan_folder
from core.image.thumbnail import create_thumbnail


def process_folder(folder):

    images = scan_folder(
        folder
    )

    thumbnails = []

    for image in images:

        thumbnail = create_thumbnail(
            image
        )

        thumbnails.append(
            thumbnail
        )

    return {
        "images": images,
        "thumbnails": thumbnails
    }