class shoe:
    def __init__(self, country, code, prod, cost, qty) -> None:
        self.country = country
        self.code = code 
        self.prod = prod
        self.cost = cost
        self.qty = qty

    def convert_int(self):
        self.qty = int(self.qty)

    def __str__(self) -> str:
        return f"""
Country: {self.country}
Code: {self.code}
Product: {self.prod}
Cost: {self.cost}
Quantity: {self.qty}
"""


shoe_data = []

def read_data():
    with open('invebtory.txt', 'r') as file:
        for lines in file:
            data = lines.strip().split(',')

            if "Country" not in data:
                shoe_data.append(shoe(data[0], data[1], data[2], data[3], data[4]))


def find_lowest_qty():
    qty_list = []
    for index in shoe_data:
        index.convert_int()
        qty_list.append(index.qty)

read_data()
find_lowest_qty()

