#Name: Aarya Vira
#Roll No: 374

nums = [5,4,374,-1]
a = str(input("enter the string i for insertion sort , b for bubble sort , s for selection sort : "))
if a=='i' or a =='I':
   
    def insertion_sort(nums):
        for i in range(1, len(nums)):
            j = i-1
            nxt_element = nums[i]

		
            while (nums[j] > nxt_element) and (j >= 0):
                nums[j+1] = nums[j]
                j=j-1
            nums[j+1] = nxt_element


    insertion_sort(nums)
    print(nums)
elif a == 'b' or a == 'B':
    
    def sort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1] = temp 
    sort(nums)
    print(nums)
elif a == 's' or a =='S':
    def sort(nums):
        for i in range(len(nums)):
            minpos = i
            for j in range(i,len(nums)):
                if nums[j] < nums[minpos]:
                    minpos=j
            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] =temp

    
    sort(nums)
    print(nums)
else:
    print("Enter valid input")
