class Dog: # class

    def __init__(self, Dog_Poroda):

        self.Dog_Poroda = Dog_Poroda

    def Dogs(self):

        print(f"Порода {self.Dog_Poroda}.")

class Color(Dog):

    def Dog_Color(self, color):

        self.color = color
        
        print(f'Цвет {self.color}.')
