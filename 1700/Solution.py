class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] in students:
                    student = students.pop(0)
                    students.append(student)
                else:
                    break
        return len(students)
