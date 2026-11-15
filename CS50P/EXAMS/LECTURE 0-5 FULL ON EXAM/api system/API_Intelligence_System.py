import json, requests
from system_tools import search_users, filter_users

user_file = "search_results.json"
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
users = response.json()

def load_users():
    with open(user_file, "r") as file:
        return json.load(user_file)
                         
def save_users(users):
    with open(user_file, "w") as file:
        json.dump(users, file, indent=4)

def search_user(users, search_text):
    print("SEARCH BY:\n1. Name\n2. Username\n3. Email")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        search_text = input("Enter name to search: ")
        result = search_users(users, search_text)
    elif choice == "2":
        search_text = input("Enter username to search: ")
        result = search_users(users, search_text)
    elif choice == "3":
        search_text = input("Enter email to search: ")
        result = search_users(users, search_text)
    else:
        print("Invalid choice. Please try again.")
        return []

    if result:
        print(f"Found {len(result)} user(s):")
        for user in result:
            print(f"Name: {user['name']}, Username: {user['username']}, Email: {user['email']}")

def filter_user(users, search_text, city=None, company=None):
    result = filter_users(users, search_text, city, company)
    if result:
        print(f"Found {len(result)} user(s):")
        for user in result:
            print(f"Name: {user['name']}, Username: {user['username']}, Email: {user['email']}, City: {user['address']['city']}, Company: {user['company']['name']}")
    else:
        print("No users found matching the criteria.")

def analyse(users):
    while True:
        print("\nANALYSE USERS:\n1.Number of users\n2.Number of users in different cities\n3.Number of users in different companies\n4.Most represented city\n5.Most represented company\n6.Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            print(f"Total number of users: {len(users)}")
        elif choice == "2":
            cities = {}
            for user in users:
                city = user["address"]["city"]
                cities[city] = cities.get(city, 0) + 1
            print("Number of users in different cities:")
            for city, count in cities.items():
                print(f"{city}: {count}")
        elif choice == "3":
            companies = {}
            for user in users:
                company = user["company"]["name"]
                companies[company] = companies.get(company, 0) + 1
            print("Number of users in different companies:")
            for company, count in companies.items():
                print(f"{company}: {count}")
        elif choice == "4":
            cities = {}
            for user in users:
                city = user["address"]["city"]
                cities[city] = cities.get(city, 0) + 1
            most_represented_city = max(cities, key=cities.get)
            print(f"Most represented city: {most_represented_city} with {cities[most_represented_city]} users")
        elif choice == "5":
            companies = {}
            for user in users:
                company = user["company"]["name"]
                companies[company] = companies.get(company, 0) + 1
            most_represented_company = max(companies, key=companies.get)
            print(f"Most represented company: {most_represented_company} with {companies[most_represented_company]} users")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nMAIN MENU:\n1. Search Users\n2. Filter Users\n3. Analyse Users\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            search_user(users, search_text)
        elif choice == "2":
            search_text = input("Enter search text: ")
            city = input("Enter city filter (or leave blank): ").strip() or None
            company = input("Enter company filter (or leave blank): ").strip() or None
            filter_user(users, search_text, city, company)

        elif choice == "3":
            analyse(users)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
