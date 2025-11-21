from src.package_sorter import PackageSorter
from src.ui import run_ui

def main(): 
    read_input = open("input.txt", "r") 
    for line in read_input:
        try:
            width, height, length, mass = map(float, line.split())
        except:
            print("INVALID_INPUT")
            continue
        sorter = PackageSorter()
        print(sorter.sort(width, height, length, mass))

if __name__ == "__main__":
    main()