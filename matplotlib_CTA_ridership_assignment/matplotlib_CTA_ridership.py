import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as tkr

# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s


def error_message():
    print("Error")


with open('CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f)  # make a reader object to pull in the data
    data = list(reader)  # make the reader into a list

header = data.pop(0)
print(header)

try:
    rider_numbers = [int(x[4]) for x in data]
except ValueError:
    error_message()
try:
    year = [int(x[0]) for x in data]
except ValueError:
    error_message()
try:
    bus_rider_numbers = [int(x[1]) for x in data]
except ValueError:
    error_message()
try:
    rail_rider_numbers = [int(x[3]) for x in data]
except ValueError:
    error_message()

plt.figure(1)
# 1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
rider_numbers_last_10_years = rider_numbers[-10:]
last_10_years = year[-10:]
plt.plot([x for x in range(10)], rider_numbers_last_10_years, label="Total Public Transport Usage")
plt.xticks([x for x in range(10)], [str(x) for x in last_10_years])

# 2  Plot bus usage for the same years as a second line on your graph. (5pts)

bus_rider_numbers_last_10_years = bus_rider_numbers[-10:]
plt.plot([x for x in range(10)], bus_rider_numbers_last_10_years, label="Bus Riders")

# 3  Plot bus and rail usage together on a third line on your graph. (5pts)

rail_rider_numbers_last_10_years = rail_rider_numbers[-10:]
plt.plot([x for x in range(10)], rail_rider_numbers_last_10_years, label="Rail Riders")
bus_and_rail_riders_last_10_years = [x for x in rail_rider_numbers_last_10_years]
for i in range(10):
    bus_and_rail_riders_last_10_years[i] += bus_rider_numbers_last_10_years[i]
plt.plot([x for x in range(10)], bus_and_rail_riders_last_10_years, label="Bus Riders + Rail Riders")

# 4  Add a title and label your axes. (5pts)

plt.xlabel("Year")
plt.ylabel("Ridership")
plt.title("Bus Stats")

# 5  Add a legend to show data represented by each of the three lines. (5pts)

plt.legend()

# 6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s).(3pts)

print("People are liking the buses a lot less and the rails a little more.")

plt.show()
