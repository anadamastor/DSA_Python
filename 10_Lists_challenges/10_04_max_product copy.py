# find max product in not sorted array 

arr = [1,2,3,4,5]

def max_product(my_array):
    max_product = 0
    for i in range(len(my_array)):
        for j in range (i+1,len(my_array)):
            current_product = my_array[i] * my_array[j]
            if current_product > max_product: # this is where the magic happens
                max_product = current_product
                pairs = str(my_array[i]) + str(my_array[j])
    return(max_product, pairs)

print(max_product(arr))

# Another solution
sorted_array = sorted(arr)
print(sorted_array[-1]*sorted_array[-2])