"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months)
of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. 
Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""




expense_list = [2200, 2350, 2600, 2130, 2190]

#1
extra_expense = expense_list[1] - expense_list[0] #O(1)
print(f"the amount spent more is {extra_expense} ")

#2
total = 0
for i in range (0,3):
    total += expense_list[i] #O(n)

print(f"the total of 3 months is {total}")

#3
is_2000 = 2000 in expense_list # O(n)

if(is_2000):
    print("exactly 2000 was spent in particular month")
else:
    print("exactly 2000 wasn't spent in a month")

#4
expense_list.insert(5, 1980) #O(n)
print(expense_list)

#5 
expense_list[3] = expense_list[3] - 200 #O(1)
print(expense_list)

