# This solution is how I approached the problem:
# - First I iterate through the input list using index i
# - For every element, I iterate through the remaining part of the list and see if there are subsequent elements that would add with element at index i to be k
# - If there is, return True.
def solution1(number_list, k):
    for i in range(len(number_list)):
        for j in number_list[i+1:]:
            if (number_list[i] + j) == k:
                return True

    return False

# This is a solution that comes up when I searched online for additional ideas:
# - The key difference here is to use Python's built-in feature to find k - i in the input list.
def solution2(number_list, k):
    for i in number_list:
        if k - i in number_list:
            return True

    return False

def test_example():
    assert solution1([10, 15, 3, 7], 17) == True
    assert solution2([10, 15, 3, 7], 17) == True


def test_false():
    assert solution1([1, 2, 3, 4], 10) == False
    assert solution2([1, 2, 3, 4], 10) == False


def test_empty_list():
    assert solution1([], 10) == False
    assert solution2([], 10) == False


def test_1_element():
    assert solution1([1], 1) == False
    assert solution2([1], 1) == False


def test_2_element():
    assert solution1([1, 2], 3) == True
    assert solution2([1, 2], 3) == True