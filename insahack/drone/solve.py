import matplotlib
import matplotlib.pyplot as plt

x=0
y=0
z=0
final_X=[]
final_Y=[]
final_Z=[]

with open('sensor.tsv', 'r') as f:
	lines = f.readlines()
	t = []
	for l in lines:
		x+=float(l.split(' ')[0])
		y+=float(l.split(' ')[1])
		z+=float(l.split(' ')[2])
		final_X.append(x)
		final_Y.append(y)
		final_Z.append(z)

ax = plt.plot(final_X, final_Y)
plt.axis('equal')
plt.show()
