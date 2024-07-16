# Ruby/SLICC assignment

Reference: [Excerpt: A Primer on Memory Consistency and Cache Coherence](https://www.gem5.org/_pages/static/external/Sorin_et-al_Excerpt_8.2.pdf).
Full reference: [A Primer on Memory Consistency and Cache Coherence](https://link.springer.com/book/10.1007/978-3-031-01764-3)

## Tasks

0. Copy the template

```sh
mkdir gem5/src/bootcamp
cp -r materials/developing-gem5-models/09-ruby/MyMSI* materials/developing-gem5-models/09-ruby/SConscript gem5/src/bootcamp
```

1. Together we will fill in the msg

- Add the different coherence request types: `GetS`, `GetM`, `PutS`, `PutM`
- Add the different response types: `Data`, `InvAck`

**Note:** Try to build to see what errors look like.

2. Together we will complete the message buffers in the directory controller.

```
    // Forwarding requests from the directory *to* the caches.
    MessageBuffer *forwardToCache, network="To", virtual_network="1",
          vnet_type="forward";
    // Response from the directory *to* the cache.
    MessageBuffer *responseToCache, network="To", virtual_network="2",
          vnet_type="response";

    // Requests *from* the cache to the directory
    MessageBuffer *requestFromCache, network="From", virtual_network="0",
          vnet_type="request";

    // Responses *from* the cache to the directory
    MessageBuffer *responseFromCache, network="From", virtual_network="2",
          vnet_type="response";
```

3. Fill out the `.slicc` file.

```text
protocol "MyMSI";
include "RubySlicc_interfaces.slicc";
include "MyMSI-msg.sm";
include "MyMSI-cache.sm";
include "MyMSI-dir.sm";
```

4. Compile

```sh
scons -j17 build/X86/gem5.opt PROTOCOL=MyMSI
```

5. Modify the runscript: Change `if buildEnv['PROTOCOL'] != 'MSI':` to `if buildEnv['PROTOCOL'] != 'MyMSI':` in `configs/learning_gem5/part3/msi_caches.py` line 48.

6. Run a parallel test

```sh
build/X86/gem5.opt configs/learning_gem5/part3/simple_ruby.py
```

Result is a failure!

```termout
build/X86/mem/ruby/protocol/L1Cache_Transitions.cc:266: panic: Invalid transition
system.caches.controllers0 time: 73 addr: 0x9100 event: DataDirNoAcks state: IS_D
```

8. Run with protocol trace

```sh
build/X86/gem5.opt --debug-flags=ProtocolTrace configs/learning_gem5/part3/simple_ruby.py
```

9. Start fixing the errors and fill in the `// Fill this in`

- Missing IS_D transition in cache
  - write the data to the cache
  - deallocate the TBE
  - mark that this is an "external load hit"
  - pop the response queue
- Fill in the "write data to cache" action
  - Get the data out of the message (how to get the message?)
  - set the cache entry's data (how? where does `cache_entry` come from?)
  - Make sure to have `assert(is_valid(cache_entry))`
- Why assert failure?
  - Fill in `allocateCacheBlock`!
  - Make sure to call `set_cache_entry`. Asserting there is an entry available and that `cache_entry` is invalid is helpful.
- Possible deadlock... hmm... This happens if *nothing* happens in the caches for a long time.
  - What was the last thing that happened before the deadlock? Let's check what was *supposed* to happen
  - Fill that in!
- Fix the next error (what to do on a store??)
  - Allocate a block, allocate a TBE, send a message, pop the queue
  - Also make sure that all actions that you need
  - When sending, you need to construct a new message. See `RequestMsg` in `MyMSI-msg.sm`
- Next error: What to do when there is sharing??
  - get data from memory (yes, this is an unoptimized protocol..)
  - remove the *requestor* from the sharers (just in case)
  - send an invalidate to all other sharers
  - set the owner
  - and pop the queue

**At some point it might be taking while to get to new errors, so...**

10. Run the ruby random tester. This is a special "cpu" which exercises coherence corner cases.

- Modify the `test_caches.py` the same way as `msi_caches.py`

```sh
build/X86/gem5.opt configs/learning_gem5/part3/ruby_test.py
```

Notice you may want to change `checks_to_complete` and `num_cpus` in `test_caches.py`.
You may also want to reduce the memory latency.

- Wow! now it should be way faster to see the error!
- Now, you need to handle this in the cache!
  - If you get an invalidate...
  - Send an ack, let the CPU know that this line was invalidated, deallocate the block, pop the queue
- So, now, hmm, it looks like it works??? But here's still one more `// Fill this in`
  - Some transitions are very rare
  - Try varying the parameters of the tester (without `ProtocolTrace`!) to find a combination which triggers an error (100000 checks, 8 CPUs, 50ns memory...)
- Now, you can fix the error!

11. Re-run the simple pthread test and lets look at some stats!

- How many forwarded messages did the L1 caches receive?
- How many times times did a cache have to upgrade from S -> M?
- What was the average miss latency for the L1?
- What was the average miss latency *when another cache had the data*?
