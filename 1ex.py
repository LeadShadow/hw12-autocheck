import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as f:
        pickle.dump(contacts, f)


def read_contacts_from_file(filename):
    with open(filename, "rb") as f:
        unpacked = pickle.load(f)
        return unpacked
