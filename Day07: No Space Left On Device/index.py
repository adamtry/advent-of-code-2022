import re


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, files: list[File] = None, parent_directory=None, sub_directories=None):
        self.name: str = name
        self.parent_directory: Directory = parent_directory
        self.size = None
        self.files = [] if files is None else files
        self.sub_directories = [] if sub_directories is None else sub_directories

        if self.parent_directory is not None:
            self.path = (self.parent_directory.path + "/" + self.name).replace(" ", "")
        else:
            self.path = self.name

    def get_size(self):
        if self.size is not None:
            return self.size
        else:
            size = 0
            for file in self.files:
                size += file.size
            for sub_directory in self.sub_directories:
                size += sub_directory.get_size()
            self.size = size
            return size


def get_terminal_lines():
    with open("input.txt", "r") as outfile:
        data = outfile.read()
    terminal_output = data.splitlines()
    return terminal_output


def build_filesystem(terminal_lines: list[str]) -> dict[str:Directory]:
    root = Directory("")
    all_directories = {
        "/": root
    }
    current_directory = root
    for out_line in terminal_lines[1:]:

        line_is_command = out_line.startswith("$ cd")
        if line_is_command:
            if out_line.endswith(".."):  # Moving up a directory
                current_directory = current_directory.parent_directory
                continue
            else:
                directory = Directory(name=out_line[4:], parent_directory=current_directory)
                current_directory.sub_directories.append(directory)
                current_directory = directory
                all_directories[current_directory.path] = directory

        line_is_file = bool(re.search("[0-9].*", out_line))
        if line_is_file:
            file_name = out_line.split()[-1]
            file_size = int(out_line.split()[0])
            current_directory.files.append(File(file_name, file_size))
    return all_directories


def get_total_size_all_directories_under_100000_p1(indexed_directories: dict[str:Directory]):
    total_size = 0
    for dir_path in indexed_directories.keys():
        directory = indexed_directories[dir_path]
        directory_size = directory.get_size()
        if directory_size <= 100000:
            total_size += directory_size
    print(total_size)


def get_smallest_directory_to_delete_to_free_up_30000000_p2(indexed_directories):
    total_available_space = 70000000
    total_used_space = indexed_directories["/"].get_size()
    free_space = total_available_space - total_used_space

    directories = indexed_directories.values()
    valid_directory_sizes = []
    for directory in directories:
        dir_size = directory.get_size()
        if free_space + dir_size >= 30000000:
            valid_directory_sizes.append(dir_size)
    print(min(valid_directory_sizes))


if __name__ == "__main__":
    lines: list[str] = get_terminal_lines()
    filesystem: dict[str:Directory] = build_filesystem(lines)
    get_total_size_all_directories_under_100000_p1(filesystem)
    get_smallest_directory_to_delete_to_free_up_30000000_p2(filesystem)
