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

    return np, plt, sci


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous définissons les constantes ( constante de gravité, la masse totale et la longueur entière du booster ) avec les valeurs dans l'énoncé.
    """)
    return


@app.cell
def _():
    g = 1.0  # gravité [m/s^2]
    M = 1.0  # masse totale [kg]
    l = 2.0  # longueur [m]

    print(f"Constantes: g={g}, M={M}, l={l}")
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On considère une force \(\vec{F}\) de norme \(f\), appliquée avec un angle total \((\theta + \phi)\) par rapport à l’axe vertical du repère orthonormé \(R(G,\vec{e_x},\vec{e_y})\).

    Les composantes cartésiennes de cette force sont obtenues par projection trigonométrique :
    """)
    return


@app.cell
def _(np):
    def forces_cartesian(f, theta, phi):
        f_x = f * np.sin(theta + phi)
        f_y = -f * np.cos(theta + phi)
        return f_x, f_y

    return (forces_cartesian,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le mouvement du centre de masse \((x,y)\) est régi par la deuxième loi de Newton appliquée selon les deux axes du repère orthonormé \(R(G,\vec{e_x},\vec{e_y})\).

    Le système étudié est soumis aux forces extérieures suivantes :
        Bilan de force :
    - la force de poussée \(\vec{F}\) exercée par le réacteur,
    - le poids \(\vec{P}\) dû à la gravité.



    ### Projection sur l’axe \(x\)

    En appliquant la deuxième loi de Newton sur l’axe horizontal :

    \[
    \sum F_x = M\ddot{x}
    \]

    La seule force selon l’axe \(x\) est la composante horizontale de la poussée :

    \[
    f_x = f\sin(\theta+\phi)
    \]

    Ainsi :

    \[
    M\ddot{x} = f_x
    \]

    d’où :

    \[
    \boxed{\ddot{x} = \frac{f_x}{M}}
    \]


    En appliquant la deuxième loi de Newton sur l’axe vertical :

    \[
    \sum F_y = M\ddot{y}
    \]

    Les forces appliquées selon l’axe vertical sont :

    - la composante verticale de la poussée \(f_y\),
    - le poids \(Mg\), dirigé vers le bas.

    On obtient alors :

    \[
    M\ddot{y} = f_y - Mg
    \]

    avec :

    \[
    f_y = f\cos(\theta+\phi)
    \]

    Ainsi :

    \[
    \boxed{\ddot{y} = \frac{f_y}{M} - g}
    \]

    ---
    """)
    return


@app.cell
def _(M, forces_cartesian, g):

    def dynamique_centre_masse(f, theta, phi, M=M, g=g):
        f_x, f_y = forces_cartesian(f, theta, phi)
        x_dotdot = f_x / M
        y_dotdot = (f_y / M) - g

        return x_dotdot, y_dotdot


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell
def _(M, l):
    J = (1.0 / 12.0) * M * l**2
    print(J)
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
    Le moment dynamique autour du centre de masse donne :

    $$\sum \vec{M}_G = J \cdot \ddot{\theta}$$

    Avec notre convention géométrique, le couple dû à la poussée appliquée à la base vaut :

    $$\sum \vec{M}_G= \frac{\ell  f \sin(\phi)}2$$

    Donc :

    $$\ddot{\theta} = \frac{\ell f \sin(\phi)}{2J}$$
    """)
    return


@app.cell
def _(np):

    def system_dynamics(J, l, f, phi):
        sum_moments = l * f * np.sin(phi)/2
        theta_dotdot = sum_moments / J
        return theta_dotdot


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
    Nous avons déjà trouvé précédemment (d'après le bilan des forces) les accélerations suivant x et y et (d'après la loi des moments) l'accélération angulaires que nous rassemblons dans le vecteur F.
    L'espace d'état possède une dimension $n = 6 :$$s = \begin{pmatrix} x \\ v_x \\ y \\ v_y \\ \theta \\ \omega \end{pmatrix} \in \mathbb{R}^6$Le champ de vecteurs $F : \mathbb{R}^{6+2} \to \mathbb{R}^6$ tel que $\dot{s} = F(s, f, \phi)$ est défini par :$F(s, f, \phi) = \begin{pmatrix} v_x \\ \frac{f \sin(\theta+\phi)}{M} \\ v_y \\ \frac{-f \cos(\theta+\phi)}{M} - g \\ \omega \\ \frac{\ell f \sin(\phi)}{2J} \end{pmatrix}$
    """)
    return


@app.cell
def _(J, M, forces_cartesian, g, l, np):
    def vector_field(t, s, f, phi):

        x, vx, y, vy, theta, omega = s
   
        f_x, f_y = forces_cartesian(f=f, theta=theta, phi=phi)

        ax = f_x / M
        ay = -f_y / M - g

        theta_dotdot = (l * f * np.sin(phi))/2*J
    

        return np.array([
            vx,     # dx/dt
            ax,     # dvx/dt
            vy,     # dy/dt
            ay,     # dvy/dt
            omega,  # dtheta/dt
            theta_dotdot,  # domega/dt
        ], dtype=float)

    return (vector_field,)


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""
        mo.md(r\"""
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
        \""")
        """
    )
    return


@app.cell
def _(np, sci, vector_field):
    def redstart_solve(t_span, y0, f_phi, max_step=0.01):

        def dynamics(t, s):
            f, phi = f_phi(t, s)
            return vector_field(t, s, float(f), float(phi))

        ivp = sci.solve_ivp(
            fun=dynamics,
            t_span=t_span,
            y0=np.asarray(y0, dtype=float),
            method="RK45",
            dense_output=True,
            max_step=max_step,
        )

        if not ivp.success:
            raise RuntimeError(f"Echec solve_ivp: {ivp.message}")

        return ivp.sol

    

    return (redstart_solve,)


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
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
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

    return


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
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


if __name__ == "__main__":
    app.run()
