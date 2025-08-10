class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{}, {}' .format(self.first, self.last)
    
emp_1 = Employee('yared', 'pena', '22/hr')
emp_2 = Employee('Gary', 'Sanchez', '50/hr')

## don't have to pass in self because we're already giving
## the instance 
emp_1.fullname() 