from number_served import Restaurant

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0  # Attribute with default value of 0

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} offers {self.cuisine_type}.")
        
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open.")

#     def set_number_served(self, customers):
#         self.number_served = customers

#     def increment_number_served(self, customers):
#         self.number_served += customers

# restaurant = Restaurant("Sunset Grill", "American Cuisine")

# restaurant.number_served = 10   # Manual change
# print(restaurant.number_served)

# restaurant.set_number_served(23)    # Use setter
# print(restaurant.number_served)

# restaurant.increment_number_served(10)  # Add 10 more served
# print(restaurant.number_served)

# Finish program
class IceScreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        # super().__init__()
        pass
