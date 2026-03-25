import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 500)
x = 2 * t**2
y = 3 * t**3

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', lw=2, label='Trajectory')
plt.title('Trajectory: Semicubical Parabola')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.grid(True, linestyle='--')
plt.legend()
plt.savefig('semicubical_parabola.png')
print("Plot saved as semicubical_parabola.png")