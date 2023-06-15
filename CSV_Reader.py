# Project: C950 WGU Delivery Algorithm Program
# Author: Sophie Dang
# Student ID: 009522974

# time and space complexities for all code referenced YouTube Video: "Big O Notation - with Examples in Python"
# by John Krohn.
# referenced Udemy course "The Complete Python Bootcamp From Zero to Hero in Python"
# section "Working with PDFs and Spreadsheet CSV Files" by Jose Portilla.
# the CI provided the above-referenced sources' links in a welcome email.

import csv
from HashTable import CreateHashTable
from Packages import Package

# import all the distances from the provided distance csv file and store them in an empty list.
# space complexity: O(n).
# time complexity: O(n).
with open("CSV/distances_file.csv") as distance_csvfile:
    distances_csv_list = csv.reader(distance_csvfile)
    distances_csv_list = list(distances_csv_list)

# import all the addresses from the provided addresses csv file and store them in an empty list.
# space complexity: O(n).
# time complexity: O(n).
addresses_list = []
with open("CSV/addresses_file.csv") as address_csvfile:
    address_csv_file = csv.reader(address_csvfile)
    for row_data in address_csv_file:
        addresses_list.append(row_data)

# import all the packages' info from the provided packages csv file and store them in the hash table.
# used the insert_item() function from the hash table class to insert packages into the hash table.
# set each row to a certain attribute from each package.
# space complexity: O(n).
# time complexity: O(n).
packages_hashtable = CreateHashTable()  # create a HashTable object to store the packages.
with open('CSV/packages_file.csv') as csv_package_file:
    packageCSV_file = csv.reader(csv_package_file, delimiter=',')  # read the provided packages csv file.
    for row in packageCSV_file:  # iterate over each row in the csv file.
        p_ID = int(row[0])  # retrieve the package ID.
        p_address = row[1]  # retrieve the package address.
        p_city = row[2]  # retrieve the package city.
        p_state = row[3]  # retrieve the package state.
        p_zipcode = row[4]  # retrieve the package postal code.
        p_deadline = row[5]  # retrieve the package delivery deadline.
        p_weight = row[6]  # retrieve the package weight.
        p_status = "At Delivery Hub"  # set the initial status of the package to the Hub.

        # create a Package object with the extracted data from the packages csv file.
        package_object = Package(p_ID, p_address, p_city, p_state, p_zipcode, p_deadline, p_weight, p_status)
        # insert the package into the HashTable using its ID number as the key.
        packages_hashtable.insert_item(p_ID, package_object)


# this function is used to look for the input address in the "addresses_list" created from
# info extracted from the provided addresses csv file.It returns the address ID associated with the matching address.
# space complexity: O(1).
# time complexity: O(n).
def retrieve_addressId(package_address):
    for row in addresses_list:  # loop over each row in the addresses list.
        if package_address in row[2]:  # if the input address is found in the third element of the row,
            return int(row[0])  # return the corresponding address ID (the first element of the row).
    return -1  # return -1 to indicate that the address ID wasn't found.


# this function accepts two addresses IDs, and retrieves the distance between them from the distances_csv_list that was
# created from the distance data extracted from the provided distances csv file.
# if the distance value is empty, the function retrieves the distance in the opposite direction.
# space complexity: O(1).
# time complexity: O(1).
def retrieve_distance_between(address1_ID, address2_ID):
    # retrieve the distance value from the distances csv list using the two input addresses' IDs.
    distance_val = distances_csv_list[address1_ID][address2_ID]
    # if the distance is empty, retrieve the distance value in the opposite direction, flipping address 1 and address 2.
    if distance_val == '':
        distance_val = distances_csv_list[address2_ID][address1_ID]

    return float(distance_val)  # convert the distance value to a float and return it.


