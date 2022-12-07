#10.1
class Elevator:                                                                                    
    def __init__(self, bottom_floors, top_floors, starting_position=0):                            
        self.bottom_floors = bottom_floors                                                         
        self.top_floors = top_floors                                                               
        self.starting_position = starting_position                                                 
                                                                                                   
    def got_to_floor(self, times):                                                                 
        if self.starting_position == 0:                                                            
            Elevator.floor_up(self, times)                                                         
        elif self.starting_position > times:                                                       
            Elevator.floor_down(self, times)                                                       
                                                                                                   
    def floor_up(self, times):                                                                     
        while times > self.starting_position:                                                      
            self.starting_position = self.starting_position + 1                                    
            print(f"you are currently in floor {self.starting_position}")                          
                                                                                                   
    def floor_down(self, times):                                                                   
        while times < self.starting_position:                                                      
            print(f"you are currently in floor {self.starting_position}")                          
            self.starting_position = self.starting_position - 1                                    
                                                                                                   
                                                                                                                                                                  
h = Elevator(0,10)                                                                                                                                                                     
h.got_to_floor(10)                                                                                 
h.got_to_floor(0)                                                                                  
