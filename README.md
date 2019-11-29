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

## Part B)
chaos_game.py - Running the file will generate a plot using the chaos game for
a n-gon with n=6, r=1/3 using 100 000-5 points and the matplotlib colormap "twilight".
5 plots using the chaos game for different n-gons is in the map "figures".

test_chaos_game.py - File runs 4 test for the class ChaosGame.

## Part C)
fern.py - Running the file generates a plot of a Barnsley fern, using a class
for affine transformation and another class Ferns. The class Ferns makes a list
og n values representing the choices of functions, instead of choosing a function
for each iteration.

For another "fern" using 2 functions with 2 assigned probabilities, use parameters1
and distribution1 in the docstring at the bottom of the program.

## Part D)
variations.py - Running the file generates 4 plots scaled to fit on a uniformly
spaced grid (-1, 1).
