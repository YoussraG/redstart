import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.


    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & \cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Le centre de masse de la fusée est en $(x, y)$. Le vecteur unitaire pointant vers le **haut** de la fusée (dans la direction de son axe) est :
    $$
    \vec{u}_{axe} = \begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    $$

    Le point situé à une distance $\ell/6$ **au-dessus** du centre de masse est :
    $$
    (x, y) + \frac{\ell}{6}\begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    = \begin{bmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{bmatrix} = h
    $$

    **Conclusion géométrique :** $h$ est la position du point situé au **tiers supérieur** de la fusée (à $\ell/6$ au-dessus du centre, donc à $\ell/3$ du sommet). C'est le **centre de masse du tiers supérieur** de la fusée.

    Ce point a une propriété mathématique remarquable : ses dérivées successives s'expriment simplement en fonction des commandes, ce qui permet la linéarisation exacte.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Calcul de $\dot{h}$ (dérivée première)

    On part de la définition :
    $$
    h = \begin{bmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{bmatrix}
    $$

    On dérive chaque composante par rapport au temps (règle de dérivation en chaîne) :

    $$
    \dot{h}_x = \frac{d}{dt}\left[x - \frac{\ell}{6}\sin\theta\right] = \dot{x} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}
    $$

    $$
    \dot{h}_y = \frac{d}{dt}\left[y + \frac{\ell}{6}\cos\theta\right] = \dot{y} - \frac{\ell}{6}\sin\theta\cdot\dot{\theta}
    $$

    Donc :
    $$
    \boxed{\dot{h} = \begin{bmatrix} \dot{x} - (\ell/6)\cos\theta\,\dot{\theta} \\ \dot{y} - (\ell/6)\sin\theta\,\dot{\theta} \end{bmatrix}}
    $$

    -

    Calcul de $\ddot{h}$ (dérivée seconde)

    On dérive $\dot{h}$ une seconde fois. Pour la composante $x$ :

    $$
    \ddot{h}_x = \frac{d}{dt}\left[\dot{x} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}\right]
    = \ddot{x} - \frac{\ell}{6}\frac{d}{dt}\left[\cos\theta\cdot\dot{\theta}\right]
    $$

    En développant la dérivée du produit $\cos\theta\cdot\dot\theta$ :

    $$
    \frac{d}{dt}\left[\cos\theta\cdot\dot{\theta}\right] = -\sin\theta\cdot\dot{\theta}^2 + \cos\theta\cdot\ddot{\theta}
    $$

    Donc :
    $$
    \ddot{h}_x = \ddot{x} + \frac{\ell}{6}\sin\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\cos\theta\cdot\ddot{\theta}
    $$

    De même pour la composante $y$ :
    $$
    \ddot{h}_y = \ddot{y} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\sin\theta\cdot\ddot{\theta}
    $$


    Substitution des équations du mouvement

    On utilise maintenant les trois équations du mouvement de la fusée :

    $$
    M\ddot{x} = f_x = -f\sin(\theta+\phi)
    \qquad \Rightarrow \qquad
    \ddot{x} = \frac{f_x}{M}
    $$

    $$
    M\ddot{y} = f_y - Mg = f\cos(\theta+\phi) - Mg
    \qquad \Rightarrow \qquad
    \ddot{y} = \frac{f_y}{M} - g
    $$

    $$
    J\ddot{\theta} = -f\frac{\ell}{2}\sin\phi
    \qquad \Rightarrow \qquad
    \ddot{\theta} = -\frac{f\ell}{2J}\sin\phi
    $$

    En substituant dans $\ddot{h}_x$ et $\ddot{h}_y$ :

    $$
    \ddot{h}_x = \frac{f_x}{M} + \frac{\ell}{6}\sin\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\cos\theta\cdot\ddot{\theta}
    $$

    $$
    \ddot{h}_y = \frac{f_y}{M} - g - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\sin\theta\cdot\ddot{\theta}
    $$

     Substitution du système auxiliaire

    Le système auxiliaire donne la force $(f_x, f_y)$ sous la forme :

    $$
    \begin{bmatrix} f_x \\ f_y \end{bmatrix}
    = R\!\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix} z - M\ell\dot{\theta}^2/6 \\ M\ell v_2/(6z) \end{bmatrix}
    $$

    La matrice de rotation $R(\theta - \pi/2)$ vaut :

    $$
    R\!\left(\theta - \frac{\pi}{2}\right)
    = \begin{bmatrix} \cos(\theta-\pi/2) & -\sin(\theta-\pi/2) \\ \sin(\theta-\pi/2) & \cos(\theta-\pi/2) \end{bmatrix}
    = \begin{bmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{bmatrix}
    $$

    Donc :

    $$
    f_x = \sin\theta\cdot\left(z - \frac{M\ell\dot{\theta}^2}{6}\right) + \cos\theta\cdot\frac{M\ell v_2}{6z}
    $$

    $$
    f_y = -\cos\theta\cdot\left(z - \frac{M\ell\dot{\theta}^2}{6}\right) + \sin\theta\cdot\frac{M\ell v_2}{6z}
    $$

    Et la dynamique angulaire du système auxiliaire donne :

    $$
    \ddot{\theta} = \frac{M\ell v_2}{6Jz} \frac{\ell} {2} = \frac{v_2} {z}
    $$



    En substituant \(f_x\), \(f_y\) et \(\ddot{\theta}\) dans les expressions de
    \(\ddot h_x\) et \(\ddot h_y\), puis en développant, on obtient :

    \[
    \ddot h_x
    =
    \frac{\sin\theta}{M}
    \left(
    z - \frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \frac{\ell\cos\theta}{6z}v_2
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    -
    \frac{\ell}{6}\cos\theta
    \cdot
    \frac{v_2}{z}
    \]



    Simplification des termes en \(\dot\theta^2\)

    Les termes en \(\dot\theta^2\) se compensent exactement :

    \[
    \frac{\sin\theta}{M}
    \left(
    -\frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    =
    0
    \]

    En effet :

    \[
    -\frac{\ell}{6}\sin\theta\,\dot\theta^2
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    =
    0
    \]
     Simplification des termes en \(v_2\)

    Les termes contenant \(v_2\) se simplifient également :

    \[
    \frac{\ell\cos\theta}{6z}v_2
    -
    \frac{\ell\cos\theta}{6z}v_2
    =
    0
    \]



    Résultat pour \(\ddot h_x\)

    Il reste donc :

    \[
    \ddot h_x
    =
    \frac{z\sin\theta}{M}
    \]

    que l’on peut écrire sous la forme :

    \[
    \ddot h_x
    =
    -
    \frac{z}{M}
    (\sin\theta)
    \]

     Calcul analogue pour \(\ddot h_y\)

    De manière similaire, les mêmes simplifications apparaissent dans
    \(\ddot h_y\), avec en plus le terme gravitationnel \(-g\).

    On obtient :

    \[
    \ddot h_y
    =
    \frac{-z}{M}\cos\theta
    -
    g
    \]



    En regroupant les deux composantes :

    \[
    \boxed{
    \ddot h
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    }
    \]
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    On part de l’expression :

    \[
    \ddot{h}
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    \]

    On dérive cette expression par rapport au temps.

    Comme \(g\) est constant, sa dérivée est nulle :

    \[
    \frac{d}{dt}
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    0
    \end{bmatrix}
    \]

    Il reste donc à dériver :

    \[
    \frac{z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]

    On applique la règle du produit :

    \[
    \frac{d}{dt}
    \left(
    \frac{z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \right)
    =
    \frac{\dot z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    +
    \frac{z}{M}
    \frac{d}{dt}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]

    Or :

    \[
    \frac{d}{dt}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    =
    \dot\theta
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    \]

    Ainsi :

    \[
    \boxed{
    h^{(3)}
    =
    \frac{\dot z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    +
    \frac{z\dot\theta}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    }
    \]



    Calcul de \(h^{(4)}\)

    On dérive maintenant \(h^{(3)}\).

    On utilise la dynamique auxiliaire :

    \[
    \ddot z = v_1
    \]

    Après dérivation complète et regroupement des termes, on obtient :

    \[
    \boxed{
    h^{(4)}
    =
    \underbrace{
    \frac{v_1}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    }_{\text{terme en } v_1}
    +
    \underbrace{
    \frac{1}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    v_2
    }_{\text{terme en } v_2}
    +
    \underbrace{
    \alpha(\theta,\dot\theta,z,\dot z)
    }_{\text{terme autonome}}
    }
    \]

    où :

    \[
    \alpha(\theta,\dot\theta,z,\dot z)
    \]

    regroupe tous les termes ne dépendant pas des commandes
    \((v_1,v_2)\).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    D'après Q23, $h^{(4)}$ est affine en $v$ :
    $$
    h^{(4)} = \alpha(\theta, \dot\theta, z, \dot{z}) + E(\theta, z)\, v
    $$

    où $E(\theta, z) \in \mathbb{R}^{2\times2}$ est inversible tant que $z \neq 0$.

    $$E(\theta, z) = \begin{pmatrix} -\frac{1}{M} \sin\theta & -\frac{\ell \cos\theta}{6z} \\ \frac{\cos\theta}{M} & -\frac{\ell \sin\theta}{6z} \end{pmatrix}$$

    Il suffit donc de choisir :
    $$
    \boxed{v = E(\theta, z)^{-1}\left(u - \alpha(\theta, \dot\theta, z, \dot{z})\right)}
    $$

    on obtient donc :
    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Pour montrer que l'on peut calculer l'état $(x, y, \theta, z, \dots)$ à partir de $(h, \dot{h}, \ddot{h}, h^{(3)})$, on procède par étapes :

    **1. Calcul de $\theta$ et $z$ (à partir de $\ddot{h}$)**
    On part de l'accélération du point $h$ :


    $$\ddot{h} + g \vec{j} = \frac{z}{M} \begin{bmatrix} \sin \theta \\ -\cos \theta \end{bmatrix}$$


    En prenant la norme des deux côtés, on trouve la poussée auxiliaire $z$ :


    $$z = -M \left\| \ddot{h} + g \vec{j} \right\|$$


    *(On prend la valeur négative car l'énoncé impose $z < 0$).*
    L'angle $\theta$ est ensuite obtenu par l'orientation du vecteur accélération :


    $$\theta = \operatorname{atan2}(\ddot{h}_x, -(\ddot{h}_y + g))$$

    **2. Calcul de $\dot{\theta}$ et $\dot{z}$ (à partir de $h^{(3)}$)**
    On dérive l'expression de $\ddot{h}$. Comme on l'a vu précédemment, cela donne un système linéaire en $\dot{z}$ et $\dot{\theta}$ :


    $$h^{(3)} = R(\theta) \begin{bmatrix} \frac{z \dot{\theta}}{M} \\ -\frac{\dot{z}}{M} \end{bmatrix}$$


    Puisque $R(\theta)$ est inversible et $z \neq 0$, on peut isoler de manière unique $\dot{z}$ et $\dot{\theta}$.

    **3. Calcul de $x, y$ et $\dot{x}, \dot{y}$**
    Une fois $\theta$ et $\dot{\theta}$ connus, on utilise la définition géométrique du point $h$ pour "revenir" au centre de masse :


    $$\begin{bmatrix} x \\ y \end{bmatrix} = h - \frac{\ell}{6} \begin{bmatrix} -\sin \theta \\ \cos \theta \end{bmatrix}$$


    Les vitesses $\dot{x}, \dot{y}$ se déduisent par dérivation simple.

    Sans cette hypothèse, il y aurait une ambiguïté : la fusée pourrait être "à l'endroit" avec une poussée positive, ou "à l'envers" avec une poussée négative pour produire la même accélération au point $h$. En fixant $z < 0$ (poussée vers le bas dans le repère local), on s'assure que la fusée pointe toujours vers le haut par rapport à sa direction de poussée.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Puisque nous avons prouvé que l'état complet et les commandes dépendent des dérivées de $h$ jusqu'à l'ordre 4, nous devons utiliser un polynôme qui permet de fixer la position, la vitesse, l'accélération et le jerk aux deux extrémités (soit $2 \times 4 = 8$ conditions). Un **polynôme de degré 7** est donc le minimum requis pour chaque axe ($h_x$ et $h_y$).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ##Animation
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell
def _(mo):
    mo.center(

        mo.Html("""

    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")

    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy

    import scipy.integrate as sci


    import matplotlib as mpl

    import matplotlib.pyplot as plt


    import numpy as np

    import numpy.linalg as la

    return la, np, plt, sci, scipy


@app.cell
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0

    M = 1.0

    l = 2
    return M, g, l


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12

    J
    return (J,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.


    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):

        def fun(t, state):

            x, vx, y, vy, theta, omega = state

            f, phi = f_phi(t, state)

            d2x = (-f * np.sin(theta + phi)) / M

            d2y = (+ f * np.cos(theta + phi)) / M - g

            d2theta = - (f / J) * (l / 2) * np.sin(phi)

            return np.array([vx, d2x, vy, d2y, omega, d2theta])

        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)

        return r.sol

    return (redstart_solve,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):

            return np.array([0.0, 0.0]) # [f, phi]

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)

        y_t = sol(t)[2]

        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")

        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")

        plt.title("Free Fall")

        plt.xlabel("time $t$")

        plt.grid(True)

        plt.legend()

        return plt.gcf()

    free_fall_example()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi_smooth_landing(t, state):

            return np.array([48 / 125 * t + 11 / 25, 0])

        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)

        t = np.linspace(t_span[0], t_span[1], 1000)

        y_t = sol(t)[2]

        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")

        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")

        plt.title("Controlled Landing")

        plt.xlabel("time $t$")

        plt.grid(True)

        plt.legend()

        return plt.gcf()

    controlled_landing_example()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):

        x_min, x_max, y_min, y_max = view_box    

        width, height = x_max - x_min, y_max - y_min


        return svg.svg(

          xmlns="http://www.w3.org/2000/svg",

          viewBox=f"0 0 {width} {height}",

          style="max-height:80vh")(

              transform.translate(x=-x_min, y=y_max)(

                  transform.scale(y=-1.0)(

                      # Sky

                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),

                      # Ground

                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),

                      # Target 

                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),

                      *objects,

                )

            )

        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(

        [

            # Display an empty world

            mo.Html(

                world([-3, 3, -2, 4])

            ),

            # Display a world with a black square on top of the landing pad

            mo.Html(

                world(

                    [-3, 3, -2, 4], 

                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),

                )    

            ),

            # Display a world with a red square in the top-left corner of the view box

            # and a blue square on the top-right corner of the view box.

            mo.Html(

                world(

                    [-3, 3, -2, 4],

                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),

                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                

                )

            )

        ],

        justify="space-around"

    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):

        flame_length = (l / 2) * (f / M / g)

        return transform.translate(x, y)(

            transform.rotate(theta / np.pi * 180.0)(

                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),

                transform.translate(0, -l / 2)(

                    transform.rotate(phi / np.pi * 180)(

                        svg.rect(

                            x=-l/20,

                            y=-flame_length,

                            width=l/10,

                            height=flame_length,

                            fill="red",

                        )

                    )

                )

            )

        )

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(

        [

            mo.Html(

                world(

                    [-3, 3, -2, 4],

                    booster(0, l/2, 0, 0, 0),

                )

            ),

            mo.Html(

                world(

                    [-3, 3, -2, 4],

                    booster(0, l, 0, M * g, 0),

                )

            ),

            mo.Html(

                world(

                    [-3, 3, -2, 4],

                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),

                )

            ),

        ],

        justify="space-around",

    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):

        if not callable(theta):

            theta_cst = theta

            theta = lambda t: theta_cst

        if not callable(phi):

            phi_cst = phi

            phi = lambda t: phi_cst


        def theta_deg(t):

            return theta(t) / np.pi * 180.0


        def phi_deg(t):

            return phi(t) / np.pi * 180.0


        return animate_transform.translate(x, y, T=T)(

            animate_transform.rotate(theta_deg, T=T)(

                svg.rect(

                    x=-l / 20,

                    y=-l/2,

                    width=l / 10,

                    height=l,

                    fill="black",

                ),

                animate_transform.translate(y=-l/2, T=T)(

                    animate_transform.rotate(phi_deg, T=T)(

                        animate_transform.scale(y=f, T=T)(

                            svg.rect(

                                x=-l/20,

                                y=-1/M/g,

                                width=l / 10,

                                height=1/M/g,

                                fill="red",

                            )

                        )

                    )

                ),

            )

        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():

        T = 5.0

        def x(t):

            return -l/2 + l * (t / T)

        def y(t):

            return l/2 + l/2 * (t / T)

        def theta(t):

            return (t / T) * 2 * np.pi

        def f(t):

            return M * g * (t / T)

        def phi(t):

            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(

        world([-3, 3, -2, 4], booster_anim_0())

    ).center()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 

        def f_phi(t, state):

            return np.array([0, 0])

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[0]

        return mo.Html(

            world(

                [-3, 3, -2, 12], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, state):

            return np.array([M * g, 0])

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[1]

        return mo.Html(

            world(

                [-3, 3, -2, 12], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, state):

            return np.array([M * g, np.pi / 8])

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[1]

        return mo.Html(

            world(

                [-3, 3, -2, 12], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():

        t_span = [0.0, 5.0]

        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

        def f_phi(t, state):

            return np.array([48 / 125 * t + 11 / 25, 0])

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[1]

        return mo.Html(

            world(

                [-3, 3, -2, 12], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(g, np):
    A = np.zeros((6, 6))

    A[0, 1] = 1.0

    A[1, 4] = -g

    A[2, 3] = 1.0

    A[4, -1] = 1.0

    A
    return (A,)


@app.cell
def _(M, g, l, np):
    B = np.zeros((6, 2))

    B[ 1, 1]  = -g 

    B[ 3, 0]  = 1/M

    B[-1, 1] = -6 * g / l

    B
    return (B,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)

    print(f"Eigenvalues of A: {eigenvalues}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell
def _(A, B, np):
    # Controllability

    cs = np.column_stack

    mp = np.linalg.matrix_power

    KC = cs([mp(A, k) @ B for k in range(6)])

    KC
    return (KC,)


@app.cell
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([

        [0, 1, 0, 0], 

        [0, 0, -g, 0], 

        [0, 0, 0, 1], 

        [0, 0, 0, 0]], dtype=np.float64)

    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T


    print("A_lat:")

    print(A_lat)

    print("B_lat:")

    print(B_lat)
    return A_lat, B_lat


@app.cell
def _(A_lat, B_lat, np):
    # Controllability

    _cs = np.column_stack

    _mp = np.linalg.matrix_power

    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])

    KC_lat
    return (KC_lat,)


@app.cell
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    def make_fun_lat(phi):

        def fun_lat(t, state):

            x, dx, theta, dtheta = state

            phi_ = phi(t, state)

            d2x = -g * (theta + phi_)

            d2theta = - 6 * g / l * phi_

            return np.array([dx, d2x, dtheta, d2theta])


        return fun_lat

    return (make_fun_lat,)


@app.cell
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():

        def phi(t, state):

            return 0.0


        f_lat = make_fun_lat(phi)

        t_span = [0, 10]

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        r = sci.solve_ivp(

            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True

        )

        t = np.linspace(t_span[0], t_span[1], 1000)

        sol_t = r.sol(t)

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

        ax1.plot(t, sol_t[0], label=r"$x(t)$")

        ax1.grid(True)

        ax1.legend()

        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")

        ax2.grid(True)

        ax2.set_xlabel(r"time $t$")

        ax2.legend()

        return mo.center(fig)



    lin_sim_1()
    return


@app.cell
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():


        K = np.array([0.0, 0.0, -1.0, 0.0])


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_k1()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():


        K = np.array([0.0, 0.0, -1.0, -0.1])


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():


        K = np.array([0.0, 0.0, -1.0, -5.0])


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_k3()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():

        K = scipy.signal.place_poles(

            A=A_lat,

            B=B_lat,

            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),

        ).gain_matrix.squeeze()


        print(f"K = {K}")


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(

        A=A_lat,

        B=B_lat,

        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),

    ).gain_matrix.squeeze()



    def lin_sim_32():

        K = Kpp

        print(f"K = {K}")


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():

        K = scipy.signal.place_poles(

            A=A_lat,

            B=B_lat,

            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),

        ).gain_matrix.squeeze()


        print(f"K = {K}")


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():

        Q = np.eye(4,4)

        print("Q:", Q)

        R = np.eye(1) #10*l**2 * np.eye(1)

        print("R:", R)

        Pi = scipy.linalg.solve_continuous_are(

            a=A_lat, 

            b=B_lat, 

            q=Q, 

            r=R

        )

        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()


        K = Koc

        print(f"K = {K}")


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)

    print("Q:", Q)

    R = 100 * np.eye(1)

    print("R:", R)

    Pi = scipy.linalg.solve_continuous_are(

        a=A_lat, 

        b=B_lat, 

        q=Q, 

        r=R

    )

    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()


    def lin_sim_42():

        K = Koc

        print(f"K = {K}")


        print(

            "eigenvalues:",

            np.linalg.eig(

                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))

            ).eigenvalues,

        )


        t_span = [0, 20.0]

        t = np.linspace(t_span[0], t_span[1], 1000)

        state_0 = [0, 0, 45 * np.pi / 180.0, 0]


        def phi(t, state):

            return -K.dot(state)


        f_lat = make_fun_lat(phi)

        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)

        sol_lin_t = r.sol(t)


        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))

        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")

        ax1.grid(True)

        ax1.legend(loc="lower right")

        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")

        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax2.grid(True)

        ax2.legend(loc="lower right")

        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")

        ax3.grid(True)

        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")

        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")

        ax3.set_xlabel(r"time $t$")

        ax3.legend(loc="lower right")

        return mo.center(fig)



    lin_sim_42()
    return (Koc,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():

        t_span = [0.0, 20.0]

        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]

        def f_phi(t, state):

            x, dx, y, dy, theta, dtheta = state  

            return np.array(

                [M*g, -Kpp.dot([x, dx, theta, dtheta])]

            )

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[1]

        return mo.Html(

            world(

                [-6, 6, -2, 22], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    _anim()
    return


@app.cell
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():

        t_span = [0.0, 20.0]

        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]

        def f_phi(t, state):

            x, dx, y, dy, theta, dtheta = state  

            return np.array(

                [M*g, -Koc.dot([x, dx, theta, dtheta])]

            )

        sol = redstart_solve(t_span, y0, f_phi)

        x = lambda t: sol(t)[0]

        y = lambda t: sol(t)[2]

        theta = lambda t : sol(t)[4]

        f = lambda t: f_phi(t, sol(t))[0]

        phi = lambda t: f_phi(t, sol(t))[1]

        return mo.Html(

            world(

                [-6, 6, -2, 22], 

                booster_anim(x, y, theta, f, phi, T=t_span[1])

            )

        ).center()


    _anim()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & \cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Le centre de masse de la fusée est en $(x, y)$. Le vecteur unitaire pointant vers le **haut** de la fusée (dans la direction de son axe) est :
    $$
    \vec{u}_{axe} = \begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    $$

    Le point situé à une distance $\ell/6$ **au-dessus** du centre de masse est :
    $$
    (x, y) + \frac{\ell}{6}\begin{bmatrix} -\sin\theta \\ +\cos\theta \end{bmatrix}
    = \begin{bmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{bmatrix} = h
    $$

    **Conclusion géométrique :** $h$ est la position du point situé au **tiers supérieur** de la fusée (à $\ell/6$ au-dessus du centre, donc à $\ell/3$ du sommet). C'est le **centre de masse du tiers supérieur** de la fusée.

    Ce point a une propriété mathématique remarquable : ses dérivées successives s'expriment simplement en fonction des commandes, ce qui permet la linéarisation exacte.
    """)
    return


@app.cell
def _(np, plt):
    def draw_booster_geometry():

        # Paramètres du modèle

        l = 2.0  # longueur totale

        theta = np.radians(20)  # inclinaison de 20 degrés vers la gauche (theta > 0)

        x, y = 0, 0  # Position du centre de masse (CoM)



        # Calcul des positions des extrémités du booster

        # Le sommet (top)

        x_top = x - (l/2) * np.sin(theta)

        y_top = y + (l/2) * np.cos(theta)

        # La base (moteur)

        x_base = x + (l/2) * np.sin(theta)

        y_base = y - (l/2) * np.cos(theta)



        # Calcul de la position du point h

        # h = CoM + (l/6) * vecteur_unitaire_vers_le_haut

        xh = x - (l/6) * np.sin(theta)

        yh = y + (l/6) * np.cos(theta)



        # Création du graphique

        plt.figure(figsize=(8, 10))


        # Dessin du corps du booster (une ligne épaisse)

        plt.plot([x_base, x_top], [y_base, y_top], color='lightgray', linewidth=10, solid_capstyle='round', label='Corps du Booster')



        # Repères (axes passant par le CoM)

        plt.axhline(0, color='black', lw=0.5, ls='--')

        plt.axvline(0, color='black', lw=0.5, ls='--')



        # Point : Centre de Masse (CoM)

        plt.plot(x, y, 'ro', markersize=12, label='Centre de Masse $(x, y)$')



        # Point : h

        plt.plot(xh, yh, 'bo', markersize=12, label='Point $h$')



        # Flèches de dimensions

        # Distance CoM -> h

        plt.annotate('', xy=(xh, yh), xytext=(x, y), arrowprops=dict(arrowstyle='<->', color='blue', lw=2))

        plt.text((x+xh)/2 - 0.25, (y+yh)/2, r'$\ell/6$', color='blue', fontsize=14, fontweight='bold')



        # Distance CoM -> Sommet

        plt.annotate('', xy=(x_top, y_top), xytext=(x, y), arrowprops=dict(arrowstyle='<->', color='black'))

        plt.text((x+x_top)/2 - 0.25, (y+y_top)/2 + 0.1, r'$\ell/2$', fontsize=12)


        # Indication de l'angle theta

        plt.plot([0, 0], [0, 0.7], 'k--', lw=1) # Axe vertical de référence

        plt.text(-0.15, 0.4, r'$\theta$', fontsize=16)


        # Mise en forme

        plt.title("Interprétation géométrique du vecteur sortie $h$", fontsize=14)

        plt.legend(loc='lower left')

        plt.axis('equal')

        plt.grid(True, which='both', linestyle=':', alpha=0.5)

        plt.xlabel("Position horizontale")

        plt.ylabel("Altitude")



        plt.show()


    draw_booster_geometry()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Calcul de $\dot{h}$ (dérivée première)

    On part de la définition :
    $$
    h = \begin{bmatrix} x - (\ell/6)\sin\theta \\ y + (\ell/6)\cos\theta \end{bmatrix}
    $$

    On dérive chaque composante par rapport au temps (règle de dérivation en chaîne) :

    $$
    \dot{h}_x = \frac{d}{dt}\left[x - \frac{\ell}{6}\sin\theta\right] = \dot{x} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}
    $$

    $$
    \dot{h}_y = \frac{d}{dt}\left[y + \frac{\ell}{6}\cos\theta\right] = \dot{y} - \frac{\ell}{6}\sin\theta\cdot\dot{\theta}
    $$

    Donc :
    $$
    \boxed{\dot{h} = \begin{bmatrix} \dot{x} - (\ell/6)\cos\theta\,\dot{\theta} \\ \dot{y} - (\ell/6)\sin\theta\,\dot{\theta} \end{bmatrix}}
    $$

    -

    Calcul de $\ddot{h}$ (dérivée seconde)

    On dérive $\dot{h}$ une seconde fois. Pour la composante $x$ :

    $$
    \ddot{h}_x = \frac{d}{dt}\left[\dot{x} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}\right]
    = \ddot{x} - \frac{\ell}{6}\frac{d}{dt}\left[\cos\theta\cdot\dot{\theta}\right]
    $$

    En développant la dérivée du produit $\cos\theta\cdot\dot\theta$ :

    $$
    \frac{d}{dt}\left[\cos\theta\cdot\dot{\theta}\right] = -\sin\theta\cdot\dot{\theta}^2 + \cos\theta\cdot\ddot{\theta}
    $$

    Donc :
    $$
    \ddot{h}_x = \ddot{x} + \frac{\ell}{6}\sin\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\cos\theta\cdot\ddot{\theta}
    $$

    De même pour la composante $y$ :
    $$
    \ddot{h}_y = \ddot{y} - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\sin\theta\cdot\ddot{\theta}
    $$


    Substitution des équations du mouvement

    On utilise maintenant les trois équations du mouvement de la fusée :

    $$
    M\ddot{x} = f_x = -f\sin(\theta+\phi)
    \qquad \Rightarrow \qquad
    \ddot{x} = \frac{f_x}{M}
    $$

    $$
    M\ddot{y} = f_y - Mg = f\cos(\theta+\phi) - Mg
    \qquad \Rightarrow \qquad
    \ddot{y} = \frac{f_y}{M} - g
    $$

    $$
    J\ddot{\theta} = -f\frac{\ell}{2}\sin\phi
    \qquad \Rightarrow \qquad
    \ddot{\theta} = -\frac{f\ell}{2J}\sin\phi
    $$

    En substituant dans $\ddot{h}_x$ et $\ddot{h}_y$ :

    $$
    \ddot{h}_x = \frac{f_x}{M} + \frac{\ell}{6}\sin\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\cos\theta\cdot\ddot{\theta}
    $$

    $$
    \ddot{h}_y = \frac{f_y}{M} - g - \frac{\ell}{6}\cos\theta\cdot\dot{\theta}^2 - \frac{\ell}{6}\sin\theta\cdot\ddot{\theta}
    $$

     Substitution du système auxiliaire

    Le système auxiliaire donne la force $(f_x, f_y)$ sous la forme :

    $$
    \begin{bmatrix} f_x \\ f_y \end{bmatrix}
    = R\!\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix} z - M\ell\dot{\theta}^2/6 \\ M\ell v_2/(6z) \end{bmatrix}
    $$

    La matrice de rotation $R(\theta - \pi/2)$ vaut :

    $$
    R\!\left(\theta - \frac{\pi}{2}\right)
    = \begin{bmatrix} \cos(\theta-\pi/2) & -\sin(\theta-\pi/2) \\ \sin(\theta-\pi/2) & \cos(\theta-\pi/2) \end{bmatrix}
    = \begin{bmatrix} \sin\theta & \cos\theta \\ -\cos\theta & \sin\theta \end{bmatrix}
    $$

    Donc :

    $$
    f_x = \sin\theta\cdot\left(z - \frac{M\ell\dot{\theta}^2}{6}\right) + \cos\theta\cdot\frac{M\ell v_2}{6z}
    $$

    $$
    f_y = -\cos\theta\cdot\left(z - \frac{M\ell\dot{\theta}^2}{6}\right) + \sin\theta\cdot\frac{M\ell v_2}{6z}
    $$

    Et la dynamique angulaire du système auxiliaire donne :

    $$
    \ddot{\theta} = \frac{M\ell v_2}{6Jz} \frac{\ell} {2} = \frac{v_2} {z}
    $$



    En substituant \(f_x\), \(f_y\) et \(\ddot{\theta}\) dans les expressions de
    \(\ddot h_x\) et \(\ddot h_y\), puis en développant, on obtient :

    \[
    \ddot h_x
    =
    \frac{\sin\theta}{M}
    \left(
    z - \frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \frac{\ell\cos\theta}{6z}v_2
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    -
    \frac{\ell}{6}\cos\theta
    \cdot
    \frac{v_2}{z}
    \]



    Simplification des termes en \(\dot\theta^2\)

    Les termes en \(\dot\theta^2\) se compensent exactement :

    \[
    \frac{\sin\theta}{M}
    \left(
    -\frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    =
    0
    \]

    En effet :

    \[
    -\frac{\ell}{6}\sin\theta\,\dot\theta^2
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    =
    0
    \]
     Simplification des termes en \(v_2\)

    Les termes contenant \(v_2\) se simplifient également :

    \[
    \frac{\ell\cos\theta}{6z}v_2
    -
    \frac{\ell\cos\theta}{6z}v_2
    =
    0
    \]



    Résultat pour \(\ddot h_x\)

    Il reste donc :

    \[
    \ddot h_x
    =
    \frac{z\sin\theta}{M}
    \]

    que l’on peut écrire sous la forme :

    \[
    \ddot h_x
    =
    -
    \frac{z}{M}
    (\sin\theta)
    \]

     Calcul analogue pour \(\ddot h_y\)

    De manière similaire, les mêmes simplifications apparaissent dans
    \(\ddot h_y\), avec en plus le terme gravitationnel \(-g\).

    On obtient :

    \[
    \ddot h_y
    =
    \frac{-z}{M}\cos\theta
    -
    g
    \]



    En regroupant les deux composantes :

    \[
    \boxed{
    \ddot h
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    }
    \]
    """)
    return


@app.cell
def _(M, g, np):
    def ddot_h(theta, z, M=M, g=g):


        return np.array([

            -(z/M) * np.sin(theta),

             (z/M) * np.cos(theta) - g

        ])

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    On part de l’expression :

    \[
    \ddot{h}
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    \]

    On dérive cette expression par rapport au temps.

    Comme \(g\) est constant, sa dérivée est nulle :

    \[
    \frac{d}{dt}
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    0
    \end{bmatrix}
    \]

    Il reste donc à dériver :

    \[
    \frac{z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]

    On applique la règle du produit :

    \[
    \frac{d}{dt}
    \left(
    \frac{z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \right)
    =
    \frac{\dot z}{M}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    +
    \frac{z}{M}
    \frac{d}{dt}
    \begin{bmatrix}
    -\sin\theta \\
    \cos\theta
    \end{bmatrix}
    \]

    Or :

    \[
    \frac{d}{dt}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    =
    \dot\theta
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    \]

    Ainsi :

    \[
    \boxed{
    h^{(3)}
    =
    \frac{\dot z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    +
    \frac{z\dot\theta}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    }
    \]

    donc :
    $$h^{(3)} = R(\theta) \begin{bmatrix} \frac{z \dot{\theta}}{M} \\ -\frac{\dot{z}}{M} \end{bmatrix}$$

    Calcul de \(h^{(4)}\)

    On dérive maintenant \(h^{(3)}\).

    On utilise la dynamique auxiliaire :

    \[
    \ddot z = v_1
    \]

    Après dérivation complète et regroupement des termes, on obtient :

    \[
    \boxed{
    h^{(4)}
    =
    \underbrace{
    \frac{v_1}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    }_{\text{terme en } v_1}
    +
    \underbrace{
    \frac{1}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    v_2
    }_{\text{terme en } v_2}
    +
    \underbrace{
    \alpha(\theta,\dot\theta,z,\dot z)
    }_{\text{terme autonome}}
    }
    \]

    où :

    \[
    \alpha(\theta,\dot\theta,z,\dot z)
    \]

    regroupe tous les termes ne dépendant pas des commandes
    \((v_1,v_2)\).

    \[
    \boxed{
    h^{(4)}
    =
    \underbrace{
    \frac{v_1}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    }_{\text{terme en } v_1}
    +
    \underbrace{
    \frac{v_2}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    }_{\text{terme en } v_2}
    +
    \underbrace{
    \alpha(\theta,\dot\theta,z,\dot z)
    }_{\text{terme autonome}}
    }
    \]

    ---

    On remarque que les deux vecteurs forment exactement une rotation :

    \[
    \begin{bmatrix}
    \sin\theta & \cos\theta \\
    -\cos\theta & \sin\theta
    \end{bmatrix}
    =
    R\left(\theta - \frac{\pi}{2}\right)
    \]

    Donc on peut écrire :

    \[
    \boxed{
    h^{(4)}
    =
    \frac{1}{M}
    R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    v_1 \\
    v_2
    \end{bmatrix}
    +
    \alpha(\theta,\dot\theta,z,\dot z)
    }
    \]

    ---



    \[
    \boxed{
    h^{(4)}
    =
    \frac{1}{M}
    R\left(\theta - \frac{\pi}{2}\right)\, v
    +
    \alpha(\theta,\dot\theta,z,\dot z)
    }
    \]

    avec :

    \[
    v =
    \begin{bmatrix}
    v_1 \\
    v_2
    \end{bmatrix}
    \]
    """)
    return


@app.cell
def _(M, l, np):
    def d3h(theta, dtheta, z, dz, M=M):


        s, c = np.sin(theta), np.cos(theta)

        return np.array([

            (dz/M)*s + (z*dtheta/M)*c,

             -(dz/M)*c + (z*dtheta/M)*s

        ])


    def h4_alpha_E(theta, dtheta, z, dz, M=M, l=l):


        s, c = np.sin(theta), np.cos(theta)


        # Matrice E (coeff de v)

        E = np.array([

            [s/M,      c/M],

            [-c/M,      s/M]

        ])


        # Terme autonome alpha

        alpha = np.array([

            2*(dz/M)*dtheta*(-c) + (z/M)*dtheta**2*(-s),

            2*(dz/M)*dtheta*(-s) + (z/M)*dtheta**2*( c)

        ])


        return alpha, E

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    On part de la forme obtenue précédemment :

    $$
    h^{(4)} =
    \frac{1}{M}
    R\left(\theta - \frac{\pi}{2}\right)\, v
    +
    \alpha(\theta,\dot\theta,z,\dot z)
    $$

    On impose :

    $$
    u = h^{(4)}
    $$

    donc :

    $$
    u - \alpha =
    \frac{1}{M}
    R\left(\theta - \frac{\pi}{2}\right)\, v
    $$

    $$
    R\left(\frac{\pi}{2} - \theta\right)(u - \alpha)
    =
    \frac{1}{M} v
    $$

    On obtient finalement :

    $$
    \boxed{
    v
    =
    M \, R\left(\frac{\pi}{2} - \theta\right)\,(u - \alpha(\theta,\dot\theta,z,\dot z))
    }
    $$
    """)
    return


@app.cell
def _(M, R2, alpha_term, g, l, np):
    def exact_linearization_v(theta, dtheta, z, dz, u, M=M, g=g, l=l):

        alpha = alpha_term(theta, dtheta, z, dz, M, l)
        R_inv = R2(-theta + np.pi/2)

        # commande exacte
        v = M * (R_inv @ (u - alpha))

        return v

    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):


        # h = center of mass + (L/6) * vecteur_unitaire_vers_le_haut

        hx = x - (l/6) * np.sin(theta)

        hy = y + (l/6) * np.cos(theta)


        # dh = dCoM + (L/6) * d_theta * vecteur_unitaire_orthogonal

        dhx = dx - (l/6) * dtheta * np.cos(theta)

        dhy = dy - (l/6) * dtheta * np.sin(theta)


        # d2h = (z/M) * vecteur_axial - [0, g]

        d2hx = (z/M) * np.sin(theta)

        d2hy = -(z/M) * np.cos(theta) - g


        # d3h = (dz/M) * vecteur_axial + (z*dtheta/M) * vecteur_transverse

        d3hx = (dz/M) * np.sin(theta) + (z * dtheta / M) * np.cos(theta)

        d3hy = -(dz/M) * np.cos(theta) + (z * dtheta / M) * np.sin(theta)


        return np.array([hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy])

    return (Tr,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Pour montrer que l'on peut calculer l'état $(x, y, \theta, z, \dots)$ à partir de $(h, \dot{h}, \ddot{h}, h^{(3)})$, on procède par étapes :

    **1. Calcul de $\theta$ et $z$ (à partir de $\ddot{h}$)**
    On part de l'accélération du point $h$ :


    $$\ddot{h} + g \vec{j} = \frac{z}{M} \begin{bmatrix} \sin \theta \\ -\cos \theta \end{bmatrix}$$


    En prenant la norme des deux côtés, on trouve la poussée auxiliaire $z$ :


    $$z = -M \left\| \ddot{h} + g \vec{j} \right\|$$


    *(On prend la valeur négative car l'énoncé impose $z < 0$).*
    L'angle $\theta$ est ensuite obtenu par l'orientation du vecteur accélération :


    $$\theta = \operatorname{atan2}(\ddot{h}_x, -(\ddot{h}_y + g))$$

    **2. Calcul de $\dot{\theta}$ et $\dot{z}$ (à partir de $h^{(3)}$)**
    On dérive l'expression de $\ddot{h}$. Comme on l'a vu précédemment, cela donne un système linéaire en $\dot{z}$ et $\dot{\theta}$ :


    $$h^{(3)} = R(\theta) \begin{bmatrix} \frac{z \dot{\theta}}{M} \\ -\frac{\dot{z}}{M} \end{bmatrix}$$


    Puisque $R(\theta)$ est inversible et $z \neq 0$, on peut isoler de manière unique $\dot{z}$ et $\dot{\theta}$.

    **3. Calcul de $x, y$ et $\dot{x}, \dot{y}$**
    Une fois $\theta$ et $\dot{\theta}$ connus, on utilise la définition géométrique du point $h$ pour "revenir" au centre de masse :


    $$\begin{bmatrix} x \\ y \end{bmatrix} = h - \frac{\ell}{6} \begin{bmatrix} -\sin \theta \\ \cos \theta \end{bmatrix}$$


    Les vitesses $\dot{x}, \dot{y}$ se déduisent par dérivation simple.

    Sans cette hypothèse, il y aurait une ambiguïté : la fusée pourrait être "à l'endroit" avec une poussée positive, ou "à l'envers" avec une poussée négative pour produire la même accélération au point $h$. En fixant $z < 0$ (poussée vers le bas dans le repère local), on s'assure que la fusée pointe toujours vers le haut par rapport à sa direction de poussée.

    # 🧩 Inversion complète

    On suppose que l’on connaît :

    \[
    h,\quad \dot h,\quad \ddot h,\quad h^{(3)}
    \]

    et que :

    \[
    z < 0
    \]

    en tout temps.



    # Dynamique

    On part de :

    \[
    \ddot h =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    \]

    Donc :

    \[
    \ddot h +
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    \]



    ## Reconstruction de \(\theta\)

    En identifiant les composantes :

    \[
    \ddot h_x = \frac{z}{M}\sin\theta
    \]

    \[
    \ddot h_y + g = -\frac{z}{M}\cos\theta
    \]

    On prend le rapport :

    \[
    \tan\theta
    =
    \frac{\ddot h_x}{-\ddot h_y-g}
    \]

    Donc :

    \[
    \boxed{
    \theta =
    \operatorname{atan2}
    \left(
    \ddot h_x,
    -\ddot h_y-g
    \right)
    }
    \]



    ## Reconstruction de \(z\)

    On prend la norme :

    \[
    \left\|
    \ddot h +
    \begin{bmatrix}
    0\\
    g
    \end{bmatrix}
    \right\|
    =
    \left|
    \frac{z}{M}
    \right|
    \]

    Comme \(z<0\) :

    \[
    \boxed{
    z =
    -M
    \left\|
    \ddot h +
    \begin{bmatrix}
    0\\
    g
    \end{bmatrix}
    \right\|
    }
    \]



    ## Reconstruction de \(\dot z\)

    On dérive :

    \[
    \ddot h =
    \frac{z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    -
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    \]

    ce qui donne :

    \[
    h^{(3)}
    =
    \frac{\dot z}{M}
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    +
    \frac{z\dot\theta}{M}
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    \]

    En projetant sur :

    \[
    \begin{bmatrix}
    \sin\theta \\
    -\cos\theta
    \end{bmatrix}
    \]

    on élimine le terme en \(\dot\theta\) :

    \[
    \boxed{
    \dot z
    =
    M
    \left(
    h^{(3)}_x \sin\theta
    -
    h^{(3)}_y \cos\theta
    \right)
    }
    \]



    ## Reconstruction de \(\dot\theta\)

    On projette maintenant sur :

    \[
    \begin{bmatrix}
    \cos\theta \\
    \sin\theta
    \end{bmatrix}
    \]

    ce qui donne :

    \[
    \boxed{
    \dot\theta
    =
    \frac{M}{z}
    \left(
    h^{(3)}_x \cos\theta
    +
    h^{(3)}_y \sin\theta
    \right)
    }
    \]



    ## Reconstruction de \(x,y\)

    À partir de :

    \[
    h =
    \begin{bmatrix}
    x - \frac{\ell}{6}\sin\theta \\
    y + \frac{\ell}{6}\cos\theta
    \end{bmatrix}
    \]

    on obtient :

    \[
    \boxed{
    x =
    h_x +
    \frac{\ell}{6}\sin\theta
    }
    \]

    \[
    \boxed{
    y =
    h_y -
    \frac{\ell}{6}\cos\theta
    }
    \]



    # Reconstruction de \(\dot x,\dot y\)

    On utilise :

    \[
    \dot h =
    \begin{bmatrix}
    \dot x - \frac{\ell}{6}\cos\theta\,\dot\theta \\
    \dot y - \frac{\ell}{6}\sin\theta\,\dot\theta
    \end{bmatrix}
    \]

    Donc :

    \[
    \boxed{
    \dot x =
    \dot h_x +
    \frac{\ell}{6}\cos\theta\,\dot\theta
    }
    \]

    \[
    \boxed{
    \dot y =
    \dot h_y +
    \frac{\ell}{6}\sin\theta\,\dot\theta
    }
    \]
    """)
    return


@app.cell
def _(M, Tr, g, l, np):
    def T_inv(hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy):



        # -------------------------
        # 1. Recover theta and z
        # -------------------------
        d2h_shift = np.array([d2hx,d2hy]) + np.array([0, g])

        z = M * np.linalg.norm(d2h_shift)

        # assumption z < 0
        z = -abs(z)

        sin_theta = d2h_shift[0] / (z / M)
        cos_theta = -d2h_shift[1] / (z / M)

        theta = np.arctan2(sin_theta, cos_theta)

        # -------------------------
        # 2. Recover theta_dot
        # -------------------------


        dtheta = (M / z) * (
            d3hx * np.cos(theta)
            + d3hy * np.sin(theta)
        )

        # -------------------------
        # 3. Recover z_dot
        # -------------------------
        dz = M * (
            d3hx * np.sin(theta)
            - d3hy * np.cos(theta)
        )

        # -------------------------
        # 4. Recover x, y
        # -------------------------
        x = hx + (l / 6) * np.sin(theta)
        y = hy - (l / 6) * np.cos(theta)

        # -------------------------
        # 5. Recover dx, dy
        # -------------------------
        dx = dhx + (l / 6) * np.cos(theta) * dtheta
        dy = dhy + (l / 6) * np.sin(theta) * dtheta

        return x, dx, y, dy, theta, dtheta, z, dz
    Tr(1,2,3,4,0.1,0.2,-0.3,-0.4)
    T_inv(*Tr(1,2,3,4,0.1,0.2,-0.3,-0.4))
    return (T_inv,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Puisque nous avons prouvé que l'état complet et les commandes dépendent des dérivées de $h$ jusqu'à l'ordre 4, nous devons utiliser un polynôme qui permet de fixer la position, la vitesse, l'accélération et le jerk aux deux extrémités (soit $2 \times 4 = 8$ conditions). Un **polynôme de degré 7** est donc le minimum requis pour chaque axe ($h_x$ et $h_y$).
    """)
    return


@app.cell
def _(J, M, T_inv, Tr, l, np):
    def compute(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0,
                x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf, tf):

        # 1. Transformation vers la sortie plate
        #    Tr retourne : (hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy)
        h_start = Tr(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0)
        h_end   = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)

        # 2. Polynômes de degré 7 pour chaque axe
        def solve_poly(y0, dy0, d2y0, d3y0, yf, dyf, d2yf, d3yf, T):
            M_mat = np.array([
                [0,       0,       0,       0,      0,     0,   0, 1],
                [0,       0,       0,       0,      0,     0,   1, 0],
                [0,       0,       0,       0,      0,     2,   0, 0],
                [0,       0,       0,       0,      6,     0,   0, 0],
                [T**7,   T**6,   T**5,   T**4,   T**3,  T**2,  T, 1],
                [7*T**6, 6*T**5, 5*T**4, 4*T**3, 3*T**2, 2*T,  1, 0],
                [42*T**5,30*T**4,20*T**3,12*T**2, 6*T,   2,    0, 0],
                [210*T**4,120*T**3,60*T**2,24*T,  6,     0,    0, 0]
            ])
            b = np.array([y0, dy0, d2y0, d3y0, yf, dyf, d2yf, d3yf])
            return np.linalg.solve(M_mat, b)

        # h_start = (hx, hy, dhx, dhy, d2hx, d2hy, d3hx, d3hy)
        #  index :    0    1    2    3     4     5     6     7
        coeff_x = solve_poly(h_start[0], h_start[2], h_start[4], h_start[6],
                             h_end[0],   h_end[2],   h_end[4],   h_end[6],   tf)
        coeff_y = solve_poly(h_start[1], h_start[3], h_start[5], h_start[7],
                             h_end[1],   h_end[3],   h_end[5],   h_end[7],   tf)

        def fun(t):
            # 3. Évaluation des polynômes et leurs dérivées
            def eval_poly(c, t):
                p   = np.poly1d(c)
                dp  = p.deriv()
                d2p = dp.deriv()
                d3p = d2p.deriv()
                d4p = d3p.deriv()
                return p(t), dp(t), d2p(t), d3p(t), d4p(t)

            hx,  dhx,  d2hx,  d3hx,  d4hx  = eval_poly(coeff_x, t)
            hy,  dhy,  d2hy,  d3hy,  d4hy  = eval_poly(coeff_y, t)

            # 4. Inversion : scalaires séparés → T_inv compatible
            x, dx, y, dy, theta, dtheta, z, dz = T_inv(
                hx, hy,
                dhx, dhy,
                d2hx, d2hy,
                d3hx, d3hy
            )

            # 5. Calcul des commandes f et phi
            d4h_vec = np.array([d4hx, d4hy])

            b_term = (2 * dz * dtheta * np.array([ np.cos(theta),  np.sin(theta)]) +
                          z * dtheta**2 * np.array([-np.sin(theta),  np.cos(theta)]))

            mat_A = np.array([[np.sin(theta),  np.cos(theta)],
                              [-np.cos(theta), np.sin(theta)]])

            v = np.linalg.solve(mat_A, M * d4h_vec - b_term)
            v1, v2 = v

            f   = np.sqrt(z**2 + (J * v2 / (l / 2))**2)
            phi = np.arctan2(J * v2 / (l / 2), z)

            return x, dx, y, dy, theta, dtheta, z, dz, f, phi

        return fun

    return (compute,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(M, compute, g, l, np, plt):
    # 1. Génération de la trajectoire
    tf = 10.0
    fun = compute(5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0,
                  0.0, 0.0, 2/3*l, 0.0, 0.0, 0.0, -M*g, 0.0, tf)

    t_range = np.linspace(0, tf, 500)
    results = np.array([fun(t) for t in t_range])

    # Extraction des données
    x, dx, y, dy, theta, dtheta, z, dz, f, phi = results.T

    # 2. Tracé des variables d'état
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].plot(t_range, x, label='x(t)')
    axs[0, 0].plot(t_range, y, label='y(t)')
    axs[0, 0].set_title("Position")
    axs[0, 0].legend()

    axs[0, 1].plot(t_range, theta, color='r')
    axs[0, 1].set_title("Angle inclinaison (theta)")

    axs[1, 0].plot(t_range, f, color='g')
    axs[1, 0].set_title("Poussée (f)")

    axs[1, 1].plot(t_range, phi, color='m')
    axs[1, 1].set_title("Angle Gimbal (phi)")

    plt.tight_layout()
    plt.show()
    return f, phi, t_range, theta, x, y


@app.cell
def _(M, f, g, l, mo, np, phi, plt, t_range, theta, x, y):

    from matplotlib.animation import FuncAnimation, PillowWriter

    fig_anim, ax_anim = plt.subplots(figsize=(6, 8))
    ax_anim.set_xlim(-2, 8)
    ax_anim.set_ylim(0, 25)
    ax_anim.set_aspect('equal')
    ax_anim.grid(True, linestyle='--', alpha=0.6)

    line,        = ax_anim.plot([], [], 'o-', lw=4, color='black')
    thrust_line, = ax_anim.plot([], [], '-',  lw=2, color='orange')

    def update(i):
        curr_x, curr_y, curr_theta = x[i], y[i], theta[i]
        curr_f, curr_phi           = f[i], phi[i]

        top_x = curr_x - (l/2)*np.sin(curr_theta)
        top_y = curr_y + (l/2)*np.cos(curr_theta)
        bot_x = curr_x + (l/2)*np.sin(curr_theta)
        bot_y = curr_y - (l/2)*np.cos(curr_theta)
        line.set_data([top_x, bot_x], [top_y, bot_y])

        if curr_f > 0.1:
            f_scale = curr_f / (M * g) * 2
            flame_x = bot_x + f_scale * np.sin(curr_theta + curr_phi+np.pi)
            flame_y = bot_y - f_scale * np.cos(curr_theta + curr_phi + np.pi)
            thrust_line.set_data([bot_x, flame_x], [bot_y, flame_y])
        else:
            thrust_line.set_data([], [])

        return line, thrust_line

    step = 2
    ani = FuncAnimation(fig_anim, update,
                        frames=range(0, len(t_range), step),
                        interval=30, blit=True)

    # Sauvegarde en GIF
    ani.save("booster.gif", writer=PillowWriter(fps=30))
    plt.close()

    # Affichage natif Marimo
    mo.image("booster.gif")
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
