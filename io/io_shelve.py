import shelve

# dictionary keys in shelve must be a str

with shelve.open("/home/centos/IdeaProjects/mp-basics.py/shelvedb") as shelve_file:
    if "ID1" not in shelve_file.keys():
        shelve_file['ID1'] = ["Identifier 1"]

    shelve_file['ID2'] = ["Identifier 2"]

    for key, value in shelve_file.items():
        print(f"Key: {key}, value: {value}")

    if "ID3" not in shelve_file.keys():
        shelve_file['ID3'] = ["Identifier 3"]

    print(shelve_file.values())
    print(shelve_file.keys())

    tmp_list = shelve_file['ID3']
    tmp_list.append("who will pay for this?")
    shelve_file['ID3'] = tmp_list

with shelve.open("/home/centos/IdeaProjects/mp-basics.py/shelvedb", writeback=True) as shelve_file:
    shelve_file['ID1'].append("I don't know")





