class Dog: # class

    def __init__(self, Dog_Paroda):

        self.Dog_Paroda = Dog_Paroda

    def Dogs(self):

        print(f"Парода {self.Dog_Paroda}.")

class Color(Dog):

    def Dog_Color(self, color):

        self.color = color
        
        print(f'Цвет {self.color}.')
