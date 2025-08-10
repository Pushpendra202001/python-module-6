# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

student_marks= {'divya':99, 'alice':85, 'user1':30, 'user2':20, 'ajay':60, 'jay':100}
name = input("Enter the student\'s name: ")
if name in student_marks:
    mark = student_marks[name]
    print(name+"\'s marks:", mark)
else:
    print("Student not found.")