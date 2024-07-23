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

- How to enable debug flags (examples of DRAM and Exec) [Not doing this]
- `--debug-help`
- Adding a new debug flag
- Functions other than DPRINTF
- Panic/fatal/assert
- gdb? Mahyar's opinion: does not sound interesting or exclusive to gem5 and hard to teach.

---
<!-- _class: title -->

## DebugFlags: Debugging and Logging in gem5

***IMPORTANT***: This slide deck builds on top of what has already been developed in [Introduction to SimObjects](01-sim-objects-intro.md).

---

## DebugFlags

`DebugFlags` facilitate debug printing. Debug printing is useful for debugging models in gem5 and logging.

Each `DebugFlag` enables printing certain statements within the gem5 code base. Run the following command in the base gem5 directory. to see all the available `DebugFlags` in gem5.

```sh
./build/NULL/gem5.opt --debug-help
```

You should see an output like below.

```cpp
// record with asciinema Mysore or whoever this slide deck is assigned to.
// add some prose on what the output shows.
```

---
<!-- _class: small-code -->

## DebugFlags: HelloExampleFlag

To define a new `DebugFlag` in gem5, you have to just simply define it in **any** `SConscript` in the gem5 directory. However, it is convention that `DebugFlags` are defined in the same `SConscript` that registers `SimObjects` that are relevant to the `DebugFlag`.

To define a new `DebugFlag` that we will use to print debug/log statement in `HelloSimObject`, open `src/bootcamp/hello-sim-object/SConscript` in your editor of choice and add the following line.

```python
DebugFlag("HelloExampleFlag")
```

Adding this line will create a new **auto-generated** header file (with the same name as the `DebugFlag`) that defines the `DebugFlag` in C++.

---
<!-- _class: small-code -->
## DebugFlags: Using HelloExampleFlag in Code

One of the functions in gem5 that allows for debug printing is `DPRINTF` will let you print a formatted string if a certain `DebugFlag` is enabled (more on how to enable `DebugFlags` later). `DPRINTF` is defined in `src/base/trace.hh`. Make sure to include it every time you want to use `DPRINTF`.

Now let's get to actually adding `HelloExampleFlag` in C++. As I mentioned, the header files for `DebugFlags` are auto-generated. For now, trust that the header file for `HelloExampleFlag` will be in `build/NULL/debug/HelloExampleFlag.hh` when we recompile gem5.

Let's include the header files in `hello_sim_object.cc` by adding the following lines. Remember to follow the right order of includes!

```cpp
#include "base/trace.hh"
#include "debug/HelloExampleFlag.hh
```

Now let's add a simple `DPRINTF` statement inside the constructor of `HelloSimObject` to print `Hello from ...`. Do it by adding the following line after the `for-loop`. **NOTE**: `__func__` will return the name of the function we're in as a string.

```cpp
    DPRINTF(HelloExampleFlag, "%s: Hello from HelloSimObject's constructor!\n", __func__);
```

---
<!-- _class: small-code -->

## DebugFlags: How Files Look Like

Below is how `src/bootcamp/hello-sim-object/SConscript` should look like after the changes.

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

#include "base/trace.hh"
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

## DebugFlags: After Adding HelloExampleFlag

Now, our `HelloExampleFlag` should be listed whenever we print debug help from gem5. Let's run the following command in the base gem5 directory to verify that our `DebugFlag` is added.

```sh
./build/NULL/gem5.opt --debug-help
```

Below shows an expected output of running the following command.

```cpp
// Mysore of whoever is assigned please record with asciinema
// add prose that the DebugFlag is added.
```

---
<!-- _class: small-code -->

## Enabling DebugFlags: Using Configuration Script

To enable a `DebugFlag` you can import `flags` from `m5.debug` and access the flag by indexing `flags`. You can enable and disable flags by calling `enable` and `disable` methods. Below is an example of how your `second-hello-example.py` should look like if you want to enable `HelloExampleFlag`. **CAUTION**: Do **not** make this change in your configuration script for now.

```python
import m5
from m5.debug import flags
from m5.objects.Root import Root
from m5.objects.HelloSimObject import HelloSimObject


root = Root(full_system=False)
root.hello = HelloSimObject(num_hellos=5)

m5.instantiate()

flags["HelloExampleFlag"].enable()

exit_event = m5.simulate()

print(f"Exited simulation because: {exit_event.getCause()}.")
```


---

## Enabling DebugFlags: Using Command Line

Alternatively you can pass `--debug-flags=[comma-separated list of DebugFlags]` to your gem5 binary when running your configuration script. As an example, below is a shell command that you can use to enable `HelloExampleFlag` (like always run it in the base gem5 directory).

**NOTE**: Make sure to pass it before passing the configuration script to gem5.

```sh
./build/NULL/gem5.opt --debug-flags=HelloExampleFlag configs/bootcamp/hello-sim-object/second-hello-example.py
```

---

## Simulate: With and Without HelloExampleFlag

```cpp
// Mysore of whoever is assigned please record with asciinema
// add prose on how to enable a DebugFlag and compare and contrast two outputs.
```
<!-- record with asciinema -->

---
<!-- _class: small-code -->

## Assertions in gem5

I strongly recommend using [`assert`](https://www.geeksforgeeks.org/assertions-cc/) and [`static_assert`](https://www.geeksforgeeks.org/understanding-static_assert-c-11/) when developing for gem5. They help you find assumptions you hold that might not be true as well as help you find your development mistakes early. `assert` and `static_assert` are standard C++ functions that you can (and are strongly encouraged to) use while developing in gem5.

`fatal`, `fatal_if`, `panic`, and `panic_if` are gem5's specific `assert like` functions that allow you to print an error messages. gem5 convention is use `fatal` and `fatal_if` to assert assumptions on user inputs (similar to `ValueError`). As an example if a user tries to configure your SimObject with negative capacity you can use `fatal` or `fatal_if` in your `SimObject` to let the user (most probably yourself) know of their mistake. Below shows an example of doing this with `fatal` and `fatal_if`.

```cpp
if (capacity < 0) { fatal("capacity can not be negative.\n"); }
\\ OR
fatal_if(capacity < 0, "capacity can not be negative.\n");
```

You should use `panic`, and `panic_if` to catch developer mistakes. We will see examples of them in [Ports](04-ports.md).

---

### Other Debugging Facilities in gem5

```cpp
// Mysore or whoever this is assigned to do a little bit of research on other debug printing in gem5.
// src/base/trace.hh
// https://www.gem5.org/documentation/learning_gem5/part2/debugging/
```
