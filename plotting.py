#import numpy as np
#import scipy as sp
from matplotlib import pyplot as plt

x = range(10)
y = [w*w for w in x]
plt.plot(x, y, 'o-')
#plt.savefig('plot.pdf', format='pdf')
plt.show(block = False)
plt.clf()

n_bins = 30
h = range(n_bins)
for i in range(n_bins/2):
    h += [ w+i for w in range(n_bins-2*i)]
n, bins, patches = plt.hist(h, n_bins*3)
#plt.plot(bins, n, 'o-')
#plt.savefig('hist.pdf', format='pdf')
plt.show()
plt.clf()

plt.pie(y)
#plt.savefig('pie.pdf', format='pdf')
plt.show()
plt.clf()

