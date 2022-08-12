"""Create a list of all odd numbers between 1 and a
max number. Max number is something
you need to take from a user using input() function

"""


odd_nums = []

max_number = int(input("Enter a max number greater than 2\n"))

print(max_number)


for i in range(max_number):
    if i % 2 != 0:
        odd_nums.append(i)

print(odd_nums)

