class vehicle:
    def _init(self,type,year,make,model,doors,roof):
        self.type = type 
        self.year = year
        self.make = make
        self.model = model 
        self.doors = doors
        self.roof = roof 

vehicle1 = vehicle()

vehicle1.type = input("Enter the vehicle type! ")
vehicle1.year = input("Enter the vehicle year! ")
vehicle1.make = input("Enter the vehicle make! ")
vehicle1.model = input("Enter the vehicle model! ")
vehicle1.doors = input("Enter the vehicle's amount doors! ")
vehicle1.roof = input("Enter the vehicle roof type! ")

print("So the vehicle you descibed is a :"+vehicle1.type+". It is a "+vehicle1.year+" "+vehicle1.make+" "+vehicle1.model)
print("It has "+vehicle1.doors+" doors and it has a "+vehicle1.roof+" !" )