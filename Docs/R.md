# R #

# Variables
lo <- TRUE # logic variable
nu <- 1 # numeric variable
ch <- "ciao"   #character variable
nu_as_char <- as.character(nu)

# Vector
v <- c(1,2,3)
v[1] # prints out the first value
bigger_than_two <- v > 2  #returns a vector with element bigger than 2 

# Matrix
m <- matrix(1:20, ncol=4, nrow=5) # creates a 4 by 5 matrix filled with numbers from 1 to 20

## Basic maths ##
````
sum(x) # adds up a vector
x^y
sqrt(x)
log(x) # default is natural log
log(x, base=y) # any sort of log
log2(x) # short cut
log10(x) # short cut
exp(x) # e^x
factorial(x)
````

## Reference ##
http://egret.psychol.cam.ac.uk/statistics/R/basicstats.html
