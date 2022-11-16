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
      
