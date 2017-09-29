def bubble_sort(list):
    ######################list를 입력받아 bubblesort 해주는 함수##################
    for i in range(len(list)-1, 1, -1): # Index of step
        for j in range(0, i): # Index of stage, in each step
            if list[j] > list[j+1]: # If previous value is higher than next value, swap them
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    ##############################################################################

list = [3,1,10,6,8,9,5,5,4,2]
print("List Before Sort")
print(list)

bubble_sort(list)
print("List After Sort")
print(list)
