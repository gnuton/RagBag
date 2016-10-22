# R

```r
## Variables
lo <- TRUE # logic variable
nu <- 1 # numeric variable
ch <- "ciao"   #character variable
nu_as_char <- as.character(nu)

## Vector
v <- c(1,2,3) # or v <- 1:3
v[1] # prints out the first value
bigger_than_two <- v > 2  #returns a vector with element bigger than 2 

# Round numerics
round(1.2345, digits=2) # returns 1.23

## Matrix
m <- matrix(1:20, ncol=4, nrow=5) # creates a 4 by 5 matrix filled with numbers from 1 to 20
dim(m) # returns the n of col and row of the matrix. Works for array and dataframes too

## Factors - Statistical data type which stores categorical (or discrete/ no continuous) vars (a kind of enum)
student_status <- c("student", "not student", "student", "not student")
categorical_student <- factor(student_status)
levels(categorical_student) # returns the two possible variables "student", "not student"

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
planet_df <- data.frame(planets, diameter, diameter)
planet_df[1, c(2,3)] # select the values in the first row and second and third columns
planet_df$diameter # select the column diameter

# get the size of the dataframe with dir
dir(mtcars)

# Code continuos numeric data in categorical - here we create a new variable and we set hight
# if the contiuous one is bigger than 20
my_dataframe$the_new_categ_data[my_dataframe$the_continuosvar <= 20] <- "high"

# Display frequency table
table(your_dataframe) # returns a matrix with the frequency for each category

# Making a bar graph
barplot(table(my_dataframe$the_var_to_plot) # polots a barplot from a frequency table
#  If you like to cusomize the label on the Y or the X you can pass those as argument 
barnames <- c("automatic", "manual")
barplot(table(cars$am), ylab="number of cars", names.arg= barnames)

# Plotting a Histogram
hist(mtcars$carb, main = "title", ylim=c(0, 20), col="red", xlab="The X label")

# calculate mode mean and median
mode <- sort(table(mydataframe$thevar), decreasing= TRUE)[1]
mean(mydataframe$thevar)
median(mydataframe$thevar)

# quantiles
my_data <- c(21.0,21.0 ,22.8 ,21.4 ,18.7 ,18.1 ,14.3 ,24.4 ,22.8 ,19.2 ,17.8 ,16.4 ,17.3 ,15.2 ,10.4)
quantile(my_data) # returns lowest, 1st quartile, 2nd, 3rd, highest val
 
# Make a boxplot
boxplot(my_data)

# Calculate the interquartile IQR and standard deviation SD
IQR(my_data)
sd(my_data)

# Calculate Z-scores
my_data <- c(21.0,21.0 ,22.8 ,21.4 ,18.7 ,18.1 ,14.3 ,24.4 ,22.8 ,19.2 ,17.8 ,16.4 ,17.3 ,15.2 ,10.4)
(my_data - mean(my_data)/sd(my_data)


## Regression 
### Plot a graph
plot(women$height, women$weight, main="Heights and Weights") # where women is a dataframe

### Contigency table
table(my_dataframe)

### Correlation between two variables (those are vector of vars eg:heights vs weights)
corr(dataframe$heights, dataframe$weights) # outputs the correlation. a single number which describes the degree of relationship btw the vars
 
#### Squared Error betwen line and actual values
y1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # predicted values of y according to line 1
y <- c(3, 2, 1, 4, 5, 10, 8, 7, 6, 9)   # actual values of y
sum((y1-y)^2) # calculate the squared error of line 1

### Calculate regression line intercept(b) and slope(a). Y = a +bX
plot(x,y) # draws scattered plot
line <- lm(y ~ x) # returns the coefficients a and b of the regression line
abline(line) # draws the regression line

## List
li <- list(1,c(2,3,4),TRUE)
li[[2]][1] # grabs the second element (vector) and prints out the second element in the vector

# Grab the first column of the third component of `my_list` and print it to the console
my_list[[3]][,1]
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


## Functions
# arguments can be passed by position or by name
grades <- c(1,2,3)
mean(grades) # runs mean by position
mean(x=grades) # runs mean by name

#  Creating a new function
multiply_a_b <- function(a, b) {
    return (a*b)
}
result= multiply_a_b(3,7) # call the function multiply_a_b and store the result into a variable result

## Getting data into R
# 1. read.table: Reads in tabular data such as txt files
# 2. read.csv: Read in data from a comma-separated file format
# 3. readWorksheetFromFile : Reads in an excel worksheet
# 4. read.spss: Reads in data from .sav SPSS format.
cars <- read.csv("http://the_url/read.csv", sep=";") # reads data from csv

## Handling local dirs
getwd() # returns the current Dir
setwd("/tmp") # chaange working dir

## Importing R packages
# Install the package ggplot2 using install.packages("ggplot2")
# Load the package ggplot2 using library(ggplot2) or require(ggplot2)


## Getting Help
help(function_name) # or ?help
```

## Reference ##
http://egret.psychol.cam.ac.uk/statistics/R/basicstats.html
http://ideone.com/

