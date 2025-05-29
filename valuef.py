def find_key_value():

    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "email": "alice@example.com"
    }

    key = input("Enter the key you want to look up: ")

    if key in data:
        print(f"The value for '{key}' is: {data[key]}")
    else:
        print(f"Key '{key}' not found in the data.")

find_key_value()
