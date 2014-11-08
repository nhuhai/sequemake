#!/bin/bash

# Normally, this script would connect to some data store to print out the node ids in their sequence order.  For this example, though, the sequence file is just concatenated.

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

out_dir="$1"
sequence_id="$2"

cat "${this_dir}/../${sequence_id}" > "${out_dir}/node_ids.txt"
