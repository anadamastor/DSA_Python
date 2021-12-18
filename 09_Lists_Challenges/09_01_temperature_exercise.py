# Calculate average temperature

num_days = int(input("How many days? "))
total = 0

for i in range(1, num_days +1):
  next_day = int(input("day" + str(i) +" high temperature: "))
  total += next_day

avg = round(total/num_days,2)
print("Average = " +str(avg))

# Calculate average temperature with arrays
