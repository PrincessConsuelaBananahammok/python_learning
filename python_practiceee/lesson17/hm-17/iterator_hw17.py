
class ReverseIterator:
    def __init__(self, list_num):
        self.list_num = list_num[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_num):
            raise StopIteration

        current_index = self.list_num[self.index]
        self.index += 1

        return current_index


class EvenValueIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.max_num:
            raise StopIteration

        result = self.current
        self.current += 2
        return result

iterator = EvenValueIterator(2)

print(next(iterator))
print(next(iterator))
print(next(iterator))








