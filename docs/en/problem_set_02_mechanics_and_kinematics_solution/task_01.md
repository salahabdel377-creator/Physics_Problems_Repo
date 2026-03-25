
# Task 1: Solution

## Problem 1 – Uniform and uniformly accelerated motion

1. **Velocity and Acceleration:**
   The velocity is the first derivative of position with respect to time, and acceleration is the second derivative.
   
   $v(t) = \frac{dx}{dt} = v_0 + at$
   
   $a(t) = \frac{dv}{dt} = a$

2. **Calculations for given parameters ($x_0=0$, $v_0=5$ m/s, $a=-2$ m/s²):**
   * **Stopping time:** The body stops when $v(t) = 0$.
     
     $5 - 2t = 0 \implies t = 2.5 \text{ s}$
     
   * **Maximum velocity:** Since the acceleration is negative, the velocity is strictly decreasing for $t \ge 0$. The maximum velocity occurs at the start ($t=0$).
     
     $v_{max} = 5 \text{ m/s}$
     
   * **Maximum displacement:** Because the object stops and reverses direction at $t=2.5$ s, the maximum positive displacement occurs exactly at the stopping time.
     
     $x(2.5) = 0 + 5(2.5) + \frac{1}{2}(-2)(2.5)^2 = 12.5 - 6.25 = 6.25 \text{ m}$

3. **Visualization (Python/Matplotlib snippet):**
   ```python
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
   plt.show()
   ```

