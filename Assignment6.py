
#calualtor class: addition, subtraction, multiplication, exponent, and division.

class Calculator():

    def add(self, x, y):
        return x+y
    
    def subtract(self, x, y):
        return x-y
    
    def multiply(self, x, y):
        return x*y
    
    def exponent(self, x, y):
        return x ** y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("undefined")
        return x / y
     
        
      
    

    
    

    
    
        

