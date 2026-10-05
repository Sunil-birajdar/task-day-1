cost_price=int(input("enter the price:"))
selling_amount=int(input("enter the sell amount:"))
if cost_price > selling_amount:
    loss= cost_price-selling_amount
    print("loss:",loss)
elif cost_price < selling_amount:
    profit=selling_amount-cost_price
    print("profit:",profit)
else:
    print("no profit ,no loss")