"""
You are a developer for a university.
Your current project is to develop a system for students to find courses they share with friends.
The university has a system for querying courses students are enrolled in,
returned as a list of (ID, course) pairs.

Write a function that takes in a collection of (student ID number, course name)
pairs and returns, for every pair of students, a collection of all courses they share.

Sample Input:

enrollments1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]

Sample Output (pseudocode, in any order):

find_pairs(enrollments1) =>
{
  "58,17": ["Software Design", "Linear Algebra"]
  "58,94": ["Economics"]
  "58,25": ["Economics"]
  "94,25": ["Economics"]
  "17,94": []
  "17,25": []
}

Additional test cases:
Sample Input:

enrollments2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"]
]

Sample output:

find_pairs(enrollments2) =>
{
  "1,0":[]
  "2,0":[]
  "2,1":[]
  "3,0":[]
  "3,1":["Course 1", "Course 2"]
  "3,2":[]
  "4,0":[]
  "4,1":[]
  "4,2":[]
  "4,3":[]
}


Sample Input:
enrollments3 = [
  ["23", "Software Design"],
  ["3", "Advanced Mechanics"],
  ["2", "Art History"],
  ["33", "Another"],
]

Sample output:


find_pairs(enrollments3) =>
{
  "23,3": []
  "23,2": []
  "23,33":[]
  "3,2":  []
  "3,33": []
  "2,33": []
}

All Test Cases:
find_pairs(enrollments1)
find_pairs(enrollments2)
find_pairs(enrollments3)

Complexity analysis variables:

n: number of student,course pairs in the input
s: number of students
c: total number of courses being offered
(note: The number of courses any student can take is bounded by a small constant)
"""


enrollments1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]


enrollments2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"],
]


enrollments3 = [
  ["23", "Software Design"],
  ["3", "Advanced Mechanics"],
  ["2", "Art History"],
  ["33", "Another"],
]


# (23,3) (2,3), (23,33), (3,33)


# 23, 3, 2, 33
#        ^  ^         (23,3), (23,2), (23, 33), (3, 2), (33,3), (2,33)


#Pseudo
# build a dict with studentID as keys and courses for values
#access the dictionary for the key of the first student's ID
#look at the values
#access the dictionary for the key of the 2nd student's ID
#compare the values to the first student
#If any are a match, we can add that value under the corresponding
#key in our output dictionary

def find_pairs(arr):

    arr.sort()
    result = {}
    dic = {}
    seen = set()
    start = 0
    ids = []

    #convert arrays into dictionary entries
    for entry in arr:
        id_num = int(entry[0])
        course = entry[1]
        if id_num not in dic:
            dic[id_num] = [course]
        else:
            dic[id_num].append(course)

    #logic for dictionary keys
    for idx, num in enumerate(arr):
        ids.append(int(arr[idx][0]))

    id1 = int(ids[start])
    while start < len(ids) - 1 :
        for end in range(start + 1, len(ids)):
            id2 = int(ids[end])
            if id1 != id2:
                result[(id1,id2)] = []
        seen.add(ids[start])
        start += 1
        id1 = ids[start]



    #logic for dictionary values
    for pair in result.keys():
        stu1 = pair[0]
        stu2 = pair[-1]

        for course in dic[stu1]:
            if course in dic[stu2]:
                result[pair].append(course)

    return result

print(find_pairs(enrollments1))




