#11.1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(
            f"The publication for this book is {self.name}. The author is {self.author} and this book has {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        print(f"The publication for this magazine is {self.name}. The chief editor is {self.chief_editor}")


magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Comprament 6", "Rosa Liksom", 192)
magazine.print_info()
book.print_info()

#11.2
class Car:
    def __init__(self, registration_num=0, max_speed=0, current_speed=0, travelled_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accerelate(self, new_speed=0):
        self.current_speed = self.current_speed + new_speed
        if new_speed > self.max_speed or new_speed < 0:
            print("The speed of the car must stay below the set maximum"
                  " and cannot be less than zero.\n"
                  "try again")
            return

    def drive(self, num_of_hours=0):
        self.travelled_distance = num_of_hours * self.current_speed
        return


class ElectricCar(Car):
    def __init__(self, registration_num="ABC", max_speed=0, battery_capacity=1.1):
        super().__init__(registration_num, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_num=0, max_speed=0, gas_tank=1.0):
        super().__init__(registration_num, max_speed,)
        self.gas_tank = gas_tank

elec_car = ElectricCar("ABC-15", 180, 52.5)

elec_car.accerelate(50)
elec_car.drive(3)
print(f"{elec_car.travelled_distance}")

gas_car = GasolineCar("ACD-123", 165, 32.3)
gas_car.accerelate(50)
gas_car.drive(3)
print(f"{gas_car.travelled_distance}")
