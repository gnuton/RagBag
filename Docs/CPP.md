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
#### Scope ####
```cpp
#include <iostream>

using namespace std;

int i = 1; // GLOBAL VAR

int main() { // SCOPE 1 STARTS
  cout << "Scope global:" << i << endl;
  int i = 2; //  
  cout << "Scope 1:" << i << endl;
  {  // SCOPE 2 START
    int i = 3;
    cout << "Scope 2:" << i << endl;
  }  // SCOPE 2 END
  
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
Are simple variable storing memory addresses. They have have a fixed size depending on the CPU/OS.
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


