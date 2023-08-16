mountain_in_jpan = {"fuji": 3776, "Kitadake": 3193, "okuhodakadake": 3190, "dummy": 0}
mountain_in_jpan_sorted = sorted(
    mountain_in_jpan.items(), key=lambda x: x[1], reverse=True
)
print(mountain_in_jpan_sorted)
