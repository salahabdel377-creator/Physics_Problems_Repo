import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)
x = 5*t - t**2
v = 5 - 2*t
a = -np.full_like(t, 2)

plt.plot(t, x, label='Position x(t)')
plt.plot(t, v, label='Velocity v(t)')
plt.plot(t, a, label='Acceleration a(t)')
plt.legend()
plt.xlabel('Time (s)')
plt.savefig('kinematics_plot.png')
print("Plot saved as kinematics_plot.png")