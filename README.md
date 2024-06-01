Parking Lot Management System
  This project implements a simple parking lot management system. The system consists of two main classes: ParkingLot and Car. The ParkingLot class manages the parking spaces and keeps track of which cars are parked in which spots, while the Car class represents individual cars with a unique 7-digit license plate. The program also includes functionality to save the state of the parking lot to a JSON file and upload this file to an S3 bucket.

Features
Create a parking lot with a specified size and parking spot dimensions.
  Park cars in random available spots.
  Ensure cars do not park in already occupied spots.
  Save the mapping of parked cars to spots in a JSON file.
  Upload the JSON file to an S3 bucket.

Prerequisites
  Python 3.x
  boto3 library for AWS S3 interactions (pip install boto3)

Running the Program
Clone the repository:
  1. git clone https://github.com/shrutibindal01/parking_lot
  2. cd parking_lot
  3. pip install boto3
  4. export AWS_ACCESS_KEY_ID=<your-access-key-id>
  5.export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
  6. bucket_name = '<your-bucket-name>'
  7. python parking_lot.py

Example Output

Car with license plate 1234567 parked successfully in spot 5.
Car with license plate 2345678 parked successfully in spot 10.
...
Car with license plate 3456789 could not park in spot 5.
...
Parked car data saved to S3 bucket.
