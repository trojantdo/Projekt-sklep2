class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(p["price"] for p in self.items)

    def vat(self):
        return self.total() * 0.23

    def total_with_vat(self):
        return self.total() + self.vat()

    def show(self):
        for p in self.items:
            print(f"{p['name']} - {p['price']} zł")
