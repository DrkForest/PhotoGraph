MIN_SIMILARITY = 0.70


def search_similar(
    index,
    vectors,
    photos,
):
    distances, indices = index.search(
        vectors,
        len(photos)
    )

    nearest = {}

    for i, photo in enumerate(photos):

        neighbours = []

        for idx, score in zip(
            indices[i],
            distances[i]
        ):
            # саме фото
            if idx == i:
                continue

            # абсолютний поріг
            if score < MIN_SIMILARITY:
                continue

            neighbours.append(
                (
                    photos[idx],
                    float(score)
                )
            )

        nearest[photo.image] = neighbours

    # Mutual graph:
    # зв'язок існує тільки якщо A бачить B
    # і B бачить A.
    result = {}

    for photo in photos:

        neighbours = nearest.get(
            photo.image,
            []
        )

        mutual = []

        for neighbour, score in neighbours:

            neighbour_neighbours = nearest.get(
                neighbour.image,
                []
            )

            neighbour_images = {
                other.image
                for other, _
                in neighbour_neighbours
            }

            if photo.image in neighbour_images:

                mutual.append(
                    (
                        neighbour,
                        score
                    )
                )

        result[photo.image] = mutual

    return result