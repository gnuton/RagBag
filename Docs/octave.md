# Octave #
![logo](http://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Gnu-octave-logo.svg/240px-Gnu-octave-logo.svg.png)


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

### VARS ###
````
% assign value to var
a = 3;

% remove var from scope
clear var_name

% slice a var - eg: takes first 3 elements from a vector with 5
octave:35> [1 2 3 4 5](1:3)
ans =

   1   2   3

% prints var in scope
octave:19> who
Variables in the current scope:

a    ans

% detailed print of  var in the scope
octave:30> whos
Variables in the current scope:

   Attr Name           Size                     Bytes  Class
   ==== ====           ====                     =====  ===== 
        a              3x2                         48  double
        ans            1x1                          1  logical
        featuresX      4x2                         64  double
        v              3x1                         24  double
        w              2x3                         48  double

Total is 24 elements using 185 bytes


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

% define coloumn vector
octave:13> v = [1; 2; 3]
v =

   1
   2   
   3

octave:14>w=ones(1,3)
w =

   1   1   1
   
octave:15>w=zeros(2,3)
w =

   0   0   0
   0   0   0
   
   
% size of a matrix
octave:8> size(w)
ans =

   2   3

octave:9> size(w,1)
ans =  2

% size of a vector
octave:14> length([1 2 3])
ans =  3


% generates diagonal matrix
octave:2> eye(3)
ans =

Diagonal Matrix

   1   0   0
   0   1   0
   0   0   1
   
% index & matrices
octave:47> a(1,:)
ans =

   1   0   0

octave:48> a(:,1)
ans =

   1
   0
   0

octave:49> a(1,1)
ans =  1
octave:50> a(1,2)
ans =  0

% get the 1st and 3rd row
octave:51> a([1 3],:)
ans =

   1   0   0
   1   0   0

% replace one column
octave:56> a(:,2) = [1; 2; 3];
a =

   1   1   0
   0   2   0
   0   3   1

% adding a new column
octave:59> a = [a,[4; 5; 6]]
a =

   1   1   0   4
   0   2   0   5
   0   3   1   6

% get all element of the matrix as vector
octave:61> a(:)
ans =

   1
   0
   0
   1
   2
   3
   0
   0
   1
   1
   2
   3

% concate matrixes
octave:62> [zeros(3) ones(3)]
ans =

   0   0   0   1   1   1
   0   0   0   1   1   1
   0   0   0   1   1   1

octave:63> [zeros(3); ones(3)]
ans =

   0   0   0
   0   0   0
   0   0   0
   1   1   1
   1   1   1
   1   1   1


````

### RANDOM NUMBER GENERATORS ###
````
% RAND Return a matrix with random elements uniformly distributed on the interval (0, 1).

% RANDN Return a matrix with normally distributed random elements having zero mean and variance one.

````

### FILESYSTEM & HANDLING DATA ###
````
% current dir
octave:16> pwd
ans = /home/gnuton/Downloads

% change working dir
octave:17> cd /tmp
octave:18> pwd
ans = /tmp

% create dir
octave:21> mkdir test;
octave:22> cd test/

% list files in dir
octave:23> ls
featuresX.dat

% loading a file
octave:26> load featuresX.dat
octave:27> who
Variables in the current scope:

a          ans        featuresX  v          w

octave:28> featuresX
featuresX =

   1   2
   3   4
   5   6
   7   8


% saving data to file
s=eye(10); % let's generate a diagonal matrix 
save hello.mat s; % saves the matrix to file

save hello.mat s -ascii % saves the matrix to file in human-readable format


```
## COMPUTING ON DATA ##

### MATRICES ###
```
% Multipling matrices
octave:6> m
m =
   1   2
   3   4
   4   5
octave:10> C=[11; 22]
C =

   11
   22
octave:11> m * C
ans =

    55
   121
   154

% Element-wise moltiplication of matrices
% period denotes element-wise operations in octave
octave:13> m
m =

   1   2
   3   4
   4   5

octave:14> B
B =

   11   22
   33   44
   55   66

octave:15> m .* B
ans =

    11    44         % 1 * 11      2 * 22
    99   176         % 3 * 33      4 * 44 
   220   330

% element-wise squaring
octave:17> m
m =

   1   2
   3   4
   4   5

octave:18> m .^2
ans =

    1    4
    9   16
   16   25
   
% 
octave:19> v = [1; 2; 3]
v =

   1
   2
   3

octave:20>  1./v
ans =

   1.00000
   0.50000
   0.33333

% log(v)o
ctave:22> log(v)
ans =

   0.00000
   0.69315
   1.09861
   
octave:23> exp(v)
ans =

    2.7183
    7.3891
   20.0855

octave:24> abs(v)
ans =

   1
   2
   3
   
octave:25> -v
ans =

  -1
  -2
  -3

% transpose
octave:30> a = [1 2; 3 4; 5 6]
a =

   1   2
   3   4
   5   6

octave:31> a'
ans =

   1   3   5
   2   4   6
```
### VECTORS ###
```
% max
octave:32> a = [1 2 3 5 6]
a =

   1   2   3   5   6

octave:33> max(a)
ans =  6

octave:34> [val, ind] = max(a)
val =  6
ind =  5    % <-- index

% finding item less/bigger than N in an array
octave:39> a < 3
ans =

   1   1   0   0   0

octave:40> find(a < 3)
ans =

   1   2   % <--- those are indexes

% find elements in matrices
octave:52> A
A =

   8   1   6
   3   5   7
   4   9   2

octave:53> [r,c] = find(A >=7)
% this means we got 3 points (1,1) (3,2) (2,3)
r =

   1   % <-- x of the first point
   3
   2

c =

   1  % <-- y of the first point
   2
   3

```

## INTERMEDIATE STUFF##


## ADVANCED STUFF##
````
% Personalize prompt
octave:15> w=randn(1,10000);
octave:16> hist(w)
