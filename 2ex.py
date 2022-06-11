import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as f:
        json.dump({"contacts": contacts}, f)


def read_contacts_from_file(filename):
    with open(filename, "r") as f:
        user = json.load(f)
        return user.get("contacts")


a = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]


write_contacts_to_file("example.json", a)

print(read_contacts_from_file("example.json"))
