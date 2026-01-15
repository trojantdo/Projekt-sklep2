from products import load_products, get_categories, get_products_by_category
from cart import Cart

def run_shop():
    products = load_products()
    cart = Cart()

    while True:
        print("\nKategorie:")
        categories = get_categories(products)
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print("0. Przejdź do koszyka")

        choice = int(input("Wybierz: "))

        if choice == 0:
            break

        selected_category = categories[choice - 1]
        items = get_products_by_category(products, selected_category)

        for p in items:
            print(f"{p['id']}. {p['name']} - {p['price']} zł")

        pid = int(input("Podaj ID produktu (0 aby wrócić): "))
        if pid == 0:
            continue

        for p in products:
            if p["id"] == pid:
                cart.add(p)
                print("Dodano do koszyka")

    return cart


