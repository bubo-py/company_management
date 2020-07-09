
class employee:
    def __init__(self, first_name, last_name, pesel, department, pay): # setting class arguments
        self.First_name = str(first_name) # string first name
        self.Last_name = str(last_name)
        self.PESEL = int(pesel) # PESEL number as a integer
        self.Department = str(department)
        self.Pay = int(pay)
        self.Email = first_name + '.' + last_name + '@python.com' # automatically creating email of each employee

    @classmethod # decorator sets function as classmethod, which means that method is not working now with an instance of a class, but with the classs itself
    def from_str(cls, string): # it takes class itself as an argument, and the string that you type to create new instance of employee
        first_name, last_name, pesel, department, pay = string.split(', ') # that line converts your typed text to the class
        return database.append(cls(first_name, last_name, pesel, department, pay)) # creating class with above values and adding it into the "database"

database = [] # creating empty so-called database(just an empty list)

employee.from_str('Jan, Kowalski, 91052793277, IT, 40_000') # some already hardcoded examples
employee.from_str('Cobie, Wheatley, 83022132896, Design, 70_000')
employee.from_str('Lisa, Waters, 76061494771, HR, 60_000')

running = True # to hold the program, because of that you can add multiple employees at once and you don't have to reset script every time.. it's no needed in real world app
                # but here there's not any real database so it has to be like that
while running:
    inp = input('What do you want do to?\n1. Add\n2. Show all employees\n3. Quit\n') # asking user for input
    if inp == '1': # if input is 1
        inp1 = input("Add your employee by the following format:\nFirst name, Last name, PESEL, Department, Pay:\n") # asking user for input with properly formated data
        employee.from_str(inp1) # creating class via from_str classmethod, parsing the above input
        print('Employee added successfully!') # printing confirmation

    if inp == '2': # if input is 2
        for emp in database: # for each employee in our database(list)
            print(emp.__dict__) # showing a dictionary of all employees, instead of memory location of the object like "<__main__.employee object at 0x0000000001EBF668>"

    if inp == '3': # if input is 3
        break # end the loop

