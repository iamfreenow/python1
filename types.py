def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100

    return price_with_discount


product = {'name': 'iPhone X', 'stock': 5, 'price': 1000.5, 'discount': 70}

product['with_discount'] = discounted(product['price'], product['discount'], max_discount=80)

print(product)

