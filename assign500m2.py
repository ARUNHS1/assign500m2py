class Calculator:
    
    user_input =input(" Pass numbers (integers or floats) in the initializer")
    
    def __init__(self,num1,num2)->None:
        self.n1 = num1
        self.n2 = num2
        
    def add(self,num1,num2):
        return(self.n1 + self.n2)
    
    def substract(self,num1,num2):
        return(self.n1-self.n2)
    
    def multiply(self,num1,num2):
        return(self.n1 * self.n2)
    
    def divide(self,num1,num2):
        return(self.n1/self.n2)  
    
x = Calculator(94,10)  
    
    
    
print("addition, subtraction, division, and multiplication",x.add(94,10) , x.substract(94,10), x.multiply(94,10), x.divide(94,10))
    