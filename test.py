from package_sorter import PackageSorter

def test_sort():
    sorter = PackageSorter()
    assert sorter.sort(10, 10, 10, 10) == "STANDARD"
    assert sorter.sort(10, 10, 10, 20) == "SPECIAL"
    assert sorter.sort(10, 10, 10, 30) == "SPECIAL"
    assert sorter.sort(10, 10, 151, 20) == "REJECTED"
    assert sorter.sort(10, 10, 10, -10) == "INVALID_INPUT"
    assert sorter.sort(10, 10, 10, 0) == "INVALID_INPUT"
    assert sorter.sort(10, 10, 10, "10") == "INVALID_INPUT"