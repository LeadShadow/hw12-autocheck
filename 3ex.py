import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        for i in contacts:
            names = i.keys()
        field_names = csv.DictWriter(f, delimiter=",", fieldnames=names)
        field_names.writeheader()
        for row in contacts:
            field_names.writerow(row)


def read_contacts_from_file(filename):
    lis = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i in reader:
            if i.get("favorite") == "True":
                v = True
            if i.get("favorite") == "False":
                v = False
            clear = i.pop("favorite")
            i.update({"favorite": v})
            lis.append(i)
        return lis


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Sasha Samus",
        "email": "olexandr.samus.2004@gmail.com",
        "phone": "+380937316048",
        "favorite": True,
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

write_contacts_to_file("example.csv", contacts)
print(read_contacts_from_file("example.csv"))
