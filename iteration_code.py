from matplotlib import pyplot as plt

y= []
x = []
base = 5
iterations = 250

for i in range(1,iterations):

	x.append(i)
	d = float(i)
	
	if d%base != 0.0:
		y.append(0)
		
	elif d%base == 0.0:
		k=0
		while d%base==0.0:
			
			d = d/float(base)
			k = k+1
		y.append(k)


plt.xlabel("Iteration")
plt.ylabel("No. of full divisions")
plt.plot(x,y)
plt.show()	
