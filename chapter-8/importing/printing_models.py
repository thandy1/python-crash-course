def make_car(manufacturer, model, **extra_info):
    car = {'manufacturer': manufacturer, 'model': model,}
    car.update(extra_info)
    return car

# print(make_car(
#         'subaru', 'outback',
#         color='blue', tow_package=True))