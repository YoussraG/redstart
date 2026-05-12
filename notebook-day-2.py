import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
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

    return la, np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    À un équilibre, la dérivée temporelle du vecteur d'état est nulle :

    $$\dot{s} = F(s, f, \phi) = \mathbf{0}$$

    Le champ de vecteurs établi précédemment est :

    $$F(s, f, \phi) = \begin{pmatrix} v_x \\ -\dfrac{f}{M}\sin(\theta+\phi) \\ v_y \\ +\dfrac{f}{M}\cos(\theta+\phi) - g \\ \omega \\ -\dfrac{f\ell}{2J}\sin\phi \end{pmatrix} = \mathbf{0}$$

    **Conditions cinématiques.** Les composantes 1, 3 et 5 donnent directement :

    $$v_x = 0, \qquad v_y = 0, \qquad \omega = 0$$

    Le booster est donc au repos : aucune vitesse de translation ni de rotation.

    **Angle du réacteur.** La composante 6, avec $f > 0$ et $\ell > 0$, donne :

    $$-\frac{f\ell}{2J}\sin\phi = 0 \implies \sin\phi = 0$$

    La contrainte $|\phi| < \pi/2$ assure que la seule solution est :

    $$\phi^* = 0$$

    **Inclinaison du booster.** La composante 2, avec $f > 0$, donne :

    $$-\frac{f}{M}\sin(\theta + \phi) = 0 \implies \sin(\theta + \phi) = 0$$

    Puisque $\phi^* = 0$ est déjà établi, on a $|\theta + \phi| = |\theta| < \pi/2$, et $\sin$ ne s'annule sur cet intervalle strict qu'en zéro, donc :

    $$\theta^* = 0$$

    **Amplitude de la poussée.** La composante 4, avec $\theta^* = \phi^* = 0$ :

    $$\frac{f}{M}\cos(0) - g = 0 \implies f^* = Mg$$

    La poussée compense exactement le poids du booster.

    **Conclusion.** L'ensemble des équilibres est la famille :

    $$s^* = (x^*,\ 0,\ y^*,\ 0,\ 0,\ 0) \in \mathbb{R}^6, \qquad f^* = Mg, \qquad \phi^* = 0$$

    pour tout $(x^*, y^*) \in \mathbb{R}^2$. La position du centre de masse est libre, mais la vitesse, l'inclinaison et la vitesse angulaire sont toutes nulles : le booster est suspendu verticalement, immobile, avec une poussée verticale qui contrebalance exactement son poids.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(M, g):
    phi_eq   = 0.0        
    theta_eq = 0.0     
    f_eq     = M * g      # poussée = poids

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On pose :
    $$x = x_{eq} + \Delta x,\quad v_x = \Delta v_x,\quad y = y_{eq} + \Delta y,\quad v_y = \Delta v_y,\quad \theta = \Delta\theta,\quad \omega = \Delta\omega$$
    $$f = Mg + \Delta f,\quad \phi = \Delta\phi$$

    On développe $F$ au premier ordre autour de $(s_{eq}, f_{eq}, \phi_{eq})=(\cdot,\, 0,0,\, 0,0,\, Mg,\, 0)$.

    Les dérivées partielles de $F$ en l'équilibre ($\theta=0$, $\phi=0$, $f=Mg$) donnent :

    $$\Delta\dot{v}_x = -\frac{\Delta f}{M}\sin(0) - \frac{Mg}{M}\cos(0)\,\Delta\theta - \frac{Mg}{M}\cos(0)\,\Delta\phi = -g\,\Delta\theta - g\,\Delta\phi$$

    $$\Delta\dot{v}_y = +\frac{\Delta f}{M}\cos(0) - \frac{Mg}{M}\sin(0)\,(\Delta\theta+\Delta\phi) = \frac{\Delta f}{M}$$

    $$\Delta\dot{\omega} = -\frac{Mg}{J}\frac{\ell}{2}\cos(0)\,\Delta\phi = -\frac{Mg\ell}{2J}\,\Delta\phi$$

    Système linéarisé complet :

    $$\Delta\dot{v}_x = -g\,\Delta\theta - g\,\Delta\phi$$
    $$\Delta\dot{v}_y = \frac{1}{M}\,\Delta f$$
    $$\Delta\dot{\omega} = -\frac{Mg\ell}{2J}\,\Delta\phi$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le système linéarisé s’écrit sous la forme :

    \[
    \dot{\delta s}
    =
    A\,\delta s
    +
    B\,\delta u
    \]

    avec :

    \[
    \delta s
    =
    \begin{pmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta y \\
    \Delta \dot{y} \\
    \Delta \theta \\
    \Delta \dot{\theta}
    \end{pmatrix}
    \]

    et :

    \[
    \delta u
    =
    \begin{pmatrix}
    \Delta f \\
    \Delta \phi
    \end{pmatrix}
    \]


    Des équations de Q11 on lit directement :

    $$A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}, \qquad
    B = \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}$$
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(J, M, g, l, np):
    A = np.array([
        [0,  1,  0,  0,   0,  0],
        [0,  0,  0,  0,  -g,  0],
        [0,  0,  0,  1,   0,  0],
        [0,  0,  0,  0,   0,  0],
        [0,  0,  0,  0,   0,  1],
        [0,  0,  0,  0,   0,  0]
    ], dtype=float)

    B = np.array([
        [0,              0           ],
        [0,             -g           ],
        [0,              0           ],
        [1/M,            0           ],
        [0,              0           ],
        [0,  -(M*g*l)/(2*J)          ]
    ], dtype=float)

    print("A =\n", A)
    print("\nB =\n", B)
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Un équilibre est asymptotiquement stable si et seulement si toutes les valeurs propres de $A$ ont une partie réelle **strictement négative**. On calcule $\text{spec}(A)$.
    """)
    return


@app.cell
def _(A, np):
    eigenvalues = np.linalg.eigvals(A)
    print("Valeurs propres de A :")
    for ev in eigenvalues:
        print(f"  λ = {ev:.4f}   Re(λ) = {ev.real:.4f}")

    print()
    if all(ev.real < 0 for ev in eigenvalues):
        print("L'équilibre est ASYMPTOTIQUEMENT STABLE")
    elif all(ev.real <= 0 for ev in eigenvalues):
        print("Toutes les valeurs propres sont à partie réelle ≤ 0,")
        print(" mais certaines sont NULLES → l'équilibre est seulement MARGINALEMENT STABLE.")
        print("Il n'est PAS asymptotiquement stable")
    else:
        print("L'équilibre est INSTABLE")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On constate alors que l'équilibre n'est pas asymptotiquement stable
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On applique le **critère de Kalman** : le système $(A, B)$ de dimension $n=6$ est contrôlable si et seulement si la matrice de contrôlabilité
    $$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix} \in \mathbb{R}^{6 \times 12}$$
    est de rang $n=6$.
    """)
    return


