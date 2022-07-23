import time
  
# store starting time
begin = time.time()

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
            squared_numbers.append(n*n)
    return squared_numbers

time.sleep(1)
# store end time
end = time.time()

numbers  = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,27,26,26,26,546,56,45,45,34,5,634,56,345,56]
squared_numbers = get_squared_numbers(numbers)
print(squared_numbers)

print(f"Total runtime of the program is {end - begin}")