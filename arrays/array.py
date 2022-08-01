stock_prices = [200 , 300 , 340,230 ,320]

print(f"The price on day1 ={ stock_prices[0]}")

# to search the day  for price of 300

for i in range(len(stock_prices)):
    if(stock_prices[i] == 300):
         day = i+1



print(f"The day was : {day}")
