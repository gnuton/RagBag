# R

```r
## Variables
lo <- TRUE # logic variable
nu <- 1 # numeric variable
ch <- "ciao"   #character variable
nu_as_char <- as.character(nu)

## Vector
v <- c(1,2,3)
v[1] # prints out the first value
bigger_than_two <- v > 2  #returns a vector with element bigger than 2 


## Matrix
m <- matrix(1:20, ncol=4, nrow=5) # creates a 4 by 5 matrix filled with numbers from 1 to 20


## Factors - Statistical data type which stores categorical (or discrete/ no continuous) vars
student_status <- c("student", "not student", "student", "not student")
categorical_student <- factor(student_status)


## Dataframes -dataset of different types
> mtcars
                   mpg cyl disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
#  head(mtcars): this by default prints the first 6 rows of the dataframe
#  tail(mtcars): this by default prints the last 6 rows to the console
#  str(mtcars): this prints the structure of your dataframe
#  dim(mtcars): this by default prints the dimensions, that is, the number of rows and columns of your dataframe
#  colnames(mtcars): this prints the names of the columns of your dataframe
#  to create a data frame
planets <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
planet_df <- data.frame(planets, diameter)

## Basic maths ##
sum(x) # adds up a vector
x^y
sqrt(x)
log(x) # default is natural log
log(x, base=y) # any sort of log
log2(x) # short cut
log10(x) # short cut
exp(x) # e^x
factorial(x)
```

## Reference ##
http://egret.psychol.cam.ac.uk/statistics/R/basicstats.html
