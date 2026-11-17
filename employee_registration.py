def register_employee(employee_id, name, department):
    employee = {
        "id": employee_id,
        "name": name,
        "department": department
    }

    return employee


if __name__ == "__main__":
    result = register_employee(101, "Rahul", "IT")
    print("Employee Registered Successfully:")
    print(result)