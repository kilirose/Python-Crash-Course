motorcycles = []
motorcycles.append("suzuki")
motorcycles.append("honda")
motorcycles.append("yamaha")

print(motorcycles)

motorcycles.insert(0, "ducati")

print(motorcycles)

del motorcycles[0]

print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

print(motorcycles)

motorcycles.append("triumph")
motorcycles.append("harley")
motorcycles.append("indian")

print(motorcycles)

boomer_bike = "harley"
motorcycles.remove(boomer_bike)
print(motorcycles)
print(f"\nA {boomer_bike.title()} is too old for me.")