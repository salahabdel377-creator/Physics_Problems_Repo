# Problem 3 – Elimination of Time and Interpretation of Acceleration

Given the parametric equations of motion:
$$x(t) = 2t^2$$
$$y(t) = 3t^3$$

---

## 1. Elimination of the parameter $t$

To find the trajectory $y(x)$, we isolate $t$ from the $x$ equation and substitute it into the $y$ equation:

1. From $x = 2t^2$, we have $t^2 = \frac{x}{2} \implies t = \sqrt{\frac{x}{2}}$ (for $t \ge 0$).
2. Substitute $t$ into $y = 3t^3$:
   $$y = 3 \left( \sqrt{\frac{x}{2}} \right)^3$$
   $$y = \frac{3}{2\sqrt{2}} x^{3/2}$$

The trajectory is a **semicubical parabola**.

---

## 2. Velocity and Acceleration

### Velocity Vector $\vec{v}(t)$
The velocity is the first derivative of position:
$$\vec{v}(t) = \left( \frac{dx}{dt}, \frac{dy}{dt} \right) = (4t, 9t^2)$$

**Magnitude (Speed):**
$$|\vec{v}(t)| = \sqrt{(4t)^2 + (9t^2)^2} = \sqrt{16t^2 + 81t^4} = |t|\sqrt{16 + 81t^2}$$

### Acceleration Vector $\vec{a}(t)$
The acceleration is the derivative of velocity:
$$\vec{a}(t) = \left( \frac{dv_x}{dt}, \frac{dv_y}{dt} \right) = (4, 18t)$$

**Magnitude:**
$$|\vec{a}(t)| = \sqrt{4^2 + (18t)^2} = \sqrt{16 + 324t^2}$$

---

## 3. Interpretation

**Is the acceleration constant?**
**No.** While the $x$-component ($a_x = 4$) is constant, the $y$-component ($a_y = 18t$) depends on time. Therefore, the vector $\vec{a}(t)$ changes in both magnitude and direction over time.

---

## 4. Visualization

To visualize the trajectory, you can use the following Python script:

```python
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
plt.show()
