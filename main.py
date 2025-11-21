from package_sorter import PackageSorter


def __main__(): 
    read_input = open("input.txt", "r") 
    for line in read_input:
        width, height, length, mass = map(float, line.split())
        sorter = PackageSorter()
        print(sorter.sort(width, height, length, mass))

if __name__ == "__main__":
    __main__()