# Model a Parking Lot using Object Oriented concepts. 
# The parking lot has 100 spaces and it should print the amount of time a vehicle has been parked on exit

import datetime

class ParkingLot:
  def __init__(self, total_space):
    self.total_space = total_space    

  def get_spaces(self):
    return self.total_space

  def check_available(self):
    if(self.total_space<1):
      return False
    return True

  def increment(self):
    self.total_space+=1
  
  def decrement(self):
    self.total_space-=1

class Parking:
    def __init__(self, vehicle, parkingLot):
      self.vehicle = vehicle
      self.pk = parkingLot
      self.start_time = datetime.date()

    def on_entry(self):
      self.pk.decrement()
      self.start_time = datetime.date()

    def on_exit(self):
      self.pk.increment()
      return self.start_time - datetime.date()

class Vehicle():
    def __init__(self, car_model):
      self.car_model = car_model

p = ParkingLot(100)
v1 = Vehicle('V1')
v2 = Vehicle('V2')
park = Parking(v1, p)
park2 = Parking(v2, p)
if(p.check_available):
    park.on_entry()
    park2.on_entry()
    print(park.on_exit())
    print(park2.on_exit())

# "Car 1" - 12: 00 -> 1:00  = 1 hr
# "Car 2" - 12: 30 -> 2:00  = 1.5 hrs


# Write a function to find the missing number from the range of 1 to n.
# [1, 1, 3, 1, 3, 4, 1] -> output is 2
# non repeating and only one number is missing in thee range

def missing_num(nums, n):
  nums = set(nums)
  total = len(nums)
  for i in range(total):
    if(i+1 not in nums):
      return i+1
  return None
