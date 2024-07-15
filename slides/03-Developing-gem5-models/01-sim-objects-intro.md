---
marp: true
paginate: true
theme: gem5
title: Developing SimObjects in gem5
---

<!-- _class: title -->

## Developing `SimObjects` in gem5

<!-- Add a topic sentence here.-->

---

## The Path Ahead

<!-- fill this in after done -->
- HelloSimObject
- GoodByeSimObject

---

## We will cover

- Development environment, code style, git branches
- The most simple `SimObject`
- Simple run script
- How to add parameters to a `SimObject`

---

## What is a SimObject?

`SimObject` is gem5's name for a simulated model.
We use SimObject and its children classes (e.g. `ClockedObject`) to model computer hardware components.
SimObject facilitates the following in gem5:

- Defining a model: e.g. a cache
- Parameterizing a model: e.g. cache size, associativity
- Gathering statistics: e.g. number of hits, number of accesses

---

## SimObject in Code

In a gem5 build, each `SimObject` based class has *some number* of files relating to it.

- SimObject definition file: Python(ish) script:
  - Represents the model at the highest level.
  Allows instantiation of the model and interfacing with the C++ backend.
  It defines the sets of parameters for the model
  It will interface with the C++ backend.
- SimObject header file: C++ header file (.hh extension):
  - Defines the SimObject class in C++.
  Strongly tied to SimObject definition file.
- SimObject source file: C++ source file (.cc extension):
  - Implements the SimObject functionalities.
- SimObjectParams header file: **Auto-generated** C++ header file (.hh) from SimObject definition:
  - Defines a C++ struct storing all the parameters of the SimObject`.

---

### HelloSimObject

We will start building our first SimObject called `HelloSimObject` and look at one of the SimObject files.

<!-- Fill in these steps -->

---

### SimObject Definition File

Let's create a python file for our SimObject under:
`src/bootcamp/hello-sim-object/HelloSimObject.py`.

To do this run the following commands in the base gem5 directory:

```sh
mkdir src/bootcamp
mkdir src/bootcamp/hello-sim-object
touch src/bootcamp/hello-sim-object/HelloSimObject.py
```

---

Open `src/bootcamp/hello-sim-object/HelloSimObject.py` in your editor of choice.

In `HelloSimObject.py` we will define a new class that represents our HelloSimObject.
We need to import the definition for SimObject from `m5.objects.SimObject`.
Add the following line to HelloSimObject.py to import the definition for SimObject.

```python
from m5.objects.SimObject import SimObject
```
