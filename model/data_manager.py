def write_in_file(file, data):
    with open(file, "a") as f:
        f.write(str(data) + "\n")


def read_full_file(file):
    with open(file, "r", encoding="utf8") as f:
        data = str(f.read())
        return data


def read_file_to_list(file):
    with open(file, "r", encoding="utf8") as f:
        data = f.readlines()
    return data


def clear_file(file):
    with open(file, "w"):
        pass


def search_for_data_in_file(file, data):
    with open(file, "r", encoding="utf8") as f:
        for line in f:
            if str(data) in str(line):
                return line.strip("\n")
        return None


def remove_line(file, data):
    lines = read_file_to_list(file)
    with open(file, "w") as f:
        for line in lines:
            if data not in line:
                f.write(line)


def update_file(file, old_data, new_data):
    lines = read_file_to_list(file)
    with open(file, "w") as f:
        for line in lines:
            if str(old_data) not in line:
                f.write(line)
            else:
                f.write(str(new_data) + "\n")
