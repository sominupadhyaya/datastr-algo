stock_prices = [200 , 300 ,300, 340,230 ,320]

stock_prices.remove(300) #O(n) removes 1st 300 
stock_prices.insert(0 , 350)# O(n) inserts at first
""" 
both occur at first iterations but,
since O(n) talks about worst cases
we say it had to go through the whole array making it O(n)
"""
print(stock_prices) 


