#10.1
class Elevator:
    def __init__(self, bottom_floors, top_floors, current_position=0):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_position = current_position

    def got_to_floor(self, times):
        if self.bottom_floors < times < self.top_floors and times > self.current_position:
            Elevator.floor_up(self, times)
        elif self.top_floors >= times > self.bottom_floors and times < self.current_position:
            Elevator.floor_down(self, times)

    def floor_up(self, times):
        self.current_position = self.current_position + times
        for floor in range(times):
            print(f"you are currently in floor {floor+1}")
        return self.current_position

    def floor_down(self, times):

        for floor in range(times):
            print(f"you are currently in floor {self.current_position-1}")
            self.current_position = self.current_position-1
        return self.current_position


h = Elevator(0, 10)

h.got_to_floor(5)
h.got_to_floor(3)  

#10.2
class Elevator:
    def __init__(self, bottom_floors, top_floors, current_position=0):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_position = current_position

    def got_to_floor(self, times):
        if self.bottom_floors < times < self.top_floors and times > self.current_position:
            Elevator.floor_up(self, times)
        elif self.top_floors >= times > self.bottom_floors and times < self.current_position:
            Elevator.floor_down(self, times)

    def floor_up(self, times):
        self.current_position = self.current_position + times
        for floor in range(times):
            print(f"you are currently in floor {floor+1}")
        return self.current_position

    def floor_down(self, times):

        for floor in range(times):
            print(f"you are currently in floor {self.current_position-1}")
            self.current_position = self.current_position-1
        return self.current_position

class Building:
    def __init__(self, bottom_floors, top_floors, num_elevators):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.num_elevators = num_elevators
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floors,top_floors))

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 0 or elevator_num >= self.num_elevators:
            print("Invalid elevator number.")
            return

        self.elevators[elevator_num].got_to_floor(destination_floor)
building = Building(0,10,2)
building.run_elevator(0,5)
building.run_elevator(1,4)
building.run_elevator(0,2)

#10.3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Floor not within elevator's range.")
            return

        if floor == self.current_floor:
            print("Elevator is already on this floor.")
            return

        if floor > self.current_floor:
            self.floor_up(floor)
        else:
            self.floor_down(floor)

    def floor_up(self, floor):
        for i in range(self.current_floor, floor):
            self.current_floor = i
            print(f"Elevator moving to floor {i}")

        self.current_floor = floor
        print(f"Elevator arrived at floor {floor}")

    def floor_down(self, floor):
        for i in range(self.current_floor, floor, -1):
            self.current_floor = i
            print(f"Elevator moving to floor {i}")

        self.current_floor = floor
        print(f"Elevator arrived at floor {floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 0 or elevator_num >= self.num_elevators:
            print("Invalid elevator number.")
            return

        self.elevators[elevator_num].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 2)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.fire_alarm()
