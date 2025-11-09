class Water:
    def travel(self):
        print("Traveling by water")

class River(Water):
    def travel(self):
        print("Sailing on the river")

class Sea(Water):
    def travel(self):
        print("Sailing on the sea")

for water in [Water(), River(), Sea()]:
    water.travel()
