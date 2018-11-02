def runner(
    input_iterable=None,
    transform_function=lambda x: x,
    post_method=None
):
    for item in input_iterable:
        post_method(item)