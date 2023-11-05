import main

addr_book = main.AddressBook()
file_name = "addr_book.json"

with open(file_name, "r") as file:
    json_string = file.read()
    addr_book = main.AddressBook.from_json(json_string)
