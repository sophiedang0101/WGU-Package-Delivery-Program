# Project: C950 WGU Delivery Algorithm Program
# Author: Sophie Dang
# Student ID: 009522974
import datetime


# this class is used to create a truck object.
# referenced Udemy course "The Complete Python Bootcamp From Zero to Hero in Python"
# section "Object-Oriented Programming" by Jose Portilla.
# referenced Python Documentation website: datetime - Basic date and time types.
# time and space complexities referenced YouTube Video: "Big O Notation - with Examples in Python" by John Krohn.
# the CI provided the above-referenced sources' links in a welcome email.
class Truck:
    # time and space complexities: O(1).
    # constructor for to create a Truck object.
    def __init__(self, truckId_num):
        self.truckId_num = truckId_num
        self.set_of_packages = set()  # a set to store packages that'll be loaded onto the truck object.
        self.truck_current_address = "4001 South 700 East"  # the truck's current_address.
        self.num_loaded_packages = 0  # number of packages loaded onto the truck.
        self.avg_driving_speed = 18  # average driving speed in miles per hour.
        self.time_of_departure = datetime.timedelta()  # the truck's departure time.
        self.current_time = datetime.timedelta()  # current time of the truck.
        self.miles_traveled = float(0)  # miles traveled by the truck.
        self.truck_status = "At Delivery Hub"  # current status of the truck.

    # this function is used to insert packages into the truck's set of packages.
    # time and space complexities: O(1).
    def insert_package_data(self, input_package):
        if self.num_loaded_packages <= 16:  # if the maximum number of packages for a truck hasn't been reached,
            self.set_of_packages.add(input_package)  # insert the package to the truck's set of packages.
            self.num_loaded_packages += 1  # increase the number of packages that have been loaded.
        else:  # if the max capacity of packages has been reached, print this statement.
            print('The maximum amount of packages has been loaded onto the truck')
