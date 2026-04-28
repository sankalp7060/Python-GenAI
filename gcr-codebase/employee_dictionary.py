employees = {
    101: {"name": "Alice", "salary": 50000},
    102: {"name": "Bob", "salary": 60000},
    103: {"name": "Charlie", "salary": 55000}
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print(employees[emp_id])
else:
    print("Employee not found")