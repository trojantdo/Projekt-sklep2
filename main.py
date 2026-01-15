from shop import run_shop

cart = run_shop()

print("\n KOSZYK")
cart.show()

print(f"\nSuma: {cart.total():.2f} zł")
print(f"VAT (23%): {cart.vat():.2f} zł")
print(f"Do zapłaty: {cart.total_with_vat():.2f} zł")

cash = float(input("\nPodaj kwotę: "))
change = cash - cart.total_with_vat()

if change >= 0:
    print(f"Reszta: {change:.2f} zł")
    print("Zakup zakończony ")
else:
    print("Za mało pieniędzy ")
