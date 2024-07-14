#!/usr/bin/env bash

# The following will run 4 gem5 processes in parallel.
# To stop each process overwriting the output of the other, we have each
# output to a unique directory.
#
# **Flag notes**:
#
# `-r`: Redirects the stdout to a file in the outdput directory.
# `-e`: Redirects the stderr to a file in the output directory.
# `-d`: Specifies the output directory.
#
# Usage
# =====
# ./run-experiment.sh
#

gem5 -re -d experiment_1 experiment.py "8kB" "8kB" && \
gem5 -re -d experiment_2 experiment.py "16kB" "8kB" && \
gem5 -re -d experiment_3 experiment.py "8kB" "16kB" && \
gem5 -re -d experiment_4 experiment.py "16kB" "16kB"
