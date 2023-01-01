# using simple structure's unpackaging
pair = ('Kaya', 'Mateusz')
girlfriend, boyfriend = pair
print(f'Beautiful, loving pair {girlfriend} and {boyfriend}')

# using throwaway variable name
name_first_letter, _, _, _ = girlfriend

print(f'Girlfriends\'s name first letter is: {name_first_letter}')

# using starred variables to consume lists
def display_client_contact_details(client):
    name, email, *phones = client
    print(f'{name}\n{email}\n{phones}\n')

display_client_contact_details(('Hope2Code', 'talk@h2c.io', '530-300-200', '599-310-210'))

# using built-in math functions
my_expenditures = [100, 499, 250, 399]
print(f'You have spent ${sum(my_expenditures)} so far!')

# unpackaging different tuples from the list
class FullName:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f'{self.lastName}, {self.firstName}'

class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    def __str__(self):
        return f'Employee of {self.company}, {self.name}'

company = 'Hope2Code'

# obviously we ought to use more effective structure (eg. map)

employees_expenditures = [
    (Employee(FullName('Mateusz', 'Czyzewski'), company), 399, 450, 800),
    (Employee(FullName('Kaya', 'Priwerska'), company), 250, 300, 499)
]

def show_employees_expenditures(company):
    for employee, *expenditures in employees_expenditures:
        if(employee.company == company):
            print(f'{employee} has already spent ${sum(expenditures)}')

show_employees_expenditures('Hope2Code')
