from chrysopoeia import runner

class TestPipeline(object):
    def test_unit(self):
        some_side_effect = []

        input_iterable = [1, 2, 3, 4]
        identity_function = lambda x: x
        output_method = lambda message: some_side_effect.append(message)

        runner(
            input_iterable=input_iterable,
            post_method=output_method
        )

        assert some_side_effect == [1, 2, 3, 4]

    def test_valid_transform(self):
        some_side_effect = []

        input_iterable = [1, 2, 3, 4]
        identity_function = lambda x: x**2
        output_method = lambda message: some_side_effect.append(message**2)

        runner(
            input_iterable=input_iterable, 
            transform_function=identity_function, 
            post_method=output_method
        )

        assert some_side_effect == [1, 4, 9, 16]