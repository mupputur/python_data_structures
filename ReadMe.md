#### Discussion Points 


1. What will happen when the function is called? 
 ```
 When we invoked a function , the compiler will create a stack 
 frame and the function will gets executed inside 
 the stack , once the function execution was done
 the stack will be delated. 
 
 All the function variables (local variables)
 will be stored inside a stack , that is the 
 reason we are not able to access local variables 
 of a function outside of the function definition 
 ```

#### 2. What is recursive function ?
```
Calling same function itself is a recursion, 
When we are implementing a recursion there must be a
one condition that shoud break the recursion
```
#### 3. What will happen if the condition was not met in recursion ?
```commandline
We can encounter memory overflow or stack overflow error
In python we can seen the erro message as maximum recursion depth was reached 
```
#### 4. What is stack behaviour?
```commandline
The stack data structure can work as FILO or LIFO fashion 
```

#### 5. What is the recursion limit ?
```commandline
In python the default recursion limit was 1000 , 
```

#### 6. How we can increase the recursion limit 
```commandline
By using sys module we get or set the recursion limit 

To get :  sys.getrecursionlimit()

To set :  sys.setrecursionlimit()
```

    
