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

   1   2

octave:48> a(:,1)
ans =

   1
   3
   5

octave:49> a(1,1)
ans =  1
octave:50> a(1,2)
ans =  2

% get the 1st and 3rd row
octave:51> a([1 3],:)
ans =

   1   2
   5   6

% replace one column
octave:56> a(:,2) = [1; 2; 3];
octave:57> a
a =

   1   1
   3   2
   5   3

% adding a new column
octave:59> a = [a,[1; 2; 3]];
octave:60> a
a =

   1   1   1
   3   2   2
   5   3   3

% get all element of the matrix as vector
octave:61> a(:)
ans =

   1
   3
   5
   1
   2
   3
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
## INTERMEDIATE STUFF##


## ADVANCED STUFF##
````
% Personalize prompt
octave:15> w=randn(1,10000);
octave:16> hist(w)
