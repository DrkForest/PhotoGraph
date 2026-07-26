def search_similar(
    index,
    vectors,
    image_list,
    k=6
):

    distances, indices = index.search(
        vectors,
        k
    )

    result = {}

    for i, image in enumerate(image_list):

        neighbours = []

        for idx, score in zip(
            indices[i],
            distances[i]
        ):

            if idx == i:
                continue

            neighbours.append(
                (
                    image_list[idx],
                    float(score)
                )
            )

        result[image] = neighbours

    return result