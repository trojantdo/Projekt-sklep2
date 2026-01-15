import json

def load_products():
    with open("data/products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_categories(products):
    return sorted(set(p["category"] for p in products))

def get_products_by_category(products, category):
    return [p for p in products if p["category"] == category]

