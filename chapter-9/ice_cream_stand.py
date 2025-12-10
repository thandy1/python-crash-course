from number_served import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = list(flavors)
        

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)

# Instance of IceCreamStand
ice_cream = IceCreamStand("Sunset Scoops", "Ice Cream", "Vanilla",
                          "Strawberry", "Chocolate", "Mint")

# Test code
if __name__ == "__main__":
    ice_cream.display_flavors()
