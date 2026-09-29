class Student:
    school = "MUST"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []
        
    def add_mark(self, mark):
        self.marks.append(mark)
        
    def average_mark(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0
    
    def __str__ (self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age})"
    
    
s1 = Student("ALi", 22)
s1.add_mark(80)
s1.add_mark(90)
print(s1, s1.average_mark(), Student.school)
print(repr(s1))