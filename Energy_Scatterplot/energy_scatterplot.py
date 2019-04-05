import matplotlib.pyplot as plt
import csv
import numpy as np

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts) -- DONE
- Includes ONLY data for K-12 Schools. (3pts) -- DONE
- Labelled x and y axis and appropriate title (3pt) -- DONE
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts) -- DONE
- Label Francis W. Parker. (3pts) -- DONE
- Create a best fit line for schools shown. (5pts) -- DONE
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts) -- DONE

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

with open('Chicago_Energy_Benchmarking.csv') as f:
    reader = csv.reader(f, delimiter=",")
    data = list(reader)

headers = data.pop(0)
print(headers)
only_schools = []
for i in range(len(data)):
    if data[i][6] == "K-12 School":
        only_schools.append(data[i])
print(only_schools)
sqft = []
ghg = []
school_names = []
for i in range(len(only_schools)):
    try:
        current_sqft = float(only_schools[i][7])
        current_ghg = float(only_schools[i][20])
        sqft.append(current_sqft)
        ghg.append(current_ghg)
        school_names.append(only_schools[i][2])
    except ValueError:
        print("This ain't happening for", str(only_schools[i][2]) + ".")

plt.figure(1, figsize=(10,6))
plt.title("Square Footage by Greenhouse Gasses")
plt.xlabel("Square Footage")
plt.ylabel("Greenhouse Gasses")
plt.scatter(sqft, ghg, alpha=.3)
plt.annotate("Francis W Parker", xy=(float(only_schools[1174][7]), float(only_schools[1174][20])))
plt.scatter(float(only_schools[1174][7]), float(only_schools[1174][20]), color="blue")
only_schools_that_have_ghg = []


# This doesn't work
for schools in only_schools:
    if not len(schools[20]) == 0 and not len(schools[21]) == 0:
        only_schools_that_have_ghg.append(schools)

only_schools_that_have_ghg.sort(key=lambda x: float(x[21]))
print(only_schools_that_have_ghg, end="\n"*2)

for i in range(3):
    plt.annotate(only_schools_that_have_ghg[i][2], xy=(float(only_schools_that_have_ghg[i][7]), float(only_schools_that_have_ghg[i][20])), xytext=(float(only_schools_that_have_ghg[i][7]), int((i + 4)*1000)), arrowprops={"width":1})
    plt.scatter(float(only_schools_that_have_ghg[i][7]), float(only_schools_that_have_ghg[i][20]), color="green")
for i in range(-3, -0, 1):
    plt.annotate(only_schools_that_have_ghg[i][2], xy=(float(only_schools_that_have_ghg[i][7]), float(only_schools_that_have_ghg[i][20])))
    plt.scatter(float(only_schools_that_have_ghg[i][7]), float(only_schools_that_have_ghg[i][20]), color="red")

sqft_o_schools = []
ghg_o_schools = []
for items in only_schools_that_have_ghg:
    sqft_o_schools.append(float(items[7]))
    ghg_o_schools.append(float(items[20]))
print(sqft_o_schools)
m, b = np.polyfit(sqft_o_schools, ghg_o_schools, deg=1)
print(m)
print(b)
fit_x = [0, 700000]
fit_y = [b, m*700000 + b]

plt.plot(fit_x, fit_y)

plt.show()


