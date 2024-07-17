---
marp: true
paginate: true
theme: gem5
title: Debugging and Debug Flags
---

<!-- _class: title -->

## Debugging and debug flags

---

## We will cover

- How to enable debug flags (examples of DRAM and Exec)
- `--debug-help`
- Adding a new debug flag
- Functions other than DPRINTF
- Panic/fatal/assert
- gdb?

---
<!-- _class: title -->

## DebugFlags

---
<!-- _class: small-code -->

## DebugFlags: HelloExampleFlag

DebugFlags facilitate debug printing useful for debugging models in gem5 and logging.

To define a new DebugFlag in gem5, you have to just simply define in **any** SConscript in the gem5 directory. However, it is convention that DebugFlags are defined in the same SConscript that registers SimObjects that are relevant to the DebugFlag.

To define a new DebugFlag that we will use to print debug/log statement in HelloSimObject, open `src/bootcamp/hello-sim-object/SConscript.py` in your editor of choice and add the following line.

```python
DebugFlag("HelloExampleFlag")
```

Adding this line will create a new **auto-generated** header file (that has the same name as the DebugFlag) that defines the DebugFlag in C++.

---
<!-- _class: small-code -->
## DebugFlags: Using HelloExampleFlag in Code

One of the functions in gem5 that allows for debug printing is `DPRINTF` will let you print a formatted string if a certain debug flag is enabled. Later, we will learn about what it means for a debug flag to be enabled.

Now let's get to actually adding HelloExampleFlag in C++. As I mentioned, the header files for DebugFlags are auto-generated. For now trust that the header file for HelloExampleFlag will be in `build/NULL/debug/HelloExampleFlag.hh` when we recompile gem5.

Let's include the header file in hello_sim_object.cc by adding the following line to the `#include ...` statements. Remember to follow the right order of includes!

```cpp
#include "debug/HelloExampleFlag.hh
```

Now let's add a simple DPRINTF statement inside the constructor of HelloSimObject to print `Hello from ...`. Do it by adding the following line after the `for-loop`. **NOTE**: `__func__` will return the name of the function we're in as a string.

```cpp
    DPRINTF(HelloExampleFlag, "%s: Hello from HelloSimObject's constructor!\n", __func__);
```

---
<!-- _class: small-code -->

## DebugFlags: How Files Look Like

Below is how `src/bootcamp/hello-sim-object/SConscript.py` should look like after the changes.

```python
Import("*")

SimObject("HelloSimObject.py", sim_objects=["HelloSimObject"])

Source("hello_sim_object.cc")

DebugFlag("HelloExampleFlag")
```

Below is how `src/bootcamp/hello-sim-object/hello_sim_object.cc` looks like with changes

```cpp
#include "bootcamp/hello-sim-object/hello_sim_object.hh"

#include <iostream>

#include "debug/HelloExampleFlag.hh"

HelloSimObject::HelloSimObject(const HelloSimObjectParams& params):
    SimObject(params)
{
    for (int i = 0; i < params.num_hellos; i++) {
        std::cout << "i: " << i << ", Hello from HelloSimObject's constructor!" << std::endl;
    }
    DPRINTF(HelloExampleFlag, "%s: Hello from HelloSimObject's constructor!\n", __func__);
}
```

---

## Let's Recompile

Now, let's recompile gem5 with the command below. After compilation is done, you should be able to find the header file in `build/NULL/debug/HelloExampleFlag.hh`.

```sh
scons build/NULL/gem5.opt -j$(nproc)
```

And here is a snippet of the contents of `build/NULL/debug/HelloExampleFlag.hh`.

```cpp
// Mysore put definition of HelloExampleFlag here.
```

---

### Simulate: With and Without HelloExampleFlag

<!-- record with asciinema -->
