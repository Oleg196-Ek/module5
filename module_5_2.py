class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor: int):
        if new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    print(h1)
    print(h2)
    print(len(h1))
    print(len(h2))
if main == main():
    main()










