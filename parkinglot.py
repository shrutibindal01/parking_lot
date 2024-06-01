import json
import boto3
import random

class ParkingLot:
    def __init__(self, size, spot_size=(8, 12)):
        self.spot_size = spot_size
        self.capacity = size // (spot_size[0]*spot_size[1])
        self.spots = [None] * self.capacity
    
    def is_full(self):
        return None not in self.spots
    
    def find_empty_spot(self):
        index = random.randint(0, len(self.spots)-1)
        while self.spots[index] is not None:
            index = random.randint(0, len(self.spots)-1)
        return index
    
    def park_car(self, car, spot):
        if self.spots[spot] is None:
            self.spots[spot] = car
            return True
        else:
            return False
    
    def map_parked_cars(self):
        parked_cars = {}
        for i, car in enumerate(self.spots):
            if car is not None:
                parked_cars[i] = car.license_plate
        return parked_cars
        
class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate
    
    def park(self, parking_lot):
        spot = parking_lot.find_empty_spot()
        if parking_lot.park_car(self, spot):
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot}.")
        else:
            print(f"Car with license plate {self.license_plate} could not park in spot {spot}.")
        

def main():
    parking_lot = ParkingLot(2000)
    cars = [Car(str(random.randint(1000000, 9999999))) for _ in range(20)]
    
    while not parking_lot.is_full() and cars:
        car = cars.pop()
        car.park(parking_lot)
    
    parked_cars = parking_lot.map_parked_cars()
    json_str = json.dumps(parked_cars)
    
    # Upload file to S3 bucket
    s3 = boto3.resource('s3',
        aws_access_key_id='<ACCESS_KEY>',
        aws_secret_access_key='<SECRET_KEY>')
    bucket = s3.Bucket('<BUCKET_NAME>')
    object = bucket.Object('parked_cars.json')
    object.put(Body=json_str)
    print("Parked car data saved to S3 bucket.")

if __name__ == '__main__':
    main()