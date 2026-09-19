def display_name_score(names, scores):
    """Print the name and score pair combining by index"""
    for index in range(len(names)):
        print(names[index], scores[index])


# Preferred way than manually getting with iterating index
def display_name_scores(names, scores):
    """Print the name and score pair combining by zip"""
    for name, score in zip(names, scores):
        print(name, score)


def create_name_score(names, scores):
    """ Create and return a dictionary with name score mapping"""
    return dict(zip(names, scores))


names = ["saranya", "Deepa", "Kavya"]
scores = [23, 64, 89, 65, 0]
display_name_score(names, scores)
display_name_scores(names, scores)
print(create_name_score(names, scores))


def combine_product_price_stock(products, prices, stocks):
    """ Create and return a tuple by mapping product, price and stock"""
    return tuple(zip(products, prices, stocks))


products = ["computer", "Mouse", "Keyboard", "Pendrive"]
prices = [12000, 45, 234, 10]
stocks = [12, 5, 0]
# When zipped lists has different length then the minimun length taken as threshold
print(combine_product_price_stock(products, prices, stocks))


def tuple_unpacking(products_info):
    """Print unpacked tuple of zipped data"""
    for product, price, stock in products_info:
        print(f"Product: {product}, Price: {price}, Stock: {stock}")


tuple_unpacking(combine_product_price_stock(products, prices, stocks))


def swap_number(num_one, num_two):
    """Return swapped numbers without temporary variable"""
    return num_two, num_one


numone, numtwo = 4, 8
swapped_numone, swapped_numtwo = swap_number(numone, numtwo)
print(
    f"Original Number: {numone},{numtwo}: Swapped numbers:{swapped_numone},{swapped_numtwo}")
