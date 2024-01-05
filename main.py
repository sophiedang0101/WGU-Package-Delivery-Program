# Project: C950 WGU Delivery Algorithm Program
# Author: Sophie Dang
# Student ID: 009522974

# time and space complexities for all code referenced YouTube Video: "Big O Notation - with Examples in Python"
# by John Krohn.
# referenced datetime — Basic date and time types - Python Documentation.
# the CI provided the above-referenced sources in a welcome email.
# referenced 8. Errors and Exceptions - Python Documentation.

from Truck import Truck
import datetime
from CSV_Reader import packages_hashtable
from CSV_Reader import retrieve_distance_between
from CSV_Reader import retrieve_addressId

# create three truck objects to represent the three trucks that'll be delivering the packages.
# space complexity: O(1).
# time complexity: O(1).
truck_num1 = Truck(1)
truck_num2 = Truck(2)
truck_num3 = Truck(3)

# Define the package IDs for each truck
truck_packages = {
    truck_num1: [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
    truck_num2: [3, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
    truck_num3: [6, 2, 4, 5, 7, 8, 10, 11, 25, 28, 32, 33]
}

# Use a loop to insert packages into each truck
# space complexity: O(1).
# time complexity: O(n).
for truck, package_ids in truck_packages.items():
    for data_row in package_ids:
        truck.insert_package_data(packages_hashtable.retrieve_item(data_row))

# these assignments set a truck's departure time and current time to specific times based on the packages.
# truck 1 departs the earliest at 8 a.m. It'll help take into account particular package deadlines.
# truck 2 departs at 10:20 a.m. because of the address change with package #9, which will be corrected at 10:20 a.m.
# truck 3 departs at 9:05 a.m. to account for delayed packages.
# space complexity: O(1).
# time complexity: O(1).
truck_num1.time_of_departure = datetime.timedelta(hours=8)
truck_num1.current_time = datetime.timedelta(hours=8)
truck_num2.time_of_departure = datetime.timedelta(hours=10, minutes=20)
truck_num2.current_time = datetime.timedelta(hours=10, minutes=20)
truck_num3.time_of_departure = datetime.timedelta(hours=9, minutes=5)
truck_num3.current_time = datetime.timedelta(hours=9, minutes=5)


# this function is used to update a truck's status to the given status string.
# space complexity: O(1).
# time complexity: O(1).
def update_truck_status(current_truck, status):
    current_truck.truck_status = status


# this function is used to loop over each package in a given truck's package set,
# and updates the "packageId_num" attribute of each package to match the truck's "truckId_num". This is done to identify
# which packages belong to which specific truck.
# space complexity: O(1).
# time complexity: O(n).
def update_package_ids(truck):
    # Iterate over each package in the input truck object's set_of_packages.
    for package in truck.set_of_packages:
        # Update the packageId_num attribute of the package to the truck ID.
        package.truck_id_num = truck.truckId_num


# this function uses the nearest neighbor algorithm to determine an efficient route for delivering packages.
# space complexity: O(n).
# time complexity: O(n^2).
def nearest_neighbor_delivery_algo(truck_object):
    # call the update_package_ids() function to update packages IDs to the ID of the input truck object.
    update_package_ids(truck_object)
    # the algorithm continues to run until there are no packages left to deliver or when a truck's packages set
    # contains 0 packages.
    while truck_object.set_of_packages:
        update_truck_status(truck_object, "En Route")  # call the update_truck_status() function to update the status
        # of the truck object to "En Route".

        min_distance = float('inf')  # assign the min distance to infinity initially.
        next_package = None  # this variable represents the next package to be delivered.

        for package in truck_object.set_of_packages:  # iterate through the input truck's set of packages.
            # use the retrieve_distance_between() function to retrieve the distance value given the ID of the truck's
            # current address and the ID of the package's address.
            distance = retrieve_distance_between(retrieve_addressId(truck_object.truck_current_address),
                                                 retrieve_addressId(package.package_address))

            #  if the distance value is less than or equal to the previous min distance, this value is assigned
            #  to be the new min distance, and the next_package variable becomes the specific package.
            if distance <= min_distance:
                min_distance = distance
                next_package = package

        # the next_package is removed from the truck's set of packages because it has been successfully delivered.
        truck_object.set_of_packages.remove(next_package)
        # the min distance value is added to the truck's mileage.
        truck_object.miles_traveled += min_distance
        # the truck's current address is assigned to the next or upcoming package's address.
        truck_object.truck_current_address = next_package.package_address
        # the min distance value divided by 18 (truck's avg driving speed of 18mph)
        # is added to the truck's current time.The time is converted to hours because of miles/mph = hours.
        truck_object.current_time += datetime.timedelta(hours=min_distance / 18)
        # the departure time of the upcoming package is assigned to the truck's departure time.
        next_package.departure_time = truck_object.time_of_departure
        # the delivery time of the upcoming package is assigned to the current time of the truck.
        next_package.delivery_time = truck_object.current_time

    # a truck completes its route once all packages have been delivered.
    # the update_truck_status () function is called again to set the truck's status to "Route Finished" indicating
    # the truck has finished delivering all packages.
    update_truck_status(truck_object, "Route Finished")


# call the nearest neighbor delivery algorithm for each truck object.
nearest_neighbor_delivery_algo(truck_num1)
nearest_neighbor_delivery_algo(truck_num2)

# only run the nearest neighbor delivery algorithm for truck 3 when both truck 1 and truck 2 have finished their routes.
# this is because there are only two drivers available.
if truck_num1.truck_status == "Route Finished" or truck_num2.truck_status == "Route Finished":
    nearest_neighbor_delivery_algo(truck_num3)

# calculate the total mileage by of the three trucks by adding the mileage of each truck together.
total_traveled_miles = truck_num1.miles_traveled + truck_num2.miles_traveled + truck_num3.miles_traveled

# UI for user to interact with the program.
print("---------------------------------------------------------------------------------------------------")
print("                      Welcome to Western Governors University Parcel Service!                       ")
print("---------------------------------------------------------------------------------------------------")

# display the total mileage of the three trucks.
print(f"\nThe total mileage amount for all 3 trucks is {total_traveled_miles} miles.\n")
print("---------------------------------------------------------------------------------------------------")

while True:
    try:
        # ask the user to choose an option to continue.
        user_input = input('Hello, Welcome to WGUPS! Please choose an option from the list below to continue:\n'
                           '  A.) Search for a single package\'s status at a given time.\n'
                           '  B.) Search for all package statuses at a given time.\n'
                           '  Q.) Quit Program\n').lower()
        # if the user chooses 'Q', quit the program.
        if user_input == 'q':
            print("This program will now shut down. Goodbye. See you again soon.")
            break
        # get the hour and minute values from the user.
        hour_value = int(input("Please enter an hour value that's between 0 and 23:\n "))
        minute_value = int(input("Please enter a minute value that's between 0 and 59:\n "))
        # validate the hour and minute values from the user. If invalid, shut down the program.
        if not (0 <= hour_value < 24) or not (0 <= minute_value < 60):
            print("Invalid time or minute value was entered. This program will now shut down.")
            break
        # create a timedelta object based on the user's hour and minute inputs.
        t_input = datetime.timedelta(hours=hour_value, minutes=minute_value)
        # if the user enters "B", search for all package statues at a given time, and print them out.
        if user_input == 'b':
            print("packageID | truckID | address| deadline| city| zipcode| wt.| departure time| status|")
            for row in range(1, 41):
                try:
                    # retrieve the package info from the packages hashtable.
                    package = packages_hashtable.retrieve_item(row)
                    # retrieve the package status at the given time.
                    package.retrieve_package_status(t_input)

                    # if the package ID is 9, and the input time is later than 10:20, update the
                    # package address to the correct one. The address is incorrect before 10:20.
                    unique_time_case = datetime.timedelta(hours=10, minutes=20)
                    if package.packageId_num == 9 and t_input > unique_time_case:
                        package.package_address = "410 S State St"
                    elif package.packageId_num == 9 and t_input < unique_time_case:
                        package.package_address = "300 State St"

                    # print the package info.
                    if package.package_status == "Delivered":
                        package.package_status = package.delivery_time
                        print(
                            f"{package.packageId_num}| {package.truck_id_num} | {package.package_address} | {package.package_delivery_deadline}"
                            f"| {package.package_city} | {package.package_zipcode} | {package.package_weight} | {package.departure_time}|Delivered at:{package.package_status}|")
                    elif package.package_status != "Delivered":
                        package.package_status = package.package_status
                        print(
                            f"{package.packageId_num}| {package.truck_id_num} | {package.package_address} | {package.package_delivery_deadline}"
                            f"| {package.package_city} | {package.package_zipcode} | {package.package_weight} | {package.departure_time}| {package.package_status}")

                except KeyError:
                    print(f"Package with ID {row} wasn't found.")
        # if the user enters "A", search for a single package's status at a given time and
        # print the info.
        elif user_input == "a":
            # ask the user for the package ID.
            package_id_num = int(input("Please enter a package ID number that's between 1 and 40:\n "))
            # validate that the package ID is valid, shut down the program if invalid.
            if not (1 <= package_id_num <= 40):
                print("Invalid ID number was entered. The program will now shut down.")
                break
            try:
                # retrieve the package info from the packages hashtable.
                package = packages_hashtable.retrieve_item(package_id_num)
                # retrieve the package status at the given time.
                package.retrieve_package_status(t_input)

                unique_time_case = datetime.timedelta(hours=10, minutes=20)
                print("packageID | truckID | address| deadline| city| zipcode| wt.| departure time| status|")

                # if the package ID is 9, and the input time is later than 10:20, update the
                # package address to the correct one. The address is incorrect before 10:20.
                if package.packageId_num == 9 and t_input > unique_time_case:
                    package.package_address = "410 S State St"
                elif package.packageId_num == 9 and t_input < unique_time_case:
                    package.package_address = "300 State St"

                # print package info.
                if package.package_status == "Delivered":
                    package.package_status = package.delivery_time
                    print(
                        f"{package.packageId_num}| {package.truck_id_num} | {package.package_address} | {package.package_delivery_deadline}"
                        f"| {package.package_city} | {package.package_zipcode} | {package.package_weight} | {package.departure_time}|Delivered at:{package.package_status}|")

                elif package.package_status != "Delivered":
                    package.package_status = package.package_status
                    print(
                        f"{package.packageId_num}| {package.truck_id_num} | {package.package_address} | {package.package_delivery_deadline}"
                        f"| {package.package_city} | {package.package_zipcode} | {package.package_weight} | {package.departure_time}| {package.package_status}")

            except KeyError:
                print(f"Package with ID {package_id_num} wasn't found.")
                continue
        else:
            print("Invalid option was entered. Please try again and choose a valid option.")

    except ValueError:
        print("Invalid input was entered. Please enter numeric values where required.\n")
    print("\n")

# ------------------------------------------- SOURCES: WORKS CITED----------------------------------------------------

# datetime — Basic date and time types. (n.d.). Python Documentation.
# https://docs.python.org/3/library/datetime.html

# 8. Errors and Exceptions. (n.d.). Python Documentation.
# https://docs.python.org/3/tutorial/errors.html

# GeeksforGeeks. (2023). Depth-First Search or DFS for a Graph. GeeksforGeeks.
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

# Joe James. (2016, January 23). Python: Creating a HASHMAP using Lists [Video]. YouTube.
# https://www.youtube.com/watch?v=9HFbhPscPU0

# Jon Krohn. (2020, January 21). Big O Notation — with Examples in Python [Video]. YouTube.
# https://www.youtube.com/watch?v=5yJ_QLec0Lc

# 1.6. Nearest Neighbors. (n.d.). Scikit-learn.
# https://scikit-learn.org/stable/modules/neighbors.html

# Lysecky, R., & Vahid, F. (2018). C950: Data Structures and Algorithms II. zyBooks.
# https://learn.zybooks.com/zybook/WGUC950AY20182019/chapter/2/section/5

# Make School. (2021, May 4). What is Pseudocode in Python? Day 21 [Video]. YouTube.
# https://www.youtube.com/watch?v=3WSrPxINIt8

# Portilla, J. (2021, March). The Complete Python Bootcamp from Zero to Hero [Video]. Udemy.
# https://wgu.udemy.com/course/complete-python-bootcamp/learn/lecture/9478292#overview

# Portilla, J. (2021b, March). The Complete Python Bootcamp From Zero to Hero [Video]. Udemy.
# https://wgu.udemy.com/course/complete-python-bootcamp/learn/lecture/9478294#overview

# Portilla, J. (2021c, March). The Complete Python Bootcamp From Zero to Hero [Video]. Udemy.
# https://wgu.udemy.com/course/complete-python-bootcamp/learn/lecture/20568974#overview

# Tepe, C. “C950 – Webinar-1 – Let’s Go Hashing”. C950 Supplemental Material.
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71

# Tepe, C. “C950 – Webinar-2 – Getting Greedy, who moved my data”. C950 Supplemental Material.
# https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
