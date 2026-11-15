while True:
    try:
        names = ["John", "Sarah", "Mike", "David"]
        index = int(input("Index: "))
        print(names[index])
    except ValueError:
        pass
        print(f"INVALID not an integer")
    except IndexError:
        pass
        print(f"INVALID not an index in my list")
    else:
        break
    