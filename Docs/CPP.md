# C++ #
![logo](https://www.thenewboston.com/photos/users/27/original/f34559fb85ab31961e60e1928bf4e0ca.jpg)

## Getting started ##
To compile C++ code enabling C11 features you can run the following command
```
g++ mycode.cpp -std=c++11
```
A minimal C++ application would be: 
```cpp
#include <iostream>

using namespace std;

int main() {
  cout << "Hello world";
  return 0; // exit without errors.
}

```
## Basics ##
### Variables ###
Variables are valid just in a certain scope
#### Scope & Namespaces####
Braces define scopes. Outside functions we can create namespace that define a scope for variables and functions. 
```cpp
#include <iostream>

using namespace std;

namespace my_namespace {
  void myfun(int i) {}
}

int i = 1; // GLOBAL VAR

int main() { // SCOPE 1 STARTS
  cout << "Scope global:" << i << endl;
  int i = 2; //  
  cout << "Scope 1:" << i << endl;
  {  // SCOPE 2 START
    int i = 3;
    cout << "Scope 2:" << i << endl;
  }  // SCOPE 2 END
  
  my_namespace::myfun(1);
} // SCOPE 1 ENDS

```

#### Var size ####
```cpp
 sizeof(char) == 1; // 1 bytes in C++  and sizeof(int) in C
 sizeof(int) == 4; // 4 bytes or 32 bits 
 sizeof(float) == 4;
 sizeof(double) == 8; // 8 bytes or 64 bit
 sizeof(long) == 8;
 sizeof(char*) == 8; // size of a pointer depends on CPU/OS. 8 for a 64bit arch OS
```

#### Pointers ####
Are simple variables storing memory addresses. They have have a fixed size depending on the CPU/OS.
```cpp
// Pointer definitions, read this definition backwards
// when you initialize a pointer, the pointer variable doesn't point to any valid address it points to 0.
int* a; // create a pointer to an integer and initialize it to nullptr
int* a = NULL; // NOT NICE! Use nullptr if you are using C++11
int const *a; // pointer to const int
int * const a; // const pointer to int
int const * const a; // const pointer to const int

// The first const can be on either side of the type so:
const int * == int const *
const int * const == int const * const

// pointers can point to other pointers
int ** // pointer to pointer to int
int ** const // a const pointer to a pointer to an int
int * const * // a pointer to a const pointer to an int
int const ** // a pointer to a pointer to a const int
int * const * const // a const pointer to a const pointer to an int
```
#### Strings ####
```cpp
```

#### Casting ####
```cpp
```

#### Reading Command line arguments ####
When you run your app from command line as:
```
gnuton@Jeremia:/tmp$ ./a.out  1 2 3
ARGC4
ARG ./a.out
ARG 1
ARG 2
ARG 3
```

```cpp
#include <iostream>

using namespace std;

int main(int argc, char** argv){
  cout << "ARGC" << argc << endl;
  for (int x=0; x < argc; x++){
    cout << "ARG " << *argv << endl;
    ++argv;
  }
}
```

## Functions ##
### Default function argument ###
```cpp
void myfunc1(int a=1, int b=1) { }  // OK
void myfunc2(int a, int b=1) { }    // OK
void myfunc3(int a=1, int b) { }  // WRONG: default args must be at the end of the argument list
```

### Overloading ###
C++ functions are stricly typed. That means that we can our code can have two or more functions with the same name, same number of arguments but different var type

```cpp
void myfunc(int a) {
  cout << "got int" << endl;
}

void myfunc(char const* a) {
  cout << "got string" << endl;
}

void myfunc(double a) {
  cout << "got double" << endl;
}

void myfunc(float a) {
  cout << "got float" << endl;
}

// in the main
myfunc(1.3f); // got a float
myfunc("ciao"); // got a string

```

#### Ellipses ####
Used when we get a un undefined number of arguments.
```cpp
```

## Input/Output ##
### Reading and Writing to Console ###
```cpp
#include <iostream>

using namespace std;

int main() {
  // Read integer
  int i;
  cout << "Insert a number" << endl;
  cin >> i;
  cout << "Thanks" << endl;
  cerr << "Used for errors" << endl;
  // read string with spaces
  string s;
  cout << "Insert your full name" << endl;
  getline(cin, s);
  cout << "Thanks again " << s << endl;
}

```

### Reading and Writing to File ###
```cpp
```

