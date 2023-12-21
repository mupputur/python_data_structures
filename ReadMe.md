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

#### 6. When we create an object or when we create an instance of a class what will happen?
```commandline
At the time of object creation the __init__ method or constrcutor 
can be invoked , the constructor can be used to initlize the 
common attributes of an object 
```

#### What is __repr__ method does?
```commandline
To represent an object we can override __repr__ method
For example , when we have customer class or object 
customer will having sevaral attributes but we can represent 
customer object as his name and id when we directly calls the object 
```

#### 8. What is the differance between __str__ and __repr__?
    
