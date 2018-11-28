'''
2.2.2
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

(Page 15). 
'''
cover_price = 24.95
discount = .4  #percentage 
units = int(input("how many units? "))
if units == 1:
	shipping = 3.00
else: 
	shipping = 3 + (.75 * (units - 1))

total_cost = (cover_price - (cover_price * discount)) * units + shipping
print(total_cost)