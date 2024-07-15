---
marp: true
paginate: true
theme: gem5
title: "Modeling memory objects in gem5: Ports"
---

<!-- _class: title -->

## Modeling memory objects in gem5: Ports

---

- Idea of ports (request/response), packets, interface
- A simple memory object that forwards things
- Connecting ports and writing config files
- Adding stats to a SimObject

---

## InspectorGadget

```python
class InspectorGadget(ClockedObject)
    mem_side_port = ResponsePort()
    cpu_side_port = RequestPort()

    inspection_buffer_entries = Param.Int("Number of entries in the input buffer for inspection.")

    num_inspecting_units = Param.Int("Maximum number of inspections done in parallel.")

    start_per_cycle = Param.Int("Maximum number of inspections that can be started at the  same cycle.")

    inspection_latency = Param.Cycle("Number of  cycles to inspect one packet.")
    pipeline_inspection = Param.Bool("Whether the inspection units are pipelined or not.")
    critical_inspection_latency = Param.Cycle("The number of cycles between two inspections for the same inspection unit. This parameter is ignored if `pipeline_inspection` is set to `False`.")

    cxx_exports = [PyBindMethod("printInspectionBuffer")]
```
