## Problem 3 – Elimination of time and interpretation of acceleration

* **Eliminate parameter $t$:**
  From $x(t) = 2t^2$, assuming $t \ge 0$, we get $t = \sqrt{x/2}$. Substituting into $y(t)$:
  $$
  y(x) = 3 \left(\sqrt{\frac{x}{2}}\right)^3 = \frac{3}{2\sqrt{2}} x^{3/2}
  $$
  *(The trajectory is a semi-cubical parabola).*

* **Velocity and Acceleration:**
  $$
  \vec{v}(t) = \left( \frac{dx}{dt}, \frac{dy}{dt} \right) = (4t, 9t^2)
  $$
  $$
  |\vec{v}(t)| = \sqrt{16t^2 + 81t^4} = t\sqrt{16 + 81t^2}
  $$
  $$
  \vec{a}(t) = \left( \frac{d^2x}{dt^2}, \frac{d^2y}{dt^2} \right) = (4, 18t)
  $$
  $$
  |\vec{a}(t)| = \sqrt{16 + 324t^2}
  $$

* **Is the acceleration constant?**
  No. While the $x$-component is constant, the $y$-component increases linearly with time.
