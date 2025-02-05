import operator
from functools import reduce


def insertion_sort(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1

        while j >= 0 and products[j]["rating"] < key["rating"]:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return products

products = [
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics", "rating": 4.5},
    {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics", "rating": 4.0},
    {"id": 3, "name": "T-shirt", "price": 20, "category": "Clothing", "rating": 3.8},
    {"id": 4, "name": "Headphones", "price": 150, "category": "Electronics", "rating": 4.2},
    {"id": 5, "name": "Jeans", "price": 50, "category": "Clothing", "rating": 4.1},
    {"id": 6, "name": "Blender", "price": 100, "category": "Appliances", "rating": 4.0},
    {"id": 7, "name": "Refrigerator", "price": 600, "category": "Appliances", "rating": 4.3},
    {"id": 8, "name": "Coffee Maker", "price": 80, "category": "Appliances", "rating": 3.9},
]

print("after filter and mapping")
filtered = list(filter(lambda record: record["category"] == "Electronics" and record["rating"] > 3.9, products))
print(filtered)

sorted_list = list(map(lambda record: f"{record['name']} (price: ${record['price']})", filtered))
print(sorted_list)

clothing = reduce(lambda acc, record: acc + record["price"] if record["category"] == "Clothing" else acc + 0, products, 0)
print("Summary cost of Clothing products:", clothing)

print(insertion_sort(products))

