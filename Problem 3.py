class SchoolSystem:
    def __init__(self):
        self.students = []  
        self.lecturers = []  
        self.projects = []  

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Cannot add more students")
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Cannot add more lecturers")
    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Cannot add more projects")
    def display_summary(self):
        print("\nStudents:")
        for student in self.students:
            print(f"- {student}")

        print("\nLecturers:")
        for lecturer in self.lecturers:
            print(f"- {lecturer}")

        print("\nProjects:")
        for project in self.projects:
            print(f"- {project}")
school = SchoolSystem()
school.add_student("Quan")
school.add_student("Bao")
school.add_lecturer("Dr Thy")
school.add_lecturer("Mrs Quyen")
school.add_project("OOP")
school.add_project("HTML")
school.display_summary()