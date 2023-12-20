class Human:

    def __init__(self, name, age, height, fav_beverage):
        self.name = name
        self.age = age
        self.height = height
        self.fav_beverage = fav_beverage
        #self.legs = legs

    def __str__(self):
        return f"""
        Human name : {self.name}
        Human age : {self.age}
        Human height : {self.height}
        Human favourite beverage : {self.fav_beverage}
        """


    def change_age(self, new_age):
        self.age = new_age


first_human = Human("John", 28, 6.5, "latte")

print(first_human)

first_human.change_age(26)

print(first_human)