# Project: C950 WGU Delivery Algorithm Program
# Author: Sophie Dang
# Student ID: 009522974

# this class is used to create a package object.
# referenced Udemy course "The Complete Python Bootcamp From Zero to Hero in Python"
# section "Object-Oriented Programming" by Jose Portilla.
# time and space complexities referenced YouTube Video: "Big O Notation - with Examples in Python" by John Krohn.
# the CI provided the above-referenced sources' links in a welcome email.

class Package:
    # constructor to create a package object.
    # constructor contains all attributes from the provided packages csv file.
    # time and space complexities: O(1).
    def __init__(self, packageId_num, package_address, package_city, package_state, package_zipcode,
                 package_delivery_deadline, package_weight, package_status):
        self.packageId_num = packageId_num
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zipcode = package_zipcode
        self.package_delivery_deadline = package_delivery_deadline
        self.package_weight = package_weight
        self.package_status = package_status
        self.truck_id_num = None  # this attribute is used to assign a truck ID to a package to ensure the package
        # is on the correct truck.
        self.departure_time = None  # this attribute is used to retrieve a package's time of departure.
        self.delivery_time = None  # this attribute is used to retrieve a package's time of delivery.

    # this function is used to set the status of a package based on a certain time input
    # time and space complexities: O(1).
    def retrieve_package_status(self, t_input):
        # Check the status of the package based on the input time.
        if self.delivery_time and t_input > self.delivery_time:
            self.package_status = "Delivered"
        elif self.departure_time and self.delivery_time and self.departure_time < t_input < self.delivery_time:
            self.package_status = "En Route"
        else:
            self.package_status = "At Delivery Hub"

