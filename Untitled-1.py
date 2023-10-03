from matplotlib import pyplot as plt

days= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature=[36.6,37,5,6,7,8,9,1,2,3,55,66,77,88,99]
plt.plot(days,temperature)
plt.xlabel("Days")
plt.ylabel("Temp")
plt.title("Lahore Temperature")
plt.show()