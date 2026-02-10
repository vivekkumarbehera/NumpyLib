#Add element in a tuple by converting it to a list and back to a tuple

original_tuple = (1, 2, 3)
print("Original Tuple:", original_tuple)

temp_list = list(original_tuple)

temp_list.append(4)

updated_tuple = tuple(temp_list)
print("Updated Tuple after Appending 4:", updated_tuple)

additional_elements = (5, 6)
updated_tuple = updated_tuple + additional_elements
print("Updated Tuple after Adding (5, 6):", updated_tuple)


