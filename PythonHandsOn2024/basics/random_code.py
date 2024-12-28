daily_temperatures = [68, 70, 75, 72, 68, 71, 69]
average = sum(daily_temperatures) / len(daily_temperatures)
print(average)

print(max(daily_temperatures))
print(min(daily_temperatures))

average = 0.0 
tempSum = 0
for temp in daily_temperatures:
    tempSum = tempSum + temp

average = tempSum / len(daily_temperatures)
print(average)
daily_temperatures.sort()
print(daily_temperatures[-1])
print(daily_temperatures[0])