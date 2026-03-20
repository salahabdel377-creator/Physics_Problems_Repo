
---

## Problem 1 – Vectors and linear transformations

**Given:**
$$
\vec{a} = (2,-1,3), \qquad \vec{b} = (1,4,-2)
$$

**1. Lengths of the vectors:**
The length of a vector $\vec{v} = (x,y,z)$ is $|\vec{v}| = \sqrt{x^2 + y^2 + z^2}$.
* $|\vec{a}| = \sqrt{2^2 + (-1)^2 + 3^2} = \sqrt{4 + 1 + 9} = \sqrt{14}$
* $|\vec{b}| = \sqrt{1^2 + 4^2 + (-2)^2} = \sqrt{1 + 16 + 4} = \sqrt{21}$

**2. Normalized vector $\hat{a}$:**
$$
\hat{a} = \frac{\vec{a}}{|\vec{a}|} = \frac{1}{\sqrt{14}}(2, -1, 3) = \left(\frac{2}{\sqrt{14}}, \frac{-1}{\sqrt{14}}, \frac{3}{\sqrt{14}}\right)
$$

**3. Dot product and angle:**
* $\vec{a} \cdot \vec{b} = (2)(1) + (-1)(4) + (3)(-2) = 2 - 4 - 6 = -8$
* Angle $\theta$: Using the formula $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$, we get:
    $$
    \cos\theta = \frac{-8}{\sqrt{14}\sqrt{21}} = \frac{-8}{\sqrt{294}}
    $$
    $$
    \theta = \arccos\left(\frac{-8}{\sqrt{294}}\right)
    $$

**4. Cross product and parallelogram area:**
$$
\vec{a} \times \vec{b} = 
\begin{vmatrix} 
\hat{i} & \hat{j} & \hat{k} \\ 
2 & -1 & 3 \\ 
1 & 4 & -2 
\end{vmatrix}
$$
* $\hat{i}$ component: $(-1)(-2) - (3)(4) = 2 - 12 = -10$
* $\hat{j}$ component: $-((2)(-2) - (3)(1)) = -(-4 - 3) = 7$
* $\hat{k}$ component: $(2)(4) - (-1)(1) = 8 + 1 = 9$
$$
\vec{a} \times \vec{b} = (-10, 7, 9)
$$
* Area is the magnitude of the cross product:
    $$
    \text{Area} = |\vec{a} \times \vec{b}| = \sqrt{(-10)^2 + 7^2 + 9^2} = \sqrt{100 + 49 + 81} = \sqrt{230}
    $$

**5. Matrix transformations:**
Given $A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix}$

* **Calculate $A\vec{a}$:**
    $$
    A\vec{a} = 
    \begin{pmatrix} 
    (2)(2) + (1)(-1) + (0)(3) \\ 
    (0)(2) + (1)(-1) + (-1)(3) \\ 
    (1)(2) + (0)(-1) + (1)(3) 
    \end{pmatrix}
    = 
    \begin{pmatrix} 
    4 - 1 + 0 \\ 
    0 - 1 - 3 \\ 
    2 + 0 + 3 
    \end{pmatrix}
    = 
    \begin{pmatrix} 3 \\ -4 \\ 5 \end{pmatrix}
    $$
* **Calculate $\det A$:** Expanding along the first row:
    $$
    \det A = 2((1)(1) - (-1)(0)) - 1((0)(1) - (-1)(1)) + 0 = 2(1) - 1(1) = 1
    $$
* **Orientation check:** Since $\det A = 1$, which is strictly greater than 0, the transformation preserves the orientation of the space.

---

## Problem 2 – Parametric trajectory, velocity, and acceleration

**Given:** $\vec{r}(t) = (t^2, \sin t, 5)$

**1. Velocity:**
$$
\vec{v}(t) = \frac{d}{dt}(t^2, \sin t, 5) = (2t, \cos t, 0)
$$

**2. Acceleration:**
$$
\vec{a}(t) = \frac{d}{dt}(2t, \cos t, 0) = (2, -\sin t, 0)
$$

**3. Evaluate $|\vec{v}(1)|$:**
$$
\vec{v}(1) = (2(1), \cos 1, 0) = (2, \cos 1, 0)
$$
$$
|\vec{v}(1)| = \sqrt{2^2 + (\cos 1)^2 + 0^2} = \sqrt{4 + \cos^2 1}
$$

**4. Dot product $\vec{v} \cdot \vec{a}$:**
$$
\vec{v} \cdot \vec{a} = (2t)(2) + (\cos t)(-\sin t) + (0)(0) = 4t - \sin t \cos t
$$

