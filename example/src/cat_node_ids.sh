#!/bin/bash

out_dir="$1"
node_id0="$2"
node_id1="$3"

echo "${node_id0}" "${node_id1}" > "${out_dir}/node_ids.txt"
