#!/bin/bash

out_dir="$1"
sequence_id="$2"

node_list_file="${out_dir}/../list_node_ids/node_ids.txt"

prior_node_id=
while read node_id; do
  if [ ! -z "$prior_node_id" ]; then
    edge_results="${out_dir}/../../by_edge/${prior_node_id}/${node_id}/cat_node_ids/node_ids.txt"
    cat "$edge_results" >> "${out_dir}/ordered_edges"
  fi
  prior_node_id=node_id
done < "${node_list_file}"

