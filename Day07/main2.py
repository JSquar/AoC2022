#!/usr/bin/env python
# coding: utf-8
from pathlib import Path


debug = False
# input_file = Path("input_small.txt")
input_file = Path("input_big.txt")
# input_file = Path("test.txt")

with open(input_file, "r") as fh:
    lines = fh.readlines()
    lines = [line.strip() for line in lines]


class File(object):
    root = Path("/")

    def __init__(self, path, parent, weight=0, is_file=True):
        assert isinstance(path, Path)

        self.__path = path
        self.__parent = parent
        self.__children = {}
        self.__weight = weight
        self.__is_file = is_file

    @property
    def parent(self):
        if self.__path == File.root:
            return self
        else:
            return self.__parent

    def get_child(self, name):
        assert isinstance(name, Path)

        if not name in self.__children:
            if name == File.root and self.__path == File.root:
                return self
            else:
                if debug:
                    print(
                        f"There is no child {name}! Assume it is an directory, which will be now created"
                    )
            self.add_child(name, 0, is_file=False)
        return self.__children[name]

    def add_child(self, name, weight, is_file=True):
        assert isinstance(name, Path)
        assert isinstance(weight, int)

        if name in self.__children:
            print(f"There is already a child {name}!")
        else:
            self.__children[name] = File(name, self, weight, is_file)
            self.__update_weight(weight)

    def __update_weight(self, weight):
        assert isinstance(weight, int)

        self.__weight += weight
        if self.__path != File.root:
            self.__parent.__update_weight(weight)

    @property
    def weight(self):
        return self.__weight

    @property
    def is_file(self):
        return self.__is_file

    def show(self, level):
        assert isinstance(level, int)

        print(f"{' - '*level} {self}")
        level += 1
        for child in self.__children:
            assert isinstance(
                self.__children[child], File
            ), f"Child {child} has type {type(child)}"
            self.__children[child].show(level)

    def traverse(self):
        result = [self]
        for child in self.__children:
            if not self.__children[child].__is_file:
                result.extend(self.__children[child].traverse())
            else:
                result.append(self.__children[child])
        return result

    def __str__(self):
        return f"{self.__path} [{self.__weight}] ({'f' if self.__is_file else 'd'})"


class Tree(object):
    def __init__(self):
        self.__root = File(File.root, None, is_file=False)
        self.__current = self.__root

    @property
    def root(self):
        return self.__root

    def cd(self, direction):
        if direction == Path(".."):
            self.__current = self.__current.parent
        else:
            self.__current = self.__current.get_child(direction)
        return self.__current

    def ls(self, file_list):
        for weight, entry, is_file in file_list:
            self.__current.add_child(entry, weight, is_file)

    def show(self):
        self.__root.show(0)


tree = Tree()
root = tree.cd(Path(".."))
for line in lines:
    # print(line)
    line_splitted = line.split()
    # command?
    if line.startswith("$"):
        # cd command?
        if len(line_splitted) == 3:
            tree.cd(Path(line_splitted[2]))
        # ls command will be ignored
        else:
            continue
    # file size
    else:
        # found directory
        if line.startswith("dir"):
            tree.ls([(0, Path(line_splitted[1]), False)])
        # found file
        else:
            tree.ls([(int(line_splitted[0]), Path(line_splitted[1]), True)])

tree.show()


# part A
sum = 0
for entry in root.traverse():
    if not entry.is_file and entry.weight <= 100000:
        print(f"Found {entry}")
        sum += entry.weight
print(f"Total sum: {sum}")


# part B
disk_total = 70000000
disk_required = 30000000
disk_blocked = disk_total - tree.root.weight
to_be_freed = disk_required - disk_blocked

min_size = disk_total
for entry in root.traverse():
    if not entry.is_file and entry.weight < min_size and entry.weight >= to_be_freed:
        min_size = entry.weight

print(f"Min size of unknown directory: {min_size}")
