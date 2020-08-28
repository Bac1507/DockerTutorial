cars = 100
drivers = 30
passengers = 150
cars_driver = drivers #moi xe mot lai xe
cars_not_driver = cars - drivers
passengers_per_car = passengers / cars_driver

print ("There are ", cars , "cars available today")
print ("There are only ", drivers , "drivers is working")
print ("There will be ", cars_not_driver , "cars is empty")
print ("We have ", passengers, "passengers today")
print ("We need to put about ", passengers_per_car, "in each car.")
