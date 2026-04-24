# Task 1
more = [x + 1 for x in [1,2,3,4]]
# x = 1, 2, 3, 4
# more = [2, 3, 4, 5]
print()


def square(n:int) -> int:
    return n * n
    # n = 1, 2, 3, 4  -> 1, 4, 9, 16

squares = [square(x) for x in [1,2,3,4]]
# squares = [1, 4, 9, 16] The list, Squares, is made of the values returned by n * n
print()


def check(n: int) -> bool:
    return n > 2
    # n = 0, 1, 2, 3, 4  -> False, False, False, True, True
answer = [x for x in range(5) if check(x)]
# answer = [3, 4]
print()


def inc(m: int) -> int:
    return m + 1
    # m = 3, 4  -> 4, 5
def check(n: int) -> bool:
    return n > 2
    # n = 0, 1, 2, 3, 4  -> 3, 4
answer = [inc(x) for x in range(5) if check(x)]
# answer = [4, 5]
print()



# Task 2
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
    return total
    # num = 4, total = 4
    # num = 9, total = 13
    # num = 2, total = 15
    # num = 1, total = 16
result = tally([4, 9, 2, 1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list
    # idx = 0, new_list = [4]
    # idx = 1, new_list = [4, 9]
    # idx = 2, new_list = [4, 9, 2]
    # idx = 3, new_list = [4, 9, 2, 1]
    # this loop creates a new list whereas the last function just adds the values
result = copy([4, 9, 2, 1])
print(result)

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
    return new_list
    # value = 4, new_list = [5]
    # value = 9, new_list = [5, 10]
    # value = 2, new_list = [5, 10, 3]
    # value = 1, new_list = [5, 10, 3, 2]
result = increment_all([4, 9, 2, 1])

