class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.result = 0
        self.grade = []
    
    def add_grade(self, grade):
        self.grade.append(grade)
    
    def calculate_average(self):
        for grade in self.grade:
            self.result += float(grade)
            self.avg = self.result / len(self.grade)
        print(f"Name: {self.name}  \ntotal: {round(self.result, 2)}   \nAverage: {round(self.avg, 2)}")

    def is_passing(self):
        if self.avg >= 60:
            return True
        else:
            return False
        
    def run(self):
        while True:
            grade = input("Enter a grade (click 'enter' when finished): ")
            try:
                if not grade:
                    pass
                else:
                    self.add_grade(grade)
                    continue
                self.calculate_average()
                self.is_passing()
                break
            except AttributeError:
                print("You didn't enter any grade!")
                pass



if (__name__) == "__main__":
    bank = Student()
    bank.run()