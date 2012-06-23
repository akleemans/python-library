# Code from http://www.codecodex.com/wiki/Merge_sort#Python

def mergesort(arr):  
    if len(arr) == 1:  
        return arr  
      
    m = len(arr) / 2  
    l = mergesort(arr[:m])  
    r = mergesort(arr[m:])  
  
    if not len(l) or not len(r):  
        return l or r  
          
    result = []  
    i = j = 0  
    while (len(result) < len(r)+len(l)):          
        if l[i] < r[j]:  
            result.append(l[i])  
            i += 1  
        else:  
            result.append(r[j])  
            j += 1              
        if i == len(l) or j == len(r):              
            result.extend(l[i:] or r[j:])  
            break  
          
    return result
    
    
# quick sort
def quicksort(a):
    if len(a) <= 1: return a
    pivot = a.pop()
    before = [x for x in a if x <= pivot]
    after = [x for x in a if x > pivot]
    return quicksort(before) + [pivot] + quicksort(after)
