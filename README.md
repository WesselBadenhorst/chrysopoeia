# chrysopoeia

From Alchemy, meaning to change some base metal into gold.

Python library to consume data from a source, transform and map the data, and finally to produce the data to some other format.

As an example, let's say you want to take all the elements in a list and sent them to some side-effect function.

```python
some_side_effect = []

input_iterable = [1, 2, 3, 4]
square_function = lambda x: x**2
output_method = lambda message: some_side_effect.append(message)

runner(
    input_iterable=input_iterable, 
    transform_function=square_function, 
    post_method=output_method
)
```

The main reason for this code to exist is that there is a pattern that is repeated often where data elements are taken from one source, transformed in some way and then sent to some other destination. By using higher order functions and generators or iterators in python, this pattern can be formalized.

So one might want to consume a Kafka queue and sent transformed events to a data base.