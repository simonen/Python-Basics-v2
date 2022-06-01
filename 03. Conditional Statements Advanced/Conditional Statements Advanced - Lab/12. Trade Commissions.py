city = input()
sales = float(input())
commission = 0 #percent
is_city_valid = True
is_sales_valid = True

if sales < 0:
    is_sales_valid = False
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5
else:
    is_city_valid = False

profit = sales * commission / 100

if is_city_valid and is_sales_valid:
    print(f"{profit:.2f}")
else:
    print("error")