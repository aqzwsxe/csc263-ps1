'''
CSC263 Winter 2023
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements


# left = 2i   right = 2i+1    parent = floor(i/2)


def median_tree_height(commands, middle) -> list:
    '''
    Pre: commands is a list of commands, middle is the middle or lower middle value of the current collection.
    Post: return list of outputs
    '''
    left_right_heap = initialize(commands[0], middle)
    result = [middle]
    for i in commands[1:]:
        insert_value = int(i[7:])
        l_r_heap = insert(middle, left_right_heap, insert_value)
        middle = l_r_heap[2]
        result.append(middle)
    print(result)
    return result


def get_higher_middle(li: list) -> int:
    return li[-1]


def max_heap_helper(ne: list, i: int): # the root is at ne[0]
    temp = 2*(i + 1)
    for i in range(len(ne)):
        if i < len(ne):
            if temp < len(ne) and temp + 1 < len(ne): # it has both left and right child
                print(ne[0])
                if max(ne[temp], ne[temp + 1]) > ne[i]:

                    if ne[temp] > ne[temp + 1]:
                        ne[i], ne[temp] = ne[temp], ne[i]
                    else:
                        ne[i], ne[temp + 1] = ne[temp + 1], ne[i]

            if temp < len(ne):
                if ne[temp] > ne[i]:
                    ne[temp], ne[i] = ne[i], ne[temp]


def min_heap_helper(ne: list, i: int): # the root is at ne[0]
    temp = 2 * (i + 1)
    for i in range(len(ne)):
        if i < len(ne):
            if temp < len(ne) and temp + 1 < len(ne):  # it has both left and right child
                if min(ne[temp], ne[temp + 1]) > ne[i]:

                    if ne[temp] < ne[temp + 1]:
                        ne[i], ne[temp] = ne[temp], ne[i]
                    else:
                        ne[i], ne[temp + 1] = ne[temp + 1], ne[i]

            if temp < len(ne): # only have the left child
                if ne[temp] < ne[i]:
                    ne[temp], ne[i] = ne[i], ne[temp]


def initialize(data: str, middle: int) -> list:
    part = data[11:]
    li = part.split(" ")
    less = []
    greater = []
    total = []
    for i in li: # O(n)

        num = int(i)
        if num < middle:
            less.append(num)
        else:
            greater.append(num)

    max_heap_helper(less, 0)
    min_heap_helper(greater, 0)
    total.append(less)
    total.append(greater)
    total.append(middle)

    return total


def insert(median: int, r: list, insert_value: int) -> list:

    left_heap = r[0]

    right_heap = r[1]

    length = len(list(left_heap)) + len(list(right_heap)) + 1

    if length % 2 == 0:
        if len(left_heap) == len(right_heap):
            print(left_heap[0] / 2)

            new_mid = round((median + left_heap[0])/2)
        else:
            new_mid = round((median + right_heap[0])/2)

    else:
        if len(left_heap) > len(right_heap):
            new_mid = round((median + left_heap[0])/2)
        else:
            new_mid = round((median + right_heap[0]) / 2)
    if median <= new_mid:
        left_heap.append(median)
    else:
        right_heap.append(median)

    max_heap_helper(left_heap, 0)
    min_heap_helper(right_heap, 0)

    return [left_heap, right_heap, new_mid]


if __name__ == '__main__':
  # some small test cases
  # Case 1

  assert [9, 10.0, 11, 10.0] == median_tree_height(
    ['initialize 11 4 7 18 9',
     'insert 15',
     'insert 19',
     'insert 3',
     ], 9)


