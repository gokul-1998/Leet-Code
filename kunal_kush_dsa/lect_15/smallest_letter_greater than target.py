# Find smallest letter Greater than Target

from gettext import lgettext


lis=['a','b','c','f','m','y']

# ceil

def search(lis,target):
    start=0
    end=len(lis)-1
    while start<=end:
        mid=start+(end-start)//2
        print(start,mid,end)
        
        if lis[mid]==target:
            return lis[mid]
        if lis[mid]<target:
            start=mid+1
        else:
            end=mid-1
    print(start,mid,end)
    

    return lis[start%len(lis)]


assert search(lis,'a')=='a'
print()
assert search(lis,'g')=='m'
print()
assert search(lis,'z')=='a'
print("hurray!!!!!")
