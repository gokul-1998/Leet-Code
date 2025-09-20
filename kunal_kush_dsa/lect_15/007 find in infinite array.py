# find position of an element in a sorted array of infinite numbers

def search(lis,target):
    start=0
    end=len(lis)-1
    while start<=end:
        mid=start+(end-start)//2
        if lis[mid]==target:
            return mid
        if lis[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1


def infinite_array_binary_search(lis,target):
    start=0
    end=1
    while target<end:
        temp=end-start
        start =end+1
        end=


# Example: target exists
print(infinite_array_binary_search(
    [1,2,4,5,8,10,12,15,17,19,22,26,28,30,31,36], 30))  # 13

# Example: target not present and larger than all elements
print(infinite_array_binary_search(
    [1,2,4,5,8,10,12,15,17,19,22,26,28,30,31,36], 100))  # -1
