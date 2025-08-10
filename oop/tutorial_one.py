## classes and instances:
## classes let us logically group and use functions + data
## methods --> function associated with a class

## a class is a blueprint for creating unique instances
class Employee:
    ## an error will spring up unless you pass
    ##pass
    ## think of the initializer as your constructor when building your class

    def __init__(self, first, last, pay):
        ##<--- everything after the period here is an 
        ## attribute of the variable 
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    ## adding methods
    ## the idea here is to make a method that will allow us to generate
    #3 the full name of an employee
    ## self makes it so that we cna remember every instance not 
    ## just a particular instance3
    def fullname(self):
        return '{}, {}' .format(self.first, self.last)

## these two newly built employee's are their own 
## Unique Version from our original class.

##now we have the TEMPLATE for what our employees can have
emp_1 = Employee('yared', 'pena', '22/hr')
emp_2 = Employee('Gary', 'Sanchez', '50/hr')

## instead of printing like this we now cna use a different way to show code reuse
'''
print(emp_1.first)
print(emp_2.first)
'''

emp_1.fullname() ## < --I don't have to pass in self
## when calling the class, it doesn't know what instance
## we're trying to run so we'll have to 
print(Employee.fullname(emp_1)) 
##print(emp_1.fullname())
##print(emp_2.fullname())