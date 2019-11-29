# Oblig3 IN1910

# H19_project3_sanders_agathebr

## How to run
None of the files take any input. To run a file type:
```
$ python3 [file]
```

To run a test file type:
```
$ pytest [file]
```
or just type
```
$ pytest -v
```


## Part A)

triangle.py - Running the file will generate two plots of the sierpinski triangle.
The first plot uses 3 colors for points corresponding to the corner the point was
derived from. The second plot uses gradual RGB colors for points dependent on
the corner the point was derived from.

sierpinski_color_plot(x, k):

```
Shows the serpinski triangle plottet with n=100_000 points and colors R,G,B chosen for wich corner the point is going towards.
```

sierpinski_alt_colors(x, k):

```
Shows the serpinski triangle plottet with n=100_000 points and colors R,G,B chosen for how far away the point is from the respective corner.
```


## Part B)
chaos_game.py. - Running the file will generate a plot using the chaos game for
a n-gon with n=6, r=1/3 using 100 000-5 points and the matplotlib colormap "twilight".
5 plots using the chaos game for different n-gons is in the map "figures".

```
Showing the chaos_game with a square and r = 1/3. with a color map.
```

test_chaos_game.py - File runs 4 test for the class ChaosGame.

test_init_values():

```
Testing if the init crashes appropriately. When n is not an int, and r is not between 0 and 1.
```

test_called_iterate():

```
Testing if the class crashes appropriately if we try to show the plot befor doing any calculations.
```

test_big_y():

```
Testing that all points is have coordinates smaller then or equal to 1.
```

test_negative_n():

```
Testing if the class crashes appropriately, if we give a negative n
```

## Part C)
fern.py - Running the file generates a plot of a Barnsley fern, using a class
for affine transformation and another class Ferns. The class Ferns makes a list
og n values representing the choices of functions, instead of choosing a function
for each iteration.

For another "fern" using 2 functions with 2 assigned probabilities, use parameters1
and distribution1 in the docstring at the bottom of the program.

main:
```
plots a fern with n=100_100 points  and parameters and distribution from the task. (originaly sugested by Ferns)
```

## Part D)
variations.py - Running the file generates 4 plots scaled to fit on a uniformly
spaced grid (-1, 1).

example_solution():

```
Shows the effect of the Variation class on a mesh. Showing 4 of the varaions, linear, handkercheif, swirl, disc.
```

example_chaos():

```
Shows the effect of the Variation class on a n=4 chaos_game. Showing 4 of the varaions, linear, handkercheif, swirl, disc. With color gradient calculated from the chaosgame.
```

example_fern():

```
Shows the effect of the Variation class on a fern. Showing 4 of the varaions, linear, handkercheif, swirl, disc. In the color green.
```

example_transformation():

```
Shows the effect of the Variation class on a fern, but showing the gradual effect going from linear to swirl.
```
