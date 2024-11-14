def total_revenue(data: list) -> int:
    result = 0
    for purchase in data:
        result += purchase["price"] * purchase["quantity"]
    return result


def items_by_category(data: list) -> dict:
    result = dict()
    for purchase in data:
        if purchase["category"] not in result:
            result[purchase["category"]] = list()
        result[purchase["category"]].append(purchase["item"])
    return result


def expensive_purchases(data: list, min_price: float) -> list:
    result = list()
    for purchase in data:
        if purchase["price"] > min_price:
            result.append(purchase)
    return result


def average_price_bu_category(data: list) -> float:
    average = dict()
    for purchase in data:
        if purchase["category"] not in average:
            average[purchase["category"]] = 0
        average[purchase["category"]] += purchase["price"]
    for category in average:
        average[category] = average[category] / len(items_by_category(data)[category])
    return average


def most_frequent_category(data: list) -> str:
    res = dict()
    max_q = 0
    ans = ""
    for purchase in data:
        if purchase["category"] not in res:
            res[purchase["category"]] = 0
        res[purchase["category"]] += purchase["quantity"]
        if res[purchase["category"]] > max_q:
            max_q = res[purchase["category"]]
            ans = purchase["category"]
    return ans


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
print("Общая выручка:", total_revenue(purchases))
print("Товары по категориям:", items_by_category(purchases))
print("Покупки дороже 1.0:", expensive_purchases(purchases, 1.0))
print("Средняя цена по категориям", average_price_bu_category(purchases))
print("Категория с наибольшим количеством проданных товаров:", most_frequent_category(purchases))
