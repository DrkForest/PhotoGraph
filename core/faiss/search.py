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

    result = {}


    for i, photo in enumerate(photos):

        neighbours = []


        for idx, score in zip(
            indices[i],
            distances[i]
        ):

            # пропускаємо саме себе
            if idx == i:
                continue


            # слабка схожість
            if score < MIN_SIMILARITY:
                continue


            neighbours.append(
                (
                    photos[idx],
                    float(score)
                )
            )


        result[photo.image] = neighbours


    return result