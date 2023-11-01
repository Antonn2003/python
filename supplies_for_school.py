numbers_of_pens = int(input())
numbers_of_markers = int(input())
liters_of_liquid = int(input())
discount_percent = int(input())

pens_price = numbers_of_pens * 5.8
markers_price = numbers_of_markers * 7.2
liquid_price = liters_of_liquid * 1.2

sum = pens_price + markers_price + liquid_price
total_sum = sum - (sum * (discount_percent/100) )
print(total_sum)