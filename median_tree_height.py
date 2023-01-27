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
        insert(middle, left_right_heap, insert_value)
        middle = left_right_heap[2]
        result.append(middle)
    print(result)
    return result


def get_higher_middle(li: list) -> int:
    return li[-1]


def max_heap_helper(ne: list, i: int): # the root is at ne[0]
    temp = 2 * i + 1
    if temp >= len(ne):
        return None
    elif temp + 1 >= len(ne):
        if ne[temp] > ne[i]:
            ne[temp], ne[i] = ne[i], ne[temp]
    else:
        max_heap_helper(ne, temp)
        max_heap_helper(ne, temp + 1)
        if (max(ne[temp], ne[temp + 1])) > ne[i]:
            if ne[temp] > ne[temp + 1]:
                ne[i], ne[temp] = ne[temp], ne[i]
            else:
                ne[i], ne[temp + 1] = ne[temp + 1], ne[i]


def min_heap_helper(ne: list, i: int): # the root is at ne[0]

    temp = 2 * i + 1
    if temp >= len(ne):
        return None
    elif temp + 1 >= len(ne):
        if ne[temp] < ne[i]:
            ne[temp], ne[i] = ne[i], ne[temp]
    else:
        min_heap_helper(ne, temp)
        min_heap_helper(ne, temp + 1)
        if (min(ne[temp], ne[temp + 1])) < ne[i]:
            if ne[temp] < ne[temp + 1]:
                ne[i], ne[temp] = ne[temp], ne[i]
            else:
                ne[i], ne[temp + 1] = ne[temp + 1], ne[i]


def initialize(data: str, middle: int) -> list:
    part = data[11:]
    li = part.split(" ")
    less = []
    greater = []
    total = []
    for i in li: # O(n)
        print(int(i))
        num = int(i)
        if num < middle:
            less.append(num)
        elif num > middle:
            greater.append(num)
        else:
            continue
    max_heap_helper(less, 0)
    min_heap_helper(greater, 0)
    total.append(less)
    total.append(greater)
    total.append(middle)

    return total


def insert(median: int, r: list, insert_value: int) -> list:
    left_heap = r[0]

    right_heap = r[1]

    if insert_value < median:
        left_heap.append(insert_value)
        max_heap_helper(left_heap, 0)
    elif insert_value == median:
        right_heap.append(insert_value)
        min_heap_helper(right_heap, 0)
    else:
        right_heap.append(insert_value)
        min_heap_helper(right_heap, 0)

    length = len(list(left_heap)) + len(list(right_heap)) + 1

    if length % 2 != 0 and isinstance(median, int):
        if len(left_heap) > len(right_heap):

            new_mid = round((median + left_heap[0]) / 2, 1)
        else:
            new_mid = round((median + right_heap[0]) / 2, 1)

    else:
        if len(left_heap) > len(right_heap):
            new_mid = left_heap[0]

        else:
            new_mid = right_heap[0]
    if median <= new_mid and isinstance(median, int):
        left_heap.append(median)
    elif isinstance(median, int):
        right_heap.append(median)
    else:
        pass
    median = new_mid
    r[2] = new_mid
    max_heap_helper(left_heap, 0)
    min_heap_helper(right_heap, 0)

    return [left_heap, right_heap, median]


if __name__ == '__main__':
  # some small test cases
  # Case 1

  assert [8.0, 9, 9.5, 9] == median_tree_height(
      ['initialize 11 4 7 18 9 2 7 18 7 20 6 15 4 10',
       'insert 15',
       'insert 19',
       'insert 3',
       ], 8)

