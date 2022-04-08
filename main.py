from ci_build import CIBuild

import simpy
import csv

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

f = open("data.csv", "w")
f.write("Pass Rate,Rebases,Wall Clock Time\n")
f.close()

def run_sim():
  for _ in range(1000):
    env = simpy.Environment()

    build = CIBuild(env)
    build.run()

    env.run()
    build.stats(env.now)

run_sim()


input_file = csv.DictReader(open("data.csv", "r"))

xdata = []
ydata = []
zdata = []

for row in input_file:
  xdata.append(float(row['Pass Rate']))
  ydata.append(float(row['Rebases']))
  zdata.append(float(row['Wall Clock Time']))

fig = plt.figure()
ax = plt.axes(projection='3d')

# # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')

# # Data for three-dimensional scattered points
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# print(xdata)
ax.scatter3D(xdata, ydata, zdata);

plt.show()