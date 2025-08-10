# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

list1 = [1,2,3,4,5,6,7,8,9,10]
extrat_list = list1[0:5]
reversed_list = []
i = len(extrat_list)
while i >= 0:
    reversed_list.append(extrat_list[i-1])
    i = i - 1

print("Original list:",list1)
print("Extract first five elements:",extrat_list)
print("Reverse extract elements:",reversed_list)

