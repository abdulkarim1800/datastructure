def myBubbleSort(list):
    for x in range(len(list)-1,0,-1):
        for idx in range(x):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
list = [3,6,1,5,9]
myBubbleSort(list)
print(list)

            