@app.cell
def _(A, B, np):
    def controllability_matrix(A, B):
        n = A.shape[0]
        blocks = [B]
        AiB = B.copy()
        for _ in range(1, n):
            AiB = A @ AiB
            blocks.append(AiB)
        return np.hstack(blocks)

    C_full = controllability_matrix(A, B)
    rank_C = np.linalg.matrix_rank(C_full)
    n = A.shape[0]

    print(f"Dimension de l'espace d'état : n = {n}")
    print(f"Rang de C : {rank_C}")
    if rank_C == n:
        print("Le système COMPLET est CONTRÔLABLE")
    else:
        print(f"Non contrôlable (rang {rank_C} < {n})")
    return (controllability_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Puisque le rang est égale à la dimension de l'espace n=6, on constate alors que le système complet est contrôlable
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On extrait les lignes et colonnes correspondant aux indices $\{0, 1, 4, 5\}$ de $A$ (états $x, v_x, \theta, \omega$) et la colonne $\Delta\phi$ (colonne 1 de $B$, puisque $\Delta f = 0$).
    """)
    return


@app.cell
def _(A, B, controllability_matrix, np):
    # Indices : x=0, vx=1, theta=4, omega=5
    idx = [0, 1, 4, 5]

    A_lat = A[np.ix_(idx, idx)]
    B_lat = B[idx, 1:2]   # colonne Delta_phi uniquement

    print("A_lat =\n", A_lat)
    print("\nB_lat =\n", B_lat)


    C_lat = controllability_matrix(A_lat, B_lat)
    print("\nC_lat =\n",C_lat)
    rank_lat = np.linalg.matrix_rank(C_lat)
    n_lat = A_lat.shape[0]

    print(f"\nRang de C_lat : {rank_lat} / {n_lat}")
    if rank_lat == n_lat:
        print("Le système LATÉRAL RÉDUIT est CONTRÔLABLE")
    else:
        print("Non contrôlable")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Puisque le rang est égale à la dimension de l'espace n=4, on constate alors que le système réduit est contrôlable
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On applique le modèle linéarisé au sous-système latéral $(\Delta x,\, \Delta\dot{x},\, \Delta\theta,\, \Delta\dot{\theta})$ avec $\phi(t) = 0$.

    ### Mise en équation

    Les équations linéarisées du bloc latéral (avec $\Delta\phi = 0$) sont :

    $$\Delta\ddot{x} = -g\,\Delta\theta, \qquad \Delta\ddot{\theta} = 0$$
     Sous forme matricielle :


    Nous avons prévu à la fois une résolution analytique et numérique :
    La résolution analytique :

    **Angle $\theta(t)$** — la quatrième ligne de $A_{lat}$ est nulle, donc $\ddot{\theta} = 0$. Avec $\dot{\theta}(0) = 0$ :

    $$\theta(t) = \theta(0) = \frac{\pi}{4} \quad \text{(constante pour tout } t\text{)}$$

    Sans action sur $\phi$, aucun couple n'est créé : l'angle reste figé à sa valeur initiale.

    **Position $x(t)$** — on substitue $\theta(t) = \pi/4$ :

    $$\ddot{x} = -g\cdot\frac{\pi}{4} = \text{constante}$$

    En intégrant deux fois avec $x(0) = 0$ et $\dot{x}(0) = 0$ :

    $$\boxed{x(t) = -\frac{g\pi}{8}\,t^2}$$
    """)
    return


@app.cell
def _(A_lat, np, plt):
    from scipy.integrate import solve_ivp

    ds0_lat = np.array([0.0, 0.0, np.pi/4, 0.0])  # [Delta_x, Delta_vx, Delta_theta, Delta_omega]
    t_span  = [0.0, 20.0]
    t_eval  = np.linspace(0, 20, 2000)

    def lin_open_loop(t, s):
        return A_lat @ s   

    sol_ol = solve_ivp(lin_open_loop, t_span, ds0_lat, t_eval=t_eval)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(sol_ol.t, sol_ol.y[0])
    axes[0].set_title(r"$\Delta x(t)$ — dérive parabolique")
    axes[0].set_xlabel("t (s)"); axes[0].set_ylabel(r"$\Delta x$ (m)"); axes[0].grid(True)

    axes[1].plot(sol_ol.t, np.degrees(sol_ol.y[2]), color='orange')
    axes[1].set_title(r"$\Delta\theta(t)$ — reste constant ($\phi=0$)")
    axes[1].set_xlabel("t (s)"); axes[1].set_ylabel(r"$\Delta\theta$ (degrés)"); axes[1].grid(True)

    plt.suptitle("Boucle ouverte — système latéral, $\\phi=0$", fontsize=12)
    plt.tight_layout()
    plt.show()

    print("Observation : theta reste constant (pas de couple sans phi),")
    print("              mais x dérive car l'inclinaison initiale crée une accélération horizontale.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les résultats sont similaires pour les deux résolutions :
    Observations et interprétation

    - $\theta(t)$ est **constant** : sans commande $\phi$, l'angle ne peut pas être corrigé.
    - $x(t)$ présente une **dérive parabolique** vers la gauche, conséquence directe de l'inclinaison permanente.

    Ce résultat confirme l'instabilité de l'équilibre : une inclinaison initiale $\theta(0) \neq 0$, même sans perturbation supplémentaire, suffit à provoquer une dérive horizontale illimitée. Un contrôleur actif sur $\phi$ est donc indispensable pour stabiliser le booster.
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La loi de commande $\Delta\phi = -K\,\Delta s_{lat}$ injectée dans le système latéral donne :

    $$\dot{\Delta s}_{lat} = A_{lat}\,\Delta s_{lat} + B_{lat}\,\Delta\phi = (A_{lat} - B_{lat}\,K)\,\Delta s_{lat} = A_{cl}\,\Delta s_{lat}$$

    Le système en boucle fermée est donc gouverné par la matrice $A_{cl} = A_{lat} - B_{lat}\,K$.



    Les deux premiers coefficients de $K$ sont nuls car on ne cherche **pas encore** à corriger la position latérale $x$. On se concentre uniquement sur la stabilisation de l'angle $\theta$. La loi de commande se réduit donc à :

    $$\Delta\phi(t) = -k_\theta\,\Delta\theta(t) - k_\omega\,\Delta\omega(t)$$

    C'est un **correcteur PD** (Proportionnel-Dérivé) sur l'angle :
    - $k_\theta$ : **gain proportionnel** — crée un couple de rappel vers $\theta = 0$
    - $k_\omega$ : **gain dérivé** — amortit les oscillations en s'opposant à la vitesse angulaire

    On procède par essais successifs en analysant l'effet de chaque gain :

    **Effet de $k_\theta$ (gain proportionnel) :**
    - Trop petit → correction lente, le propulseur reste incliné longtemps
    - Trop grand → $\Delta\phi$ dépasse $\pi/2$ (saturation du réacteur, modèle invalide)

    **Effet de $k_\omega$ (gain dérivé) :**
    - Trop petit → oscillations non amorties autour de $\theta = 0$
    - Trop grand → réponse trop lente (sur-amortissement)

    **Règle pratique :** on commence par fixer $k_\omega \approx 2\,k_\theta$ pour avoir un amortissement correct, puis on ajuste $k_\theta$ pour le temps de convergence.
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt, scipy):


    def simulate_lateral_closed_loop(K, t_end=30, s0=None):
        """Simule le système latéral en boucle fermée avec le gain K."""
        if s0 is None:
            s0 = np.array([0.0, 0.0, 45/180*np.pi, 0.0])
    
        A_cl = A_lat - B_lat @ K  # Matrice boucle fermée
    
        def f_closed_loop(t, s):
            return A_cl @ s
    
        sol = scipy.integrate.solve_ivp(
            f_closed_loop, [0, t_end], s0, dense_output=True, max_step=0.01
        )
        return sol.sol

    def plot_controller(K, label="", t_end=30):
        """Trace les résultats de simulation pour un gain K donné."""
        s0 = np.array([0.0, 0.0, 45/180*np.pi, 0.0])
        sol = simulate_lateral_closed_loop(K, t_end=t_end, s0=s0)
        t_vals = np.linspace(0, t_end, 2000)
        states = sol(t_vals)
    
        Delta_x     = states[0, :]
        Delta_theta = states[2, :]
        Delta_phi   = -(K @ states).flatten()  # commande appliquée
    
        A_cl = A_lat - B_lat @ K
        eigs = la.eigvals(A_cl)
    
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
        axes[0].plot(t_vals, Delta_theta * 180/np.pi, 'r-')
        axes[0].axhline(0, color='k', ls='--', alpha=0.5)
        axes[0].set_title(r"$\Delta\theta(t)$ (degrés)")
        axes[0].set_xlabel("t (s)"); axes[0].grid(True)
    
        axes[1].plot(t_vals, Delta_x, 'b-')
        axes[1].axhline(0, color='k', ls='--', alpha=0.5)
        axes[1].set_title(r"$\Delta x(t)$ (m)")
        axes[1].set_xlabel("t (s)"); axes[1].grid(True)
    
        axes[2].plot(t_vals, Delta_phi * 180/np.pi, 'g-')
        axes[2].axhline(90, color='r', ls='--', alpha=0.5, label=r"$\pm 90°$")
        axes[2].axhline(-90, color='r', ls='--', alpha=0.5)
        axes[2].set_title(r"$\Delta\phi(t)$ (degrés)")
        axes[2].set_xlabel("t (s)"); axes[2].legend(); axes[2].grid(True)
    
        stable = np.all(np.real(eigs) < 0)
        plt.suptitle(f"{label} | K={K} | Valeurs propres: {np.round(eigs, 3)} | {'✅ Stable' if stable else 'Instable'}",
                     fontsize=10)
        plt.tight_layout()
        plt.show()
    
        print(f"Valeurs propres A_cl : {eigs}")
        print(f"max|Delta_theta| = {np.max(np.abs(Delta_theta))*180/np.pi:.1f}°")
        print(f"max|Delta_phi|   = {np.max(np.abs(Delta_phi))*180/np.pi:.1f}°")
        return eigs

    # --- Tentative 1 : gains initiaux faibles ---
    print("=== Tentative 1 : k_theta=0.5, k_omega=1.0 ===")
    K1 = np.array([[0, 0, 0.5, 1.0]])
    eigs1 = plot_controller(K1, label="Tentative 1")
    return (plot_controller,)


@app.cell
def _(np, plot_controller):

    print("=== Tentative 2 : k_theta=1.0, k_omega=2.0 ===")
    K2 = np.array([[0, 0, 1.0, 2.0]])
    eigs2 = plot_controller(K2, label="Tentative 2")
    return


@app.cell
def _(A_lat, B_lat, la, np, plot_controller):

    # On cherche une convergence en ~20s -> partie réelle des VPs ~ -0.2
    # Avec k_theta ~ 0.2/g*J et k_omega equilibrant
    print("=== Tentative 3 (finale) : k_theta=0.3, k_omega=1.5 ===")
    K_manual = np.array([[0, 0, 0.3, 1.5]])
    eigs_manual = plot_controller(K_manual, label="Manuel final", t_end=30)

    print("\n--- Résumé du réglage manuel ---")
    print(f"K_manual = {K_manual}")
    A_cl_manual = A_lat - B_lat @ K_manual
    eigs_final = la.eigvals(A_cl_manual)
    print(f"Valeurs propres en BF : {np.round(eigs_final, 4)}")
    stable = np.all(np.real(eigs_final) < 0)
    print(f"Système asymptotiquement stable : {'OUI' if stable else 'NON'}")
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
