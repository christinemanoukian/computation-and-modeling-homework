2# Tally Sort:
# numbers = [3,3,1,0,3,1,-2]
# 1. Subtract the min (which is -2)
# shifted_numbers = [5,5,3,2,5,3,0]
# 2. Initialize the tallies. max(shifted_numbers) = 5, so initialize tallies with zeros at indices 0,1,2,3,4,5 (6 total)
# tallies = [0,0,0,0,0,0]
# 3. For each number in shifted_numbers, increment tallies[number]
# number = 5; tallies = [0,0,0,0,0,1]
# number = 5; tallies = [0,0,0,0,0,2]
# number = 3; tallies = [0,0,0,1,0,2]
# number = 2: tallies = [0,0,1,1,0,2]
# number = 5; tallies = [0,0,1,1,0,3]
# number = 3; tallies = [0,0,1,2,0,3]
# number = 0; tallies = [1,0,1,2,0,3]
# There is 1 instance of 0, 0 instances of 1, 1 instance of 2, 2 instances of 3, 0 instances of 4, 3 instances of 5 --> [0,2,3,3,5,5,5]
# add the minimum back --> [-2,0,1,1,3,3,3] = SORTED LIST


def tally_sort(numbers):
    shifted_numbers = []
    tallies = []
    original_minimum = min(numbers)
    for number in numbers:
        new_number = number - original_minimum
        shifted_numbers.append(new_number)
    shifted_maximum = max(shifted_numbers)
    count = shifted_maximum
    while count <= shifted_maximum:
        if count < 0:
            break
        else:
            tallies.append(0)
        count -= 1
    for num in shifted_numbers:
        tallies[num] += 1
    new_list = []
    for i in range(len(tallies)):
        for n in range(tallies[i]):
            new_list.append(i+original_minimum)
    return new_list


# Card Sort:
# numbers: [3,3,1,0,3,1,-2]
# go through each entry of the list, and move it as far left as we need
# [3,3,1,0,3,1,-2] --> [3,3,1,0,3,1,-2] --> [3,3,1,0,3,1,-2] --> [1,3,3,0,3,1,-2] -> [0,1,3,3,3,1,-2] --> [0,1,3,3,3,1,-2] --> [0,1,1,3,3,3,-2] --> [-2,0,1,1,3,3,3]
# each time, you're moving the number left until it's less than or equal to the number directly ahead of it

def insert_num(num, sorted_list):
    for i in range(len(sorted_list)):
        if sorted_list[i] > num:
            sorted_list.insert(i, num)
            return sorted_list
    sorted_list.append(num)
    return sorted_list


def card_sort(numbers):
    sorted_list = [numbers[0]]
    for i in range(1, len(numbers)):
        sorted_list = insert_num(numbers[i], sorted_list)
    return sorted_list


# Swap Sort:
# numbers: [3,3,1,0,3,1,-2]
# [3,3,1,0,3,1,-2] --> [3,1,3,0,3,1,-2] --> [1,3,3,0,3,1,-2] --> [1,3,0,3,3,1,-2] --> [1,0,3,3,3,1,-2] --> [0,1,3,3,3,1,-2] --> [0,1,3,3,1,3,-2] --> [0,1,3,1,3,3,-2] --> [0,1,1,3,3,3,-2] --> [0,1,1,3,3,-2,3] --> [0,1,1,3,-2,3,3] --> [0,1,1,-2,3,3,3] --> [0,1,-2,1,3,3,3] --> [0,-2,1,1,3,3,3] --> [-2,0,1,1,3,3,3]
# just swap consecutive numbers until they are in the right place

def swap_sort(numbers):
    for i in range(len(numbers)):
        for num in range(len(numbers) - 1):
            if numbers[num] > numbers[num+1]:
                numbers[num], numbers[num+1] = numbers[num+1], numbers[num]
    return numbers
