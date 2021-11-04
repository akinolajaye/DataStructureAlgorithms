def solution(numbers):
    def mergeSort(numbers):
        if len(numbers)>1:
            mid = len(numbers)//2 +1


            left= numbers[:mid]
            right=numbers[mid:]
            mergeSort(left)
            mergeSort(right)
            
            i=j=k=0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    numbers[k]=left[i]
                    i+=1
                else:
                    numbers[k]=right[j]
                    j+=1
                k+=1

            while i < len(left):
                numbers[k]=left[i]
                i+=1
                j+=1

            while j < len(right):
                numbers[k]=right[j]
                i+=1
                j+=1

        return numbers

    large_odd=[0]
    large_even=[0]

    numbers=mergeSort(numbers)

    print(numbers)
    

    for i in range(len(numbers)-1,0,-1):
        if numbers[i] % 2 ==0 and numbers[i]>large_even[0] and large_even[0]==0:
            large_even[0]=numbers[i]
        elif numbers[i] % 2 !=0 and numbers[i]>large_odd[0] and large_odd[0]==0:
            print(numbers[i])
            large_odd[0]=numbers[i]

        if large_even[0] !=0 and large_odd[0] !=0:
            break




    print(large_odd[0]+large_even[0])



solution([5,3,10,6,11])