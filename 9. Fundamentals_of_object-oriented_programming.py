# 9.1
class Car:
    def __init__(self, registration_num=0, max_speed=0, current_speed=0, travelled_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    pass


car = Car()
car.registration_num = "ABC-123"
car.max_speed = 142
print(f" Registration number is {car.registration_num}.\n"
      f" The maximum speed is {car.max_speed} km/h.\n"
      f" Current speed is {car.current_speed} km/h.\n"
      f" Travelled distance is {car.travelled_distance} km.\n")
  
# 9.2
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


car = Car()
car.registration_num = "ABC-123"
car.max_speed = 142

car.accerelate(30)
car.accerelate(70)
car.accerelate(50)
print(f" Current speed is {car.current_speed} km/h.\n")
car.accerelate(-200)
print(f" Current speed is {car.current_speed} km/h.\n")

# 9.3
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


car = Car()
car.registration_num = "ABC-123"
car.max_speed = 142

car.accerelate(30)
car.drive(3)
print(f" Current speed is {car.current_speed} km/h.\n")
print(f" travelled distance is {car.travelled_distance} km.\n")
