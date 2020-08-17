def binary_search(array, target, start, end):
    
    while start<=end:
        mid = (start+end)//2
        sum = 0
        for i in array:
            if i >mid:
                sum+= (i-mid)
        if sum == target:
            return mid
        elif sum<target:
            end = mid-1
        else:
            start=mid+1
    return None


n, m = map(int,input().split())

array = list(map(int,input().split()))
array.sort(reverse=True)

print(binary_search(array,m,0,array[0]))
