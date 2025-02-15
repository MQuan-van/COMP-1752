class PartTimeStudent:
    counter = 0  

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        PartTimeStudent.counter += 1  

    @staticmethod
    def count():
        return PartTimeStudent.counter

# Example usage
s1 = PartTimeStudent("John", "P001")
s2 = PartTimeStudent("Jane", "P002")

print("Total Part-Time Students:", PartTimeStudent.count())  