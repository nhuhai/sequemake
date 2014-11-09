from sys import argv

root = "$(RESULTS_ROOT)"

echo_node_id_script        = "src/echo_node_id.sh"
cat_node_ids_script        = "src/cat_node_ids.sh"
list_node_ids_script       = "src/list_node_ids.sh"
write_edges_script         = "src/write_edges.sh"
write_node_sentence_script = "src/write_node_sentence.sh"

node_targets = []
edge_targets = []

# get string for the "all" target
def get_all(sequence):
    write_node_sentence_done_log = root + "/by_sequence/" + sequence + "/write_node_sentence.done.log"
    write_edges_done_log         = root + "/by_sequence/" + sequence + "/write_edges.done.log"

    all_str = "all:" + " \\\n" + \
              "  " + write_node_sentence_done_log + " \\\n" + \
              "  " + write_edges_done_log + "\n\n"
    return all_str

# takes in a node name and returns a string for that by_node target
def get_node(node):
    this_path   = root + "/by_node/" + node + "/echo_node_id"
    
    out_log     = this_path + ".out.log"
    err_log     = this_path + ".err.log"
    status_log  = this_path + ".status.log"
    done_log    = this_path + ".done.log"
    
    node_targets.append(done_log)
    
    node_str = done_log + ":" + " \\\n" + \
               "  " + echo_node_id_script + "\n" + \
               "\t" + "rm -rf " + this_path + "*" + "\n" + \
               "\t" + "mkdir -p " + this_path + "\n" + \
               "\t" + echo_node_id_script + " " + this_path + " " + node + " \\\n" + \
               "\t  " + ">" + out_log + " \\\n" + \
               "\t  " + "2>" + err_log + " ;" + " \\\n" + \
               "\t  " + "rc=$$? ;" + " \\\n" + \
               "\t  " + "echo $$rc > " + status_log + " ;" + " \\\n" + \
               "\t  " + "exit $$rc" + "\n" + \
               "\t" + "touch " + done_log + "\n"

    return node_str

# takes in a list of nodes and returns a string for all by_node targets
def get_all_nodes(nodes):
    all_by_node_str =  ""
    for node in nodes:
        all_by_node_str += get_node(node) + "\n"
    return all_by_node_str

# takes in a pair of nodes and return a string by_edge for that pair of nodes
def get_edge(node0, node1):
    this_path = root + "/by_edge/" + node0 + "/" + node1 + "/cat_node_ids"
    path_to_node0 = root + "/by_node/" + node0 + "/echo_node_id.done.log"
    path_to_node1 = root + "/by_node/" + node1 + "/echo_node_id.done.log"

    out_log     = this_path + ".out.log"
    err_log     = this_path + ".err.log"
    status_log  = this_path + ".status.log"
    done_log    = this_path + ".done.log"

    edge_targets.append(done_log)

    edge_str = done_log + ":" + " \\\n" + \
               "  " + cat_node_ids_script + " \\\n" + \
               "  " + path_to_node0 + " \\\n" + \
               "  " + path_to_node1 + "\n" + \
               "\t" + "rm -rf " + this_path + "*" + "\n" + \
               "\t" + "mkdir -p " + this_path + "\n" + \
               "\t" + cat_node_ids_script + " " + this_path + " " + node0 + " " + node1 + " \\\n" + \
               "\t  " + ">" + out_log + " \\\n" + \
               "\t  " + "2>" + err_log + " ;" + " \\\n" + \
               "\t  " + "rc=$$? ;" + " \\\n" + \
               "\t  " + "echo $$rc > " + status_log + " ;" + " \\\n" + \
               "\t  " + "exit $$rc" + "\n" + \
               "\t" + "touch " + done_log  + "\n"
               
    return edge_str

# takes in a list of nodes and returns a string for alla
def get_all_edges(nodes):
    all_edges_str = ""
    if len(nodes) >= 2:
        for i in range(0, len(nodes) - 1):
            all_edges_str += get_edge(nodes[i], nodes[i+1]) + "\n"
    return all_edges_str

