import os

basic_path = os.path.join(os.getcwd(), 'files_ex3')


def count_lines(path):
    files = os.listdir(path)
    file_data = {}
    for file_name in files:
        if '.txt' in file_name and 'final' not in file_name:
            with open(os.path.join(path, file_name), encoding='utf-8') as file:
                line_count = 0
                for line in file:
                    line_count += 1
                file_data[file_name] = line_count
    sorted_data = sorted(file_data.items(), key=lambda x: x[1])
    dict(sorted_data)
    for k, v in sorted_data:
        file_path = os.path.join(path, k)
        with open(os.path.join(path, k), 'r', encoding='utf-8') as rfile,\
                open(os.path.join(path, 'final.txt'), 'a', encoding='utf-8') as file:
            file.writelines(f'{k}\n')
            file.writelines(f'{str(v)}\n')
            file.writelines(rfile.readlines())
            file.writelines(f'\n')


count_lines(basic_path)



