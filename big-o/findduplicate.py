#example of O(n^2)
numbers = [3,6,2,3,4,6,3,9,8]


for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] == numbers[j]):
            print(f"{numbers[i]} is duplicate")
