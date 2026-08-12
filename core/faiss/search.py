TOP_K = 5
MIN_SIMILARITY = 0.55


def search_similar(
    index,
    vectors,
    photos,
):
    distances, indices = index.search(
        vectors,
        TOP_K + 1
    )

    nearest = {}

    for i, photo in enumerate(photos):

        neighbours = []

        for idx, score in zip(
            indices[i],
            distances[i]
        ):
            if idx == i:
                continue

            if score < MIN_SIMILARITY:
                continue

            neighbour = photos[idx]

            neighbours.append(
                (
                    neighbour,
                    float(score)
                )
            )

        nearest[photo.image] = neighbours

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