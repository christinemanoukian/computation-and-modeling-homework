alphabet = " abcdefghijklmnopqrstuvwxyz"


def encode(string, a, b):
    result = []
    for char in string:
        result.append(a * alphabet.index(char) + b)
    return result


def decode_numbers(numbers, a, b):
    result = ""
    for num in numbers:
        decoded_num = (num - b) / a
        if decoded_num not in range(0, 27):
            return False
        else:
            result += alphabet[int(decoded_num)]
    return result


message = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]
for a in range(1, 101):
    for b in range(0, 101):
        if decode_numbers(message, a, b) is not False:
            print(decode_numbers(message, a, b))


# I kinda combined parts a and b
def calc_square_root(bounds, x, precision):
    while bounds[1] - bounds[0] > precision:
        middle = ((bounds[0]+bounds[1])/2)
        if middle ** 2 > x:
            bounds[1] = middle
        elif middle ** 2 < x:
            bounds[0] = middle
        else:
            return middle
    return middle
print(calc_square_root([1, 2], 2, .00001))


# part c and d below
def calc_square_root_2(x, precision):
    bounds = [0, x]
    while bounds[1] - bounds[0] > precision:
        middle = ((bounds[0]+bounds[1])/2)
        if middle ** 2 > x:
            bounds[1] = middle
        elif middle ** 2 < x:
            bounds[0] = middle
        else:
            return middle
    return middle


def calc_nth_root(x, n, precision):
    bounds = [0, x]
    while bounds[1] - bounds[0] > precision:
        middle = ((bounds[0]+bounds[1])/2)
        if middle ** n > x:
            bounds[1] = middle
        elif middle ** n < x:
            bounds[0] = middle
        else:
            return middle
    return middle


class Stack:
    def __init__(self):
        self.elements = []

    def print(self):  
        print(list(reversed((self.elements))))

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.pop()


class Queue:
    def __init__(self):
        self.elements = []

    def print(self):
        print(self.elements)

    def enqueue(self, x):
        self.elements.append(x)

    def dequeue(self):
        top_item = self.elements[0]
        print(top_item)
        self.elements.remove(top_item)
        return self.elements


def calc_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if min_num >= num:
            min_num = num
        else:
            min_num = min_num
    return min_num


def simple_sort(numbers):
    result = []
    count = len(numbers) - 1
    while count <= len(numbers) - 1:
        minimum = calc_minimum(numbers)
        if count == 0:
            break
        else:
            result.append(minimum)
            numbers.remove(minimum)
        count -= 1
    result.append(numbers[0])
    return result
