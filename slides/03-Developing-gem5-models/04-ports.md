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

    inspection_buffer_entries = Param.Int(...)

    num_inspecting_units = Param.Int(...)

    inspection_starts_per_cycle = Param.Int(...)

    inspection_total_latency = Param.Cycle(...)
    pipeline_inspection = Param.Bool(...)
    inspection_frontend_latency = Param.Cycle(...)

    cxx_exports = [PyBindMethod("printInspectionBuffer")]
```
