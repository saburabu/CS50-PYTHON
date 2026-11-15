lazy import copy

inventory = {
    "electronics": {
        "laptop": 10,
        "phone": 20
    },
    "clothing": {
        "shirts": 50,
        "trousers": 30
    }
}

inventory1 = copy.deepcopy(inventory)

inventory["electronics"]["laptop"] = 5

inventory["electronics"]["mouse"] = 5

inventory1["electronics"]["laptop"] = 5

inventory1["electronics"]["mouse"] = 5

print(inventory)
print(inventory1)