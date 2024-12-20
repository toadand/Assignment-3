import random
TEST_CASE = [12, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 57, 66, 100]

"""
recursively split the list into 2 sub-arrays
appending the middle element to a new list each time
"""

def preprocess(arr):
    # arr:          list to be sorted
    # copy_buffer:   temporary space needed during merge
    copy_buffer = [None]*(len(arr))
    # initialise an empty list to be appended to
    initial_list = []
    # sort the list before calling the divide function
    # so the correct list is returned
    sorted_list = sorted(arr)
    processed_list = divide(sorted_list, copy_buffer, 0, len(arr)-1, initial_list)
    # highest value is skipped, so add this back to the list
    processed_list.append(sorted_list[-1])
    return processed_list
    
def divide(arr, copy_buffer, low, high, processed_list):
    # arr           list to be sorted
    # copy_buffer   temporary space needed during merge
    # high, low     bounds of sublist
    # middle        midpoint of sublist
    if low < high:
        middle = (low+high)//2
        processed_list.append(arr[middle])
        divide(arr, copy_buffer, low, middle, processed_list)
        divide(arr, copy_buffer, middle+1, high, processed_list)
    return processed_list


if __name__ == '__main__':
    print('original array A:\n', TEST_CASE)
    print('\nsorted array A:\n', sorted(TEST_CASE))
    preprocessed_list = preprocess(TEST_CASE)
    print('\npre-processed array B:\n', preprocessed_list)

    random_list = random.sample(range(1, 500), 16)
    print('\nrandom list:', random_list)
    print('sorted random list:', sorted(random_list))
    preprocessed_random_list = preprocess(random_list)
    print('pre-processed random list:', preprocessed_random_list)
