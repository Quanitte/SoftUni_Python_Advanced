def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    receipt = '\n'.join([f"{product}: {quantity}" for product, quantity in sorted_products])
    return receipt
