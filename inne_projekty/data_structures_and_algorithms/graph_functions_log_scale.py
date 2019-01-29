import pylab as plt
from math import log

samples = []
linear = []
logar = []
quadratic = []
cubic = []
exponential = []

for n in range(1, 30):
    samples.append(n)
    linear.append(n*8)
    #print(4*n*log(n))
    logar.append(4*n*log(n))
    quadratic.append((n**2)*2)
    cubic.append(n**3)
    exponential.append(2**n)
    

plt.figure('plots')
plt.clf()
plt.xscale('log')
plt.yscale('log')


plt.plot(samples, linear, label='linear')
plt.plot(samples, logar, label='logarythmic')
plt.plot(samples, quadratic, label='quadratic')
plt.plot(samples, cubic, label='cubic')
plt.plot(samples, exponential, label='exponential')
plt.legend()
plt.title('Linear vs. Logarythmic vs. Quadratic vs. Cubic')
plt.show()