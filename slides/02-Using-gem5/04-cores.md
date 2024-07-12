---
marp: true
paginate: true
theme: gem5
title: Modeling CPU cores in gem5
---

<!-- _class: title -->

## Modeling CPU cores in gem5

---

## Outline

- CPU models in gem5​
  - AtomicSimpleCPU, TimingSimpleCPU, O3CPU, MinorCPU, KvmCPU​

- Using the CPU models​
  - Set-up a simple system with two cache sizes and three CPU models​

- Look at the gem5 generated statistics​
  - To understand differences among CPU models

---

<style scoped>
  h2{
    margin-bottom: 60px;
  }
</style>

## Summary of gem5 CPU Models

![width:1150px padding-top:500px](04-cores-imgs/Summary-of-gem5-models-2.png)

---

## Outline

- **CPU models in gem5​**
  - AtomicSimpleCPU, TimingSimpleCPU, O3CPU, MinorCPU, KvmCPU​

- Using the CPU models​
  - Set-up a simple system with two cache sizes and three CPU models​

- Look at the gem5 generated statistics​
  - To understand differences among CPU models

---

<style scoped>
  div.line{
    display: flex;
    padding: 250px 50px 0;
    font-weight: normal;
  }
  span {
    flex: 5;
    text-align: center;
    line-height: 75px;

  }
  span.left {
    font-size: 5rem;
    font-weight: bold;
    background-size: 1000px 1000px;
    background: linear-gradient(to right,rgb(67,124,205), rgb(69,214,202));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  span.right {
    font-size: 1.9rem;
  }
  span.center {
    flex: 0.25;

  }
  div.bar {
    display: inline-block;
    width: 0px;
    border: 1px solid black;
    height: 100px;
    margin-top: -15px;
  }
</style>

<div class="line"><span class="left">SimpleCPU</span>

<span class="center">

<div class="bar"></div></span>
<span class="right">Functional, In-Order CPU Models</span></div>

---

<!--> Make this a class? <-->
<!-- <style scoped>
  h3{
    /* font-size: 1.8rem; */
  }
  h2{
    margin-bottom: 60px;
  } -->

</style>

## SimpleCPU

### **Atomic**

Seq. of nested calls
Use: Warming up, FF
<!-- </br> -->

### **Functional**

Backdoor access to mem.
(loading binaries)
No effect on coherency states
<!-- </br> -->

### **Timing**

Split transactions
Models queuing delay and
resource contention

![bg auto width:1250px Diagram to show different CPU Model Timings](04-cores-imgs/Simple-CPU.png)

---

<!-- <style scoped>
  h3{
    font-size: 1.8rem;
    margin-bottom: 0px;
    line-height: 0px;
  }
  h2{
    margin-bottom: 60px;
  } -->

## Other Simple CPUS


### AtomicSimpleCPU

- Uses **_Atomic_** memory accesses
  - No resource contentions or queuing delay
  - Mostly used for fast-forwarding and warming of caches

</br>

### TimingSimpleCPU

- Uses **_Timing_** memory accesses
  - Execute non-memory operations in one cycle
  - Models the timing of memory accesses in detail

---

## O3CPU (Out of Order CPU Model)

- **_Timing_** memory accesses _execute-in-execute_ semantics
- Time buffers between stages

---

## O3CPU Model Parameters (very configurable)

<!-- Update file location -->
src/cpu/o3/BaseO3CPU.py

---

## O3CPU Model Parameters (very configurable)

<!-- Update file location -->
src/cpu/o3/BaseO3CPU.py

---

## MinorCPU

![bg auto width:700px Diagram to show different CPU Models](04-cores-imgs/Minor-CPU.png)

<!-- 'https://nitish2112.github.io/post/gem5-minor-cpu/' Add "footer: " within the comment to make it appear on the slide-->

---

## KvmCPU

- KVM – Kernel-based virtual machine

- Used for native execution on x86 and ARM host platforms

- Guest and the host need to have the same ISA

- Very useful for functional tests and fast-forwarding

---


<style scoped>
  h3{
    font-size: 1.8rem;
    margin-bottom: 0;
    line-height: 0;
  }
  h2{
    margin-bottom: 0;
  }
</style>

## Summary of gem5 CPU Models

</br>

### **BaseKvmCPU**

- Very fast
- No timing
- No caches, BP
</br>

### **BaseSimpleCPU**

- Fast
- Some timing
- Caches, limited BP
</br>

### **DerivO3CPU and MinorCPU**

- Slow
- Timing
- Caches, BP

<!-- ![bg width:1200px Diagram to show different CPU Models](04-cores-imgs/Summary-of-gem5-models-bg-2.png) --> -->

![bg width:1200px Diagram to show different CPU Models](04-cores-imgs/Summary-of-gem5-models-bg-2.png)


---
<style scoped>
  h2{
    margin-bottom: -40px;
  }
</style>
## Interaction of CPU model with other parts of gem5

![bg auto width:1050px Diagram to show CPU Model Interactions](04-cores-imgs/CPU-interaction-model.png)


---

## Outline

- CPU models in gem5​
  - AtomicSimpleCPU, TimingSimpleCPU, O3CPU, MinorCPU, KvmCPU​

- **Using the CPU models​**
  - Set-up a simple system with two cache sizes and three CPU models​

- Look at the gem5 generated statistics​
  - To understand differences among CPU models

---

<style scoped>
  div.line{
    padding-top: 250px;
    font-size: 4rem;
    text-align: center;
    font-weight: bold;
    line-height: 75px;
    background: linear-gradient(to right,rgb(67,124,205), rgb(69,214,202));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
</style>

<div class="line">Let's use these CPU Models!</div>

---

## Material to use

gem5-bootcamp-env/materials/using-gem5/05-cpu-models/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu-models.py
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IntMM/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;finished-material/

---