**5. Cross product $\vec{v} \times \vec{a}$:**
$$
\vec{v} \times \vec{a} = 
\begin{vmatrix} 
\hat{i} & \hat{j} & \hat{k} \\ 
2t & \cos t & 0 \\ 
2 & -\sin t & 0 
\end{vmatrix}
$$
* $\hat{i}$: $(\cos t)(0) - (0)(-\sin t) = 0$
* $\hat{j}$: $-((2t)(0) - (0)(2)) = 0$
* $\hat{k}$: $(2t)(-\sin t) - (\cos t)(2) = -2t\sin t - 2\cos t$
$$
\vec{v} \times \vec{a} = (0, 0, -2t\sin t - 2\cos t)
$$
*(Note on plotting: This represents a parabola mapped onto a sine wave, constrained entirely to the horizontal plane $z = 5$.)*

---

## Problem 3 – Integration of motion

### A) Given velocity
$\vec{v}(t) = (2t, 3, -e^{-t})$ and $\vec{r}(0) = (0, 1, 2)$

**1. Determine $\vec{r}(t)$:**
$$
\int_0^t \vec{v}(\tau) \, d\tau = \left[ \tau^2, 3\tau, e^{-\tau} \right]_0^t = (t^2, 3t, e^{-t} - 1)
$$
$$
\vec{r}(t) = (0, 1, 2) + (t^2, 3t, e^{-t} - 1) = (t^2, 1 + 3t, 1 + e^{-t})
$$

**2. Determine $\vec{a}(t)$:**
$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d}{dt}(2t, 3, -e^{-t}) = (2, 0, e^{-t})
$$

### B) Given acceleration
$\vec{a}(t) = (4, -\sin t, 0)$, $\vec{v}(0) = (1, 0, 2)$, $\vec{r}(0) = (0, 0, 0)$

**1. Determine $\vec{v}(t)$:**
$$
\int_0^t \vec{a}(\tau) \, d\tau = \left[ 4\tau, \cos\tau, 0 \right]_0^t = (4t, \cos t - 1, 0)
$$
$$
\vec{v}(t) = (1, 0, 2) + (4t, \cos t - 1, 0) = (1 + 4t, \cos t - 1, 2)
$$

**2. Determine $\vec{r}(t)$:**
$$
\int_0^t \vec{v}(\tau) \, d\tau = \left[ \tau + 2\tau^2, \sin\tau - \tau, 2\tau \right]_0^t = (t + 2t^2, \sin t - t, 2t)
$$
$$
\vec{r}(t) = (0, 0, 0) + (t + 2t^2, \sin t - t, 2t) = (t + 2t^2, \sin t - t, 2t)
$$

---

## Problem 4 – Geometry of parametric curves

**A) $x = R\cos t, \quad y = R\sin t$**
1.  **Eliminate:** $x^2 + y^2 = R^2\cos^2 t + R^2\sin^2 t = R^2$.
2.  **Type:** Circle of radius $R$.
3.  **Derivatives:** $\vec{v}(t) = (-R\sin t, R\cos t)$, $\vec{a}(t) = (-R\cos t, -R\sin t)$.
4.  **Magnitudes:** $|\vec{v}| = \sqrt{R^2\sin^2 t + R^2\cos^2 t} = R$ (Constant). $|\vec{a}| = R$ (Constant).

**B) $x = a\cos t, \quad y = b\sin t$**
1.  **Eliminate:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \cos^2 t + \sin^2 t = 1$.
2.  **Type:** Ellipse.
3.  **Derivatives:** $\vec{v}(t) = (-a\sin t, b\cos t)$, $\vec{a}(t) = (-a\cos t, -b\sin t)$.
4.  **Magnitudes:** $|\vec{v}| = \sqrt{a^2\sin^2 t + b^2\cos^2 t}$ (Not constant unless $a=b$). $|\vec{a}|$ is also not constant.

**C) $x = t, \quad y = t^2$**
1.  **Eliminate:** $y = x^2$.
2.  **Type:** Parabola.
3.  **Derivatives:** $\vec{v}(t) = (1, 2t)$, $\vec{a}(t) = (0, 2)$.
4.  **Magnitudes:** $|\vec{v}| = \sqrt{1 + 4t^2}$ (Not constant). $|\vec{a}| = 2$ (Constant).

