from numpy import *

class CheckValues:
    def __init__(self, *args):
        self.my_list = self.get_list(args)
        self.currentIndex = 0  # Initialize for iteration

    def __getitem__(self, key=None):
        if key is None:
            return self.my_list
        return self.getitem(key)

    def __setitem__(self, key, value):
        the_keys = self.get_list(key)
        value = self.get_list(value)
        the_min = min(the_keys)
        the_max = max(the_keys)
        if len(the_keys) != len(value):
            raise ValueError(f"the_length of the key ({len(the_keys)}) must be equal to the length of the value ({len(value)})")
        if the_max >= len(self.my_list):
            diff = the_max - (len(self.my_list) - 1)
            self.my_list.extend([0] * diff)
        for ii, idx in enumerate(the_keys):
            self.my_list[idx] = value[ii]

    def __delitem__(self, key):
        the_keys = self.get_list(key)
        self.check_keys(the_keys)
        for key in sorted(the_keys, reverse=True):
            if 0 <= key < len(self.my_list):
                del self.my_list[key]
            else:
                raise IndexError("Index error ...")

    def check_keys(self, the_keys):
        the_min = min(the_keys)
        the_max = max(the_keys)
        if the_min < 0 or the_max < 0:
            raise IndexError(f"the index cannot be negative value; the_min: {the_min}, the_max: {the_max}")
        if isinstance(the_min, (str, float)) or isinstance(the_max, (str, float)):
            raise IndexError(f"the index cannot be the_min: {type(the_min)} and the_max: {type(the_max)} values")
        if the_max >= len(self.my_list):
            raise IndexError(f"the index ({the_max}) cannot be bigger than the list length ({len(self.my_list)})")

    def getitem(self, key):
        the_keys = self.get_list(key)
        self.check_keys(the_keys)
        return [self.my_list[x] for x in the_keys]

    @staticmethod
    def get_list(values):
        my_list = []
        if isinstance(values, (range, slice)):
            the_start = values.start if values.start is not None else 0
            the_stop = values.stop
            the_step = values.step if values.step is not None else 1
            values = range(the_start, the_stop, the_step)
        if isinstance(values, (int, float, str)):
            my_list.append(values)
        elif isinstance(values, (range, slice)):
            for x in values:
                my_list.append(x)
        else:
            for x in values:
                for y in BaseCustomList.get_list(x):
                    my_list.append(y)
        return my_list

    def __iter__(self):
        self.currentIndex = 0 
        return self

    def __next__(self):
        if self.currentIndex >= len(self.my_list):
            raise StopIteration
        result = self.my_list[self.currentIndex]
        self.currentIndex += 1
        return result

    def __repr__(self):
        if isinstance(self.my_list, int):
            return str([self.my_list])
        return str(self.my_list)

class ProcessValues(CheckValues):
    def get_values(self, *args):
        if len(args) == 0 or len(args[0]) == 0:
            return self.my_list
        return self.getitem(args)

    def sum(self, *args):
        res = self.get_values(*args)
        return sum(res)

    def mean(self, *args):
        res = self.get_values(*args)
        return sum(res) / len(res)

    def len(self, *args):
        res = self.get_values(*args)
        return len(res)

    def var(self, *args):
        res = self.get_values(*args)
        mn = mean(res)
        return mean([(x - mn) ** 2 for x in res])

    def std(self, *args):
        res = self.get_values(*args)
        mn = mean(res)
        return sqrt(mean([(x - mn) ** 2 for x in res]))

def test():
    q1 = ProcessValues(100, 90, 80, 70, 10, 20, 30, 40, 50, 0, 1, 2, 3, 4, 5,
                            ([6, [7, [8, range(9, 12)]]]), [12, 13, 14, 15, 16, [(17, 18, 19, 20, 21, range(22, 30))]])
    print(q1.sum([range(0, 10), [([(range(0, 10))])]]))
    print(q1.sum((0, 1, 2, 3, 4, 5, ([6, [7, [8, range(9, 12)]]]), [12, 13, 14, 15, 16, [(17, 18, 19, 20, 21, range(22, 30))]])))
    print(q1.sum())
    print(q1.mean())
    print(q1.std())
    print(q1.var())
    for item in q1:
        print(item)

if __name__ == "__main__":
    test()
