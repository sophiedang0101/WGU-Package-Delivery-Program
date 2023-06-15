# Project: C950 WGU Delivery Algorithm Program
# Author: Sophie Dang
# Student ID: 009522974

# this class is used to create a hash table instance.
# referenced WGU C950_Videos: Webinar-1-Let's Go Hashing by Dr.Cemal Tepe.
# time and space complexities referenced YouTube Video: "Big O Notation - with Examples in Python" by John Krohn.
# the CI provided the above reference sources' links in a welcome email.

class CreateHashTable:
    # constructor for the hash table.
    # time-complexity: O(1).
    # space-complexity: O(ht_initial_capacity).
    def __init__(self, ht_initial_capacity=20):
        self.ht_initial_capacity = ht_initial_capacity
        self.buckets_list = [None] * self.ht_initial_capacity

    # function used to create the hash value or index where the key-pair will be stored at.
    # time-complexity: O(n).
    # space-complexity: O(1).
    def generate_hash_value(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.ht_initial_capacity

    # this function is used to insert key-value pairs into the hash table.
    # this function will be used when inserting packages to the hash table.
    # time-complexity: O(n).
    # space-complexity: O(1).
    def insert_item(self, key, value):
        # generate a hash value from the input key.
        k_hash = self.generate_hash_value(key)
        kv_pair = [key, value]  # create a list containing the key and value.

        # if the bucket is empty, create a new list and store the key-value pair in it.
        if self.buckets_list[k_hash] is None:
            self.buckets_list[k_hash] = list([kv_pair])
            return True
        else:  # if the bucket isn't empty.
            for pair in self.buckets_list[k_hash]:  # loop through each key-value pair in the bucket.
                if pair[0] == key:  # if the key already exists in the bucket,
                    pair[1] = value  # update the value of the existing key-value pair.
                    return True
            # if the key doesn't exist in the bucket, add the key-value pair to the list.
            self.buckets_list[k_hash].append(kv_pair)
            return True

    # this function is used to look up a specific item in the hash table and retrieve its value.
    # time-complexity: O(n).
    # space-complexity: O(1).
    def retrieve_item(self, key):
        k_hash = self.generate_hash_value(key)  # create a hash value from the input key.

        if self.buckets_list[k_hash] is not None:  # if the bucket isn't empty,
            for pair in self.buckets_list[k_hash]:  # loop through each key-value pair in the bucket.
                if key == pair[0]:  # if the key matches the input key,
                    return pair[1]  # return the corresponding value.
        return None  # If the key isn't found or the bucket is empty, return None.

    # this function is used to delete an item from the hash table.
    # time-complexity: O(n).
    # space-complexity: O(1).
    def delete_item(self, key):
        k_hash = self.generate_hash_value(key)  # create a hash value from the input key.

        if self.buckets_list[k_hash] is None:  # if the bucket at the hash value is empty, return False.
            return False

        for i in range(0, len(self.buckets_list[k_hash])):  # loop through each key-value pair in the bucket.
            if self.buckets_list[k_hash][i][0] == key:  # if the key matches the input key,
                self.buckets_list[k_hash].pop(i)  # remove the key-value pair from the bucket.
                return True  # return True to indicate that deletion was successful.
        return False  # if the key isn't found, return False.

    # this function is used to print all items in the hash table.
    # time complexity: O(n).
    # space complexity: O(1).
    def print_items(self):
        for item in self.buckets_list:
            if item is not None:
                print(str(item))
