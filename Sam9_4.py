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
        self.engine_power = engine_power
        self.__speed = 0  # Приватный атрибут

    def sail(self, speed):
        if speed < 0:
            print("Speed cannot be negative")
        else:
            self.__speed = speed
            print(f"{self.name} is sailing at {self.__speed} knots")

    def get_speed(self):
        return self.__speed

motor_boat = MotorBoat("Speedster", 10, 300)
motor_boat.sail(25)
print(f"Current speed: {motor_boat.get_speed()} knots")
motor_boat.sail(-10)
