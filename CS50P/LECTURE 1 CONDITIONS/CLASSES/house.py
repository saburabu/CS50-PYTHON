# match
name = input("What's your name? ")

if name == "Harry":
      print("Gryffindor")
elif name == "Hermione":
      print("Gryffindor")
elif name == "Ron": 
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

# we can also resolve the problem like this

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

# we can make use of the match statements

name = input("What's your name? ")

match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

# we can still tighten-up the code like this

name = input("What's your name? ")

match name: 
      case "Harry"| "Hermione"| "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")