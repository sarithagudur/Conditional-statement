actual_price=float(input("enter the actual price:"))
selling_price=float(input("enter the selling price:"))

if selling_price>actual_price:
    profit=selling_price-actual_price
    print("the profit is:£",profit)
else:
    loss=actual_price-selling_price
    print("the loss is:£",loss)