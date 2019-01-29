import pylab as plt
import math

samples = []
logar = []
quadratic = []
for i in range(1, 30):
    samples.append(i)
    quadratic.append(2*i**2)
    logar.append(8*i*math.log2(i))

plt.figure('comp_func')
plt.clf()
#plt.xscale('log')
#plt.yscale('log')
plt.plot(samples, quadratic, label= 'quadratic')
plt.plot(samples, logar, label='logaritmic')
plt.legend()
plt.title('Comparing two functions')
plt.show()