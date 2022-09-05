def write_json (json_string, file_name):
    # needs to be of type <class 'str'
    full_file_name = file_name + ".json"
    
    with open(full_file_name, 'w') as outfile:
        outfile.write(json_string)