def sandwich(*items):
    print(f"The following items will be on your sandwich:")
    for item in items:
        print(f"\t{item}")

sandwich("Lettuce", "Cheese")
sandwich("Beef", "Chicken", "Tomato")
sandwich("Ham")