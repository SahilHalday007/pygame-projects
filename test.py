class Employee:
    count = 0
    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.count += 1

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def validate_position(position):
        valid_positions = ["cook", "manager", "cashier", "janitor"]
        return position in valid_positions

    @classmethod
    def get_count(cls):
        return f"There are {cls.count} employees"


employee1 = Employee("Spongebob", "cook")
employee2 = Employee("Mr.Krabs", "manager")
employee3 = Employee("Squidward", "cashier")

print(employee1.get_count())