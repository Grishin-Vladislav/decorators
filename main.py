from tests.logger1 import test_1
from tests.logger2 import test_2
from src.decorator2 import logger


class FlatIterator:

    @logger('iterator.log')
    def __init__(self, list_of_list):
        self.flat_list = []
        self.set_flat(list_of_list)
        self.counter = -1

    @logger('iterator.log')
    def __iter__(self):
        return self

    @logger('iterator.log')
    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.counter]

    def set_flat(self, list_of_lists):
        for pos, element in enumerate(list_of_lists):
            if type(element) is list:
                self.set_flat(list_of_lists[pos])
            else:
                self.flat_list.append(element)


if __name__ == '__main__':
    test_1()
    test_2()

    test_obj = [1, [[[2], 2.3]], '3/3.5', 4, [5, 5.1, 5.2], 6]

    for item in FlatIterator(test_obj):
        pass
