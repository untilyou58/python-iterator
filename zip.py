names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}.")

# Output:
# Alice is 25 years old and lives in New York.
# Bob is 30 years old and lives in London.
# Charlie is 35 years old and lives in Paris.
