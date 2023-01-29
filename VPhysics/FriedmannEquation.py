import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#(da/dt/a)^2 = H0^2*[(8.4*10^-5)/a^4 + 0.31/a^3  +  0.69 + (sum(omegas)-1)/a^2 )
H0=7.2e-11
omegaR = 8.4*10**-5
omegaM = 0.31
omegaA = 0.69

def model(a,t):
    RHS = H0**2*(omegaR/a**2 + omegaM/a + omegaA*a**2 +(omegaM+omegaA+omegaR-1) )
    dadt = np.sqrt(RHS)
    print(RHS, a**2, omegaR, omegaM, omegaA, omegaM+omegaA+omegaR-1)
    return dadt


y0 = 1


t = np.linspace(0,-10**14,2*10**7)


a = odeint(model,y0,t)