**D) $x = \cosh t, \quad y = \sinh t$**
1.  **Eliminate:** $x^2 - y^2 = \cosh^2 t - \sinh^2 t = 1$.
2.  **Type:** Hyperbola (right branch, since $\cosh t > 0$).
3.  **Derivatives:** $\vec{v}(t) = (\sinh t, \cosh t)$, $\vec{a}(t) = (\cosh t, \sinh t)$.
4.  **Magnitudes:** $|\vec{v}| = \sqrt{\sinh^2 t + \cosh^2 t} = \sqrt{\cosh(2t)}$ (Not constant). $|\vec{a}|$ is also not constant.

---

## Problem 5 – Trajectory curvature and normal acceleration

**1. Velocity and Acceleration:**
$$
\vec{v}(t) = (-a\sin t, b\cos t)
$$
$$
\vec{a}(t) = (-a\cos t, -b\sin t)
$$

**2. Unit tangent vector:**
$$
\hat{T}(t) = \frac{\vec{v}(t)}{|\vec{v}(t)|} = \frac{1}{\sqrt{a^2\sin^2 t + b^2\cos^2 t}}(-a\sin t, b\cos t)
$$

**3. Normal Acceleration magnitude:**
The quickest way to find normal acceleration $a_n$ is using the cross product: $a_n = \frac{|\vec{v} \times \vec{a}|}{|\vec{v}|}$.
* $\vec{v} \times \vec{a} = (-a\sin t)(-b\sin t) - (b\cos t)(-a\cos t) = ab\sin^2 t + ab\cos^2 t = ab$
$$
a_n(t) = \frac{ab}{\sqrt{a^2\sin^2 t + b^2\cos^2 t}}
$$

**4. Radius of curvature at $t=0$:**
At $t=0$, velocity magnitude $v(0) = \sqrt{a^2(0) + b^2(1)} = b$.
Normal acceleration at $t=0$ is $a_n(0) = \frac{ab}{\sqrt{0 + b^2}} = \frac{ab}{b} = a$.
Using $a_n = \frac{v^2}{R}$, solve for $R$:
$$
R = \frac{v^2}{a_n} = \frac{b^2}{a}
$$

**5. Comparison with a circle ($a=b$):**
If $a=b$, then $R = \frac{a^2}{a} = a$. This confirms the radius of curvature for a circle is just its radius.

### Physical Interpretation Answers:
* **Does greater curvature imply greater normal acceleration?** Yes. Curvature is $\kappa = \frac{1}{R}$. Since $a_n = v^2\kappa$, for a given velocity, a higher curvature directly yields a greater normal acceleration.
* **Where is it more curved?** The ellipse is most "curved" (smallest $R$, highest $\kappa$) at the ends of the major semi-axis.
* **Why does it change direction?** Acceleration is the rate of change of velocity. The tangential component ($a_t$) acts strictly along the velocity vector, changing its speed (magnitude). The normal component ($a_n$) acts perpendicular to velocity; it does no work and cannot change the speed, so its sole physical effect is continuously deflecting the velocity vector, thereby changing the direction of motion.

---

## Problem 6 – Curve length and numerical integration

1.  **Velocity vector:** $\vec{v}(t) = (1, 2t)$
2.  **Magnitude:** $|\vec{v}(t)| = \sqrt{1^2 + (2t)^2} = \sqrt{1 + 4t^2}$
3.  **Arc length integral:**
    $$
    s = \int_0^1 \sqrt{1 + 4t^2} \, dt
    $$
4.  **Analytical Calculation:** Using trigonometric substitution ($2t = \tan u$, $2dt = \sec^2 u \, du$), this integral evaluates to:
    $$
    s = \frac{1}{4} \left[ 2t\sqrt{1+4t^2} + \ln\left(2t + \sqrt{1+4t^2}\right) \right]_0^1 = \frac{1}{4} \left( 2\sqrt{5} + \ln(2 + \sqrt{5}) \right)
    $$
    This is approximately $1.4789$. 

*(Numerical integration via HTML/JS is addressed at the bottom).*

---

## Problem 7 – Work of a force along a trajectory

**Given:** $\vec{F}(x,y) = (y, 2x)$, and trajectory $x = t, y = t^2$ for $t \in [0,1]$.

1.  **Velocity vector:** $\vec{v}(t) = \frac{d\vec{r}}{dt} = (1, 2t)$
2.  **Work calculation:** Substitute $x$ and $y$ into $\vec{F}$ to get $\vec{F}(t) = (t^2, 2t)$.
    The differential displacement is $d\vec{r} = \vec{v}(t)dt = (1, 2t)dt$.
    $$
    W = \int_0^1 \vec{F}(t) \cdot \vec{v}(t) \, dt = \int_0^1 (t^2(1) + 2t(2t)) \, dt = \int_0^1 (t^2 + 4t^2) \, dt = \int_0^1 5t^2 \, dt
    $$
    $$
    W = \left[ \frac{5t^3}{3} \right]_0^1 = \frac{5}{3}
    $$
