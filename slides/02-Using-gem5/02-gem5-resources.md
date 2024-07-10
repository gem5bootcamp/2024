---
marp: true
paginate: true
theme: gem5
title: gem5 Resources
---

<!-- _class: title -->

## gem5 Resources

---

## What are resources? (Disks, kernels, binaries, etc.)

- gem5 resources are prebuilt artifacts that can be used to run gem5 simulations.

- gem5 resources are categorized by 13 different categories (binary, kernel, etc) and 6 different ISAs (ARM, x86, risc-v, etc).

- For more information about categories: [resources.gem5.org/category](https://resources.gem5.org/category)

- [gem5 resources website](https://resources.gem5.org) is an easy way to search for the resources you want to use.

---

## How are resources versioned

- Each unique resource is represented by its `id` and `resource_version`.

- When an existing resource is updated the `id` remains the same but the `resource_version` is updated.

- Each resource also has a field called `gem5_versions` which shows which releases of gem5 the resource is known to work on.

<div style="text-align: center; margin-top: 12px;">
  <img src="./02-gem5-resouces/resource_website_version.png" alt="Versions tab from resources website" style="width: 80%; height: 350px;">
</div>

---

## How to use resources in gem5 simulations

- To use the resources in gem5, we can use the `obtain_resource` function.
- Lets to an example to use the `x86-hello64-static` binary in an example.

---

## Workloads and suites

- Workload is a package of one or more resources that can have pre-defined parameters.
- Lets see the `x86-ubuntu-24.04-boot-with-systemd` workload, you can see the [raw](https://resources.gem5.org/resources/x86-ubuntu-24.04-boot-with-systemd/raw?database=gem5-resources&version=1.0.0) tab to see how the resource is made.
  - The `function` field has the name of the function that the workload calls.
  - The `resources` field contains the resources that the workload uses.
    - The key of the `resources` field like `kernel`, `disk_image`, etc are named the same as the parameter name in the `function` that the workload calls.
  - The `additional_params` fields contains values of non-resource parameters that we want the workload to have
    - `kernel_args` parameter we are using in the above workload.

- Suites are a collection of workloads, that can be run in parallel using multiprocessing (This will be shown later)

- Lets do an example that obtains a suite and then runs a workload from the suite.

---
## Local resources

- You can also use resources that you have created locally in gem5.
- You can create a local JSON file that you can use as a data source by setting the
  - GEM5_RESOURCE_JSON environment variable to point to the JSON, if you want to just use the resources in the JSON.
  - GEM5_RESOURCE_JSON_APPEND environment variable to point to the JSON, if you want to use local resources along with gem5 resources.
- For more details on how to use local resources, read [local resources documentation](https://www.gem5.org/documentation/gem5-stdlib/using-local-resources)

- Lets do an example that create a local binary and runs that binary on gem5.
