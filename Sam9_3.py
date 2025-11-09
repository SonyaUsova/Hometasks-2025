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




class MotorBoat(Boat):
    def __init__(self, name, length, engine_power):
        super().__init__(name, length)
        self.engine_power = engine_power  # Мощность двигателя в л.с.

    def show_power(self):
        print(f"{self.name} has engine power of {self.engine_power} HP")

motor_boat = MotorBoat("Speedster", 10, 300)
motor_boat.sail(25)
motor_boat.show_power()
