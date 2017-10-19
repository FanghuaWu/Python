# 3个技巧
# 每一行上写注释用英文解释每行做什么用
# 从后往前阅读你的脚本
# 大声朗读你的脚本，甚至是每个字符

# 建议：用x = 100代替x=100，等号两侧增加空格有助于阅读
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about",average_passengers_per_car, "in each car.")