3.  **Riemann sum setup:** $\lim_{N \to \infty} \sum_{i=1}^N 5t_i^2 \Delta t$.

---

## Problem 8 – First-order differential equation

**1. Solve the equation:**
$$
\frac{dy}{dt} = -ky
$$
Separate variables and integrate:
$$
\int \frac{1}{y} \, dy = \int -k \, dt \implies \ln|y| = -kt + C \implies y(t) = e^{-kt+C} = Ae^{-kt}
$$
Applying the initial condition $y(0)$, we get $A = y(0)$, so the analytical solution is:
$$
y(t) = y(0)e^{-kt}
$$

---

## Problem 9 – Harmonic oscillator

**1. General solution:**
$$
\frac{d^2 x}{dt^2} + \omega^2 x = 0
$$
The characteristic equation is $r^2 + \omega^2 = 0 \implies r = \pm i\omega$. 
The general solution is:
$$
x(t) = C_1\cos(\omega t) + C_2\sin(\omega t)
$$

**2. Solve for initial conditions $x(0) = x_0$ and $v(0) = v_0$:**
At $t=0$, $x(0) = C_1\cos(0) + C_2\sin(0) = C_1 \implies C_1 = x_0$.
Take the derivative: $x'(t) = -x_0\omega\sin(\omega t) + C_2\omega\cos(\omega t)$.
At $t=0$, $x'(0) = C_2\omega\cos(0) = C_2\omega \implies C_2 = \frac{v_0}{\omega}$.
$$
x(t) = x_0\cos(\omega t) + \frac{v_0}{\omega}\sin(\omega t)
$$

---

## Problem 10 – Angular momentum in circular motion

**Given:** $\vec{r}(t) = (R\cos(\omega t), R\sin(\omega t), 0)$

**1. Velocity:**
$$
\vec{v}(t) = (-R\omega\sin(\omega t), R\omega\cos(\omega t), 0)
$$

**2. Angular momentum:**
$$
\vec{L}(t) = m(\vec{r}(t) \times \vec{v}(t)) = m
\begin{vmatrix} 
\hat{i} & \hat{j} & \hat{k} \\ 
R\cos(\omega t) & R\sin(\omega t) & 0 \\ 
-R\omega\sin(\omega t) & R\omega\cos(\omega t) & 0 
\end{vmatrix}
$$
The $\hat{i}$ and $\hat{j}$ components are 0. The $\hat{k}$ component is:
$$
\vec{L}(t) = m\left( (R\cos(\omega t))(R\omega\cos(\omega t)) - (R\sin(\omega t))(-R\omega\sin(\omega t)) \right)\hat{k}
$$
$$
\vec{L}(t) = m(R^2\omega\cos^2(\omega t) + R^2\omega\sin^2(\omega t))\hat{k} = mR^2\omega(\cos^2(\omega t) + \sin^2(\omega t))\hat{k} = mR^2\omega\hat{k}
$$

**3. Magnitude and orthogonality:**
$|\vec{L}| = mR^2\omega$, which contains only constants, so it is constant. The vector has only a $\hat{k}$ component, meaning it strictly points along the z-axis, perpendicular to the $xy$ plane of motion.

**4. Interpretation:**
Following the right-hand rule, if you curl your fingers in the direction of the counter-clockwise circular motion (from x to y), your thumb points straight up along the positive z-axis, which is the direction of $\vec{L}$.

**5. Constant centripetal force and torque:**
Centripetal force is $\vec{F} = -m\omega^2\vec{r}$ (it points toward the origin).
Torque is $\vec{\tau} = \vec{r} \times \vec{F} = \vec{r} \times (-m\omega^2\vec{r})$.
Since the cross product of any vector with a scalar multiple of itself is strictly 0 ($\vec{r} \times \vec{r} = 0$), the torque $\vec{\tau} = 0$. 
Verify: $\frac{d\vec{L}}{dt} = \frac{d}{dt}(mR^2\omega\hat{k}) = 0$. Therefore, $\vec{\tau} = \frac{d\vec{L}}{dt} = 0$, confirming the conservation of angular momentum in uniform circular motion.

---

### **Interactive Visualization Components (Problems 6-9)**

