pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input()) #percent

total_cost = pens * 5.80 + markers * 7.20 + cleaner * 1.20
final_price = total_cost * (1 - discount / 100)

print(final_price)