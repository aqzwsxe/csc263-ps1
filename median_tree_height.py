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
        left_right_heap = insert(middle, left_right_heap)
        middle = left_right_heap[2]
        result.append(middle)
    return result


def get_higher_middle(li: list) -> int:
    return li[-1]


def max_heap_helper(ne: list, i: int): # the root is at ne[0]
    temp = 2*(i + 2)
    if i < len(ne):
        if temp < len(ne) and temp + 1 < len(ne): # it has both left and right child
            if max(ne[temp], ne[temp + 1]) > ne[i]:

                if ne[temp] > ne[temp + 1]:
                    ne[i], ne[temp] = ne[temp], ne[i]
                else:
                    ne[i], ne[temp + 1] = ne[temp + 1], ne[i]

        if temp < len(new):
            if ne[temp] > ne[i]:
                ne[temp], ne[i] = ne[i], ne[temp]

    initialize_helper(ne, temp)
    initialize_helper(ne, temp + 1)


def min_heap_helper(ne: list, i: int): # the root is at ne[0]
    temp = 2 * (i + 2)
    if i < len(ne):
        if temp < len(ne) and temp + 1 < len(ne):  # it has both left and right child
            if min(ne[temp], ne[temp + 1]) > ne[i]:

                if ne[temp] < ne[temp + 1]:
                    ne[i], ne[temp] = ne[temp], ne[i]
                else:
                    ne[i], ne[temp + 1] = ne[temp + 1], ne[i]

        if temp < len(new): # only have the left child
            if ne[temp] < ne[i]:
                ne[temp], ne[i] = ne[i], ne[temp]

    initialize_helper(ne, temp)
    initialize_helper(ne, temp + 1)


def initialize(data: str, middle: int) -> list:
    part = data[11:]
    li = part.split(" ")
    less = []
    greater = []
    total = []
    for i in li: # O(n)
        num = int[i]
        if num <= middle:
            less.append(i)
        else:
            greater.append(i)

    max_heap_helper(less, 0)
    min_heap_helper(greater, 0)
    total.append(less)
    total.append(middle)
    total.append(greater)
    return new


def insert(median: int, r: list) -> list:

    left_heap = list[0]
    right_heap = list[2]
    length = len(left_heap) + len(right_heap) + 1

    if length % 2 == 0:
        if len(left_heap) == len(right_heap):
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

