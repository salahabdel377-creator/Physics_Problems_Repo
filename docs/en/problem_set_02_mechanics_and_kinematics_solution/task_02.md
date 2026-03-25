## Problem 2 – Projectile motion

* **Equations of motion:**
  Integrating the constant gravitational acceleration $\vec{a} = (0, -g)$ yields:
  $$
  x(t) = v_0 \cos(\alpha) t
  $$
  $$
  y(t) = v_0 \sin(\alpha) t - \frac{1}{2}gt^2
  $$

* **Time of flight ($T$):** Set $y(T) = 0$ (ignoring $t=0$).
  $$
  v_0 \sin(\alpha) T - \frac{1}{2}gT^2 = 0 \implies T = \frac{2v_0 \sin(\alpha)}{g}
  $$

* **Maximum height ($H$):**
  Occurs at $t = T/2 = \frac{v_0 \sin(\alpha)}{g}$. Substitute this into $y(t)$:
  $$
  H = v_0 \sin(\alpha) \left( \frac{v_0 \sin(\alpha)}{g} \right) - \frac{1}{2}g \left( \frac{v_0 \sin(\alpha)}{g} \right)^2 = \frac{v_0^2 \sin^2(\alpha)}{2g}
  $$

* **Range ($R$):**
  Substitute $T$ into $x(t)$:
  $$
  R = x(T) = v_0 \cos(\alpha) \frac{2v_0 \sin(\alpha)}{g} = \frac{v_0^2 \sin(2\alpha)}{g}
  $$

* **Maximum range:**
  $R$ is maximized when $\sin(2\alpha) = 1$, which occurs at $2\alpha = 90^\circ$, so $\alpha = 45^\circ$.

---