def search_employee(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return "Employee Not Found"


if __name__ == "__main__":
    employees = [
        {"id": 101, "name": "Rahul", "department": "IT"},
        {"id": 102, "name": "Priya", "department": "HR"}
    ]

    result = search_employee(employees, 102)
    print("Search Result:")
    print(result)