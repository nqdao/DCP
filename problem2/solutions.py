# Find product of all the elements, then divide the product by element i when creating new list
# The edge case where there are 0s in the list makes this solution a bit more complicated.
# - if there is one 0, then the product list contains 0s everywhere except where i = 0.
# - if there are more than one 0s, then product list contains only 0s.
def solution1(numlist):
    product = 1
    for i in numlist:
        if i != 0:
            product = product * i

    zero_count = numlist.count(0)
    if (zero_count > 1):
        return [0] * len(numlist)        
    if (zero_count == 1):
        return [product if i == 0 else 0 for i in numlist]
    else:
        return [product / i for i in numlist]

# Without using division
# This is a much more general solution that addresses when list contains 0 as well.
def solution2(numlist):
    product_list = []
    for i in numlist:
        templist = list(numlist)
        templist.remove(i)
        product = 1
        for j in templist:
            product = product * j
        product_list.append(product)

    return product_list

def test_example1():
    test_input = [1, 2, 3, 4, 5]
    test_output = [120, 60, 40, 30, 24]
    assert solution1(test_input) == test_output
    assert solution2(test_input) == test_output


def test_example2():
    test_input = [3, 2, 1]
    test_output = [2, 3, 6]
    assert solution1(test_input) == test_output
    assert solution2(test_input) == test_output

def test_empty():
    assert solution1([]) == []
    assert solution2([]) == []

def test_1_zero_element():
    test_input = [1, 0, 2]
    test_output = [0, 2, 0]
    assert solution1(test_input) == test_output
    assert solution2(test_input) == test_output

def test_2_zero_elements():
    test_input = [1, 0, 2, 0]
    test_output = [0, 0, 0, 0]
    assert solution1(test_input) == test_output
    assert solution2(test_input) == test_output