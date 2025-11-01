class Boat:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.speed = 0  # Скорость в узлах

    def sail(self, speed):
        self.speed = speed
        print(f"{self.name} is sailing at {self.speed} knots")

my_boat = Boat("Wave Rider", 15)
my_boat.sail(20)
