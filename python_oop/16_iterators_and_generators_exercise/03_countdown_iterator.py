class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration

        counter_value = self.count
        self.count -= 1

        return counter_value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")