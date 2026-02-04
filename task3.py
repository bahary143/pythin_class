contacts = {
	"anna": "0123456789",
	"bob": "9876543210",
	"carol": "546468166"
}

name = input("Enter the name: ").lower()
if "anna" == name:
    print("Anna's number is", contacts["anna"])
elif "bob" == name:
    print("Bob's number is", contacts["bob"])
elif "carol" == name:
    print("Carol's number is", contacts["carol"])
elif name == "all":
    print(f"All contacts: {contacts}")
else:
    print("Contact not found.")   


 ///////////////////////////////////////////////////

students = {
    "student1": {"name": "carol", "grade": {"math": 42, "science": 60, "english": 88}},
    "student2": {"name": "bob", "grade": {"math": 75, "science": 85, "english": 80}},
    "student3": {"name": "anna", "grade": {"math": 90, "science": 92, "english": 95}}
}

name = input("Enter the student name: ").lower()
i = name 
for i in students:
    print(f"Student name is {students[i]['name']}, and his grade's avrage is {(students[i]['grade']['math'] + students[i]['grade']['science'] + students[i]['grade']['english']) / 3}")
    break