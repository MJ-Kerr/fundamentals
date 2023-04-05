class Stack:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        def print_info(self):
            print(f'stack:,{self.name} grade: {self.grade}')

alex_python = Stack('python', 90)
martha_java = Stack('java', 80)

alex_python.print_info()
martha_java.print_info()