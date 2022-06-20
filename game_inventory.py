import csv


# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    try: 
        file = open(inventory)
        csv_reader = csv.reader(file)
        csv_line = []
        csv_line = next(csv_reader)
    except Exception as error:
        return error
    else:
        inventory_dict = dict()
        for i in csv_line:
            inventory_dict[i] = inventory_dict.get(i, 0) + 1
        return inventory_dict


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    new_inventory = display_inventory(inventory)
    keys = new_inventory.keys()
    for item in added_items:
        if item in keys:
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1
    print(sorted(new_inventory))
    return sorted(new_inventory)


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    new_inv = display_inventory(inventory)
    for i in removed_items:
        if new_inv[i] == 1:
            new_inv.pop(i)
        else:
            new_inv[i] -= 1
    print(sorted(new_inv))
    return sorted(new_inv)


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    for key, value in inventory.items():
        key, name = value
        print("{:<10} {:<10} ".format(key, name))
    dict_list = list(inventory.items())
    if order == "asc":
        dict_list.sort()
        return dict_list
    elif order == "desc":
        dict_list.sort(reverse=True)
    return dict_list



def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    filename = open(inventory)
    csvreader = csv.reader(filename)
    csv_line = []
    csv_line = next(csvreader)
    inventory_dict = dict()
    for i in csv_line:
        inventory_dict[i] = inventory_dict.get(i, 0) + 1
    return inventory_dict


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""
    try:
        with open(filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile)
            writer.writeheader()
            for data in inventory:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def start():
    inventory = 'test_inventory.csv'
    # print(display_inventory(inventory))
    # added_items = ["spade"]
    # inventory = {'dagger': 3, 'gold coin': 1, 'battleaxe': 1}
    add_to_inventory(inventory, ["spade"])
    # remove_from_inventory(inventory, removed_items=["dagger"])


if __name__ == "__main__":
    start()
