import os


def merging_files():
    all_files_name = ['file' + str(num_file) + '.txt' for num_file in range(1, 4)]
    result_file = 'result.txt'
    file_len_dict = {}

    for file in all_files_name:
        with open(os.path.join(os.getcwd(), file)) as reading_file:
            keys_in_dict = len(reading_file.readlines())
            if keys_in_dict not in file_len_dict.keys():
                file_len_dict[keys_in_dict] = list(file.split())
            else:
                file_len_dict.get(keys_in_dict).append(file)
            sort_keys = sorted(file_len_dict.keys())
            sort_dict = {i: file_len_dict[i] for i in sort_keys}

    with open(os.path.join(os.getcwd(), result_file), 'w') as result:
        for strings, name_file in sort_dict.items():
            for i in range(len(name_file)):
                result.write(str(name_file[i]) + '\n')
                result.write(str(strings) + '\n')
                with open(os.path.join(os.getcwd(), name_file[i])) as reading_file:
                    for rw_string in reading_file:
                        result.write(rw_string + reading_file.readline())
                result.write('\n\n')


merging_files()