# get string for the "write_node_sentence.done.log" target
def write_node_sentence(sequence):
    this_path              = root + "/by_sequence/" + sequence + "/write_node_sentence"
    list_node_ids_done_log = root + "/by_sequence/" + sequence + "/list_node_ids.done.log"

    out_log     = this_path + ".out.log"
    err_log     = this_path + ".err.log"
    status_log  = this_path + ".status.log"
    done_log    = this_path + ".done.log"

    sequence_str = done_log + ":" + " \\\n" + \
                   "  " + write_node_sentence_script + " \\\n" + \
                   "  " + list_node_ids_done_log 

    for node_done in node_targets:
        sequence_str += " \\\n" + "  " + node_done

    sequence_str += "\n\t" + "rm -rf " + this_path + "*" + "\n" + \
                    "\t" + "mkdir -p " + this_path + "\n" + \
                    "\t" + write_node_sentence_script + " " + this_path + " " + sequence + " \\\n" + \
                    "\t  " + ">" + out_log + " \\\n" + \
                    "\t  " + "2>" + err_log + " ;" + " \\\n" + \
                    "\t  " + "rc=$$? ;" + " \\\n" + \
                    "\t  " + "echo $$rc > " + status_log + " ;" + " \\\n" + \
                    "\t  " + "exit $$rc" + "\n" + \
                    "\t" + "touch " + done_log + "\n\n"
                   
    return sequence_str

# get string for the "list_node_ids.done.log" target
def list_node_ids(sequence):
    this_path   = root + "/by_sequence/" + sequence + "/list_node_ids"
    
    out_log     = this_path + ".out.log"
    err_log     = this_path + ".err.log"
    status_log  = this_path + ".status.log"
    done_log    = this_path + ".done.log"

    sequence_str = done_log + ":" + " \\\n" + \
                   "  " + list_node_ids_script + "\n" + \
                   "\t" + "rm -rf " + this_path + "*" + "\n" + \
                   "\t" + "mkdir -p " + this_path + "\n" + \
                   "\t" + list_node_ids_script + " " + this_path + " " + sequence + " \\\n" + \
                   "\t  " + ">" + out_log + " \\\n" + \
                   "\t  " + "2>" + err_log + " ;" + " \\\n" + \
                   "\t  " + "rc=$$? ;" + " \\\n" + \
                   "\t  " + "echo $$rc > " + status_log + " ;" + " \\\n" + \
                   "\t  " + "exit $$rc" + "\n" + \
                   "\t" + "touch " + done_log + "\n\n"
    return sequence_str

# get string for the "write_edge.done.log" target
def write_edges(sequence):
    this_path   = root + "/by_sequence/" + sequence + "/write_edges"

    out_log     = this_path + ".out.log"
    err_log     = this_path + ".err.log"
    status_log  = this_path + ".status.log"
    done_log    = this_path + ".done.log"

    sequence_str = done_log + ":" + " \\\n" + \
                   "  " + write_edges_script

    for edge_done in edge_targets:
        sequence_str += " \\\n" + "  " + edge_done

    sequence_str += "\n\t" + "rm -rf " + this_path + "*" + "\n" + \
                    "\t" + "mkdir -p " + this_path + "\n" + \
                    "\t" + write_edges_script + " " + this_path + " " + sequence + " \\\n" + \
                    "\t  " + ">" + out_log + " \\\n" + \
                    "\t  " + "2>" + err_log + " ;" + " \\\n" + \
                    "\t  " + "rc=$$? ;" + " \\\n" + \
                    "\t  " + "echo $$rc > " + status_log + " ;" + " \\\n" + \
                    "\t  " + "exit $$rc" + "\n" + \
                    "\t" + "touch " + done_log + "\n"
                   
    return sequence_str
    
# execution starts here
if len(argv) == 4:
    script, GRAPH, SEQUENCE, RESULTS = argv

    with open(SEQUENCE) as f:
        nodes = [line.strip() for line in f]

    out_str = "# Rendered from " + GRAPH + " operating on " + SEQUENCE + "\n\n"
    out_str += "RESULTS_ROOT=" + RESULTS + "\n\n"
    out_str += get_all(SEQUENCE)                  # all target
    out_str += get_all_nodes(nodes)               # by_node targets
    out_str += get_all_edges(nodes)               # by_edge targets
    out_str += write_node_sentence(SEQUENCE)      # write_node_sentence.done.log target
    out_str += list_node_ids(SEQUENCE)            # list_node_ids.done.log target
    out_str += write_edges(SEQUENCE)              # write_edges.done.log target

    out_file_name = SEQUENCE.split('.')[0]
    out_file = open(out_file_name + ".mk", "w")
    out_file.write(out_str)
    out_file.close()
else:
    print "Usage: python sequemake.py [sequemake graph] [lineage sequence] [results]"


