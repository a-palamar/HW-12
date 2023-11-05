import main

addr_book = main.AddressBook()
file_name = "addr_book.json"

with open(file_name, "w") as file:
    file.write(addr_book.to_json())
