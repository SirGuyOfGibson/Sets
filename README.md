# Sets Visualizer
    ~julia (implemented by using run_julia.py to launch)
    ~mandelbrot

# Dependency
    ~pygame

## Setting up start script written in Ubuntu
    chmod +x run

### Launch Python Interpretor run_julia.py
    ./run

### Interpretor Set Commands
    update()
    julia -julia set object from julia.py
    display -screen object running pygame

# Julia set overview
    Julia sets are computed by calculating the distance a coordinate travels from the origin of the complex plane
    when the corrdinate is iterated through( Zn-1=Zn*Zn + C )Zn being the nth coordinate of the set.
    Coordinates that 'escape' to infinity reach beyond the size of the screen and painted as the background color
    Coordinates that stay within the bounds of (-2,2)real and (-2,2)imaginary are considered part of the Julia set,
    and are assigned a color with basic modulo algo derived from distance the vector reached from the origin
    as it iterated through the squaring process (still learning this mechanism)
    The constant C of this iteration is the unique variable that is added to both the real and imaginary parts that
    get squared in the iteration.

# Easy to Use: Much Variety of Results
    ~clicking,in the display, sets the constant to the coordinates clicked on, this value is displayed in
        upper left hand corner of the display
    ~alternitively, julia.P and julia.Q variables can changed and then update() will refresh screen from interpretor
    ~julia.max_iterations is defaulted to 32 but can be increased for higher resolution calculations
    ~sometimes a low max iterations produces better looking images
    ~to change the density of colors, julia.color_density=100 and then of course update() to see change

# Thats about it to seeing Julia sets, more to come
    Cool Coordinates to start
    P=0.2685
    Q=-0.0035
    color_density=20

    Just click around and change the color densities or max_iterations
    Saved images in Saved/ directory, display.save(name) to save cool finds

exit() -to leave python interpretor and quit pygame display
