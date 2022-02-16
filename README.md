# simple-division-fractal
This is quite a simple idea. The code generates x and y lists and their graph, given a base d and number of iterations. The base d will be used as a divisor and x will run through numbers 1 to number of iterations. The iteration will generate y which is number of times x can be fully divided by d. So if base d=2, we get y=[0,1,0,2,0,1,0,3,0,1,0,2,0,1,0,3,0..] for x=1,2,3,4...17. 
Here is a graph with base 2 and 128 iterations.

![base_2_128](https://user-images.githubusercontent.com/53497039/152775551-7e5919a3-fecd-456e-ba6e-552b542a3db8.png)

Here is another with base 5 and 250 iterations

![base_5_250](https://user-images.githubusercontent.com/53497039/152775883-6932a22a-13cb-4d6c-8d3e-df808184b42b.png)

It appears that it takes (base - 1) spikes on one level before it shoots higher or lower after. This is obviously based on the fact that between any two integers, there are n-1 non-divisors of n).

Calling it fractal in a broader sense - the potential to be self similar on any scale though it will usually be based on finite points.
