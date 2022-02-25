""" Convert dictionary containing key-value paired full names to a list of full names. """

input_list = [
{"FirstName": "Virat", "LastName": "Kohli"},
{"FirstName": "Rishabh", "LastName": "Pant"},
{"FirstName": "Rohit", "LastName": "Sharma"},
{"FirstName": "Ajinkya", "LastName": None},
{"FirstName": "Shikhar", "LastName": "Dhawan"}
]

def gen_full_names(full_names_dict):
    """ Generate a list of full names from dictionaries. """
    full_names_list = []
    for names in full_names_dict:
        try:
            full_name = names["FirstName"] +" "+ names["LastName"]
            full_names_list.append(full_name)
        except TypeError:
            full_name = names["FirstName"]
            full_names_list.append(full_name)

    return full_names_list

print(gen_full_names(input_list))
