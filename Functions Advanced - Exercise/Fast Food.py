food_quantity = int(input())
orders = list(map(int, input().split()))
biggest_order = 0
orders_left = []
for order in orders:
    if order > biggest_order:
        biggest_order = order

    if order <= food_quantity:
        food_quantity -= order
    else:
        orders_left.append(order)
print(biggest_order)
if not orders_left:
    print("Orders complete")
else:
    print("Orders left:", ' '.join(map(str, orders_left)))
