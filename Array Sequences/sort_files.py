def sort_files(file1, file2):
    file3 = []

    #handle empty files
    if not file1 and not file2:
        return file3
    elif not file1 and file2:
        return file2
    elif not file2 and file1:
        return file1

    #handle sort
    file3 = file1.copy()
    file3.extend(file2)
    start = 0

    while start != len(file3) - 1:
        for end in range(start, len(file3)):
            if file3[end] < file3[start]:
                file3[end], file3[start] = file3[start], file3[end]
        start += 1
    return file3



file1 = [1, 6, 9]
file2 = [2, 4, 8]

def test_sort_files():
    assert sort_files(file1, file2) == [1,2,4,6,8,9]
    assert sort_files([], []) == []
    assert sort_files([2, 6], []) == [2, 6]
    return('ALL TEST CASES PASSED')

test = test_sort_files()

print(test)