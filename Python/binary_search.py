# Python program to perform binary search using iterations
# Learn more about this algorithm here: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

def binary_search(arr, item):
    low = 0
    high = len(arr)-1
  
    while low <= high:
        mid = (low + high)//2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

try:
    item = input("PLEASE INPUT ITEM NUMBER FOR SEARCH IN --> [0,3,5,7,20,99,100] \n: ")
    item = int(item)

    arr = [0,3,5,7,20,99,100]
    position = binary_search(arr, item)
    print(f"Item {item} found at position {position}")
except:
    print("PLEASE ENTER NUMBER ONLY !!")