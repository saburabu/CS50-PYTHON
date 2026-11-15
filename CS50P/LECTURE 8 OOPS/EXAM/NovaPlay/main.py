from models.user import User
from services.store import Store
from services.storage import Storage


def build_store():
    storage = Storage("data")
    store = Store(storage)

    store.add_game("g1", "Sky Racers", 12000, "Racing")
    store.add_game("g2", "Dungeon Quest", 8500, "Adventure")
    store.add_game("g3", "Pixel Farm", 5000, "Simulation")

    return store


def main():
    store = build_store()
    users = []

    while True:
        print("\n=== NOVAPLAY ===")
        print("1. Register")
        print("2. List users")
        print("3. View games")
        print("4. Add wallet funds")
        print("5. Buy a game")
        print("6. View game library")
        print("7. View purchase history")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Username: ").strip()
            user = User(name)
            users.append(user)
            store.save_user(user)
            print(f"Welcome, {name}!")

        elif choice == "2":
            for user in users:
                print(user)

        elif choice == "3":
            for game in store.games:
                print(game)

        elif choice == "4":
            name = input("Username: ").strip()
            amount = float(input("Amount to add: "))
            user = store.find_user(name)
            if user:
                user.wallet.add_funds(amount)
                store.save_user(user)
                print("Funds added.")
            else:
                print("User not found.")

        elif choice == "5":
            name = input("Username: ").strip()
            game_id = input("Game ID: ").strip()
            user = store.find_user(name)
            game = store.find_game(game_id)

            if user and game:
                if store.purchase(user, game):
                    print("Purchase successful.")
                else:
                    print("Purchase could not be completed.")
            else:
                print("User or game not found.")

        elif choice == "6":
            name = input("Username: ").strip()
            user = store.find_user(name)
            if user:
                for game in user.library.games:
                    print(game)
            else:
                print("User not found.")

        elif choice == "7":
            name = input("Username: ").strip()
            user = store.find_user(name)
            if user:
                for purchase in user.purchase_history:
                    print(purchase)
            else:
                print("User not found.")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
