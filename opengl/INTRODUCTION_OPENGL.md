# What is OpenGL

- specification, developed and maintained by the Khronos Group.
- The OpenGL specification specifies exactly what the result/output of each function
- Each graphics card that you buy supports specific versions of OpenGL which are the versions of OpenGL developed specifically for that card (series).
- whenever OpenGL is showing weird behavior that it shouldn't, this is most likely the fault of the graphics cards manufacturers

# Core-profile vs Immediate mode

- The immediate mode is really easy to use and understand, but it is also extremely inefficient -> deprecated since OpenGL 3.2
- The advantage of learning the modern approach (Core-profile) is that it is very flexible and efficient. 

# Programming notes

- A great feature of OpenGL is its support of extensions.
- OpenGL is by itself a large state machine: a collection of variables that define how OpenGL should currently operate.
- 