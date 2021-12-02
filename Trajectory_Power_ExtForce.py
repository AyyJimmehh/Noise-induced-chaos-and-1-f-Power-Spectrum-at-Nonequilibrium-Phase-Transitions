import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def f(s, t):
    phi = s[0]
    psi = s[1]
    dphidt = (-1 * phi * psi * psi) + 2.14*math.sin(2*math.pi*0.12*t)
    dpsidt = (-1 * phi * phi * psi) + 2 * phi
    return [dphidt, dpsidt]


t = np.arange(0, 100, 0.01)

s0 = [5, 5]
s = odeint(f, s0, t)

psi = np.array(s[:, 1])
phi = np.array(s[:, 0])
plt.plot(psi, phi, linewidth=2.0)

plt.xlabel("psi")
plt.ylabel("phi")
#plt.show()

fourier = np.fft.rfft(phi)
abs = np.abs(fourier)
power = np.square(abs)
freq = np.linspace(0, 15, len(power))
plt.plot(freq, power)
plt.ylim([100, 1000000])
plt.xlim([0.1, 1])
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Frequency")
plt.ylabel("S")
#plt.show()
