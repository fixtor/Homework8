def Input_data_file(file_name, any_strings, attribute):
    data = open(file_name, attribute, encoding='utf-8')
    data.writelines(any_strings + '\n')
    data.flush()
    data.close()


def Output_data_file_list(file_name):
    data = open(file_name, encoding='utf-8')
    data_list = []
    for line in data:
        a = line.rstrip(line[-1])
        data_list.append((a))
    data.close()
    return data_list


def Output_data_file_string(file_name, encoding='utf-8'):
        data = open(file_name, encoding='utf-8').read()
        return data

