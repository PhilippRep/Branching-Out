import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_age(ages):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(ages)]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name,age): ").strip().lower()

    if filter_option == "name":
        to_search_name = input("Enter a name to filter users: ").strip()
        filter_users_by_name(to_search_name)
    elif filter_option == "age":
        to_search_age = input("Enter a age to filter users: ").strip()
        filter_users_age(to_search_age)
    else:
        print("Filtering by that option is not yet supported.")
