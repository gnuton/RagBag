# Octave #
![logo]()


## BASICS ##
### Comments ###
% this is a comment

### Do you need help? Ask for it ###
````
octave:17> help 

  For help with individual commands and functions type

octave:18> help rand
'rand' is a built-in function from the file libinterp/corefcn/rand.cc
````

### Avoid answers ###
Using ; at the end of the command avoids octave to print the result of the operation to the console.

### Operations ###
````
>1+1
ans =  2

> 1/2
ans =  0.50000
````

### LOGICAL OPERATRRS ###
````
octave:4> 1 || 1
ans =  1
octave:5> 1 || 0
ans =  1
octave:6> 0 || 0
ans = 0
octave:7> 1 && 1
ans =  1
octave:8> 1 && 0
ans = 0
octave:9> 0 && 0
ans = 0

````

### PLOTTING GRAPHS ###
````
% HISTOGRAMS
octave:15> w=randn(1,10000);
octave:16> hist(w)

````

### VECTORS AND MATRIcES ###
````
% define matrix
octave:12> m = [1 2 3; 4 5 6; 7 8 9]
m =

   1   2   3
   4   5   6
   7   8   9

% define vector
octave:13> v = [1 2 3]
v =

   1   2   3


````
