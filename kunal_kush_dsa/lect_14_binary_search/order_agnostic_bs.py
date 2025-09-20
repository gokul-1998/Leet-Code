# https://colab.research.google.com/drive/1bub2i3n_mBN_e_eHEgQ6YaqgI9iTlPlX#scrollTo=FFHYjjCM_xPR

desc_list=[12,8,5,2,0,-4,-8]
asc_list=[-8,-4,0,2,5,8,12]

def order_agnostic_binary_search(lis,target):
    is_asc=lis[0]<lis[-1]

    start=0
    end=len(lis)-1
    while start<=end: # remember it is less than or equal to
        mid=start+(end-start)//2
        if lis[mid]==target:
            return mid
        elif is_asc:
            if lis[mid]<target:
                start=mid+1
            else:
                end=mid-1
        else:
            if lis[mid]<target:
                end=mid-1
            else:
                start=mid+1
    return -1
            



assert order_agnostic_binary_search(desc_list,5)==2
assert order_agnostic_binary_search(asc_list,5)==4
assert order_agnostic_binary_search(asc_list,100)==-1
assert order_agnostic_binary_search(desc_list,100)==-1
print("done")
