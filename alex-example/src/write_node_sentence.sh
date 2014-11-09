#!/bin/bash

out_dir="$1"
sequence_id="$2"

node_list_file="${out_dir}/../list_node_ids/node_ids.txt"

while read node_id; do
  node_results="${out_dir}/../../../by_node/${node_id}/echo_node_id/node_id.txt"
  head -n1 "$node_results" >> "${out_dir}/node_sentence.txt"
  printf " " >> "${out_dir}/node_sentence.txt"
done < "${node_list_file}"
