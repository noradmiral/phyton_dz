def show_price(items, show_delim=True):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cent = price % 100
        print(f'{rubles:02d} руб {cent:02d} коп', end=',')
    if show_delim:
        print()


prices = [57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87, 23.45]
show_price(prices)
prices.sort()
show_price(prices)
prices_desc = sorted(prices, reverse=True)
show_price(prices_desc)
show_price(prices_desc[4::-1], False)
