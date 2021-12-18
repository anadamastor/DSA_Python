# Calculate average temperature

num_days = int(input("How many days? "))
total = 0
temp = []

for i in range(num_days):
  next_day = int(input("Day " + str(i) +" high temperature: "))
  temp.append(next_day)
  total += temp[i]

avg = round(total/num_days,2)
print("Average = " + str(avg))

#check which days are above
above = 0 
for i in temp:
  if i > avg:
    above +=1
print(str(above) + " are above average")