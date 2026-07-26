from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
}


def scan_folder(folder_path):

    folder = Path(folder_path)

    images = []

    for file in folder.rglob("*"):

        if file.is_file():

            if file.suffix.lower() in SUPPORTED_EXTENSIONS:
                images.append(file)

    return sorted(images)