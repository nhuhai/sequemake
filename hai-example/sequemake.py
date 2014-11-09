from sys import argv

root = "$(RESULTS_ROOT)"

path_to_echo_node_script = "src/echo_node_id.sh"
path_to_cat_node_script = "src/cat_node_ids.sh"
path_to_list_node_script = "src/list_node_ids.sh"
path_to_write_edges_script = "src/write_edges.sh"
path_to_write_node_script = "src/write_node_sentence.sh"

path_to_write_node_sentence = ""
path_to_write_edges = ""

def get_all():
    all_str = "all:" + " \\\n" + \
              "  " + path_to_write_node_sentence + " \\\n" + \
              "  " + path_to_write_edges + "\n\n"
    return all_str

# takes in a node name and returns a string for that by_node target
def get_node(node):
    path_to_node = root + "/by_node/" + node + "/echo_node_id"
    
    node_str = path_to_node + ".done.log:" + " \\\n" + \
               "  " + path_to_echo_node_script + "\n" + \
               "\t" + "rm -rf " + path_to_node + "*" + "\n" + \
               "\t" + "mkdir -p " + path_to_node + "\n" + \
               "\t" + path_to_echo_node_script + " " + path_to_node + " " + node + " \\\n" + \
               "\t  " + ">" + path_to_node + ".out.log" + " \\\n" + \
               "\t  " + "2>" + path_to_node + ".err.log ;" + " \\\n" + \
               "\t  " + "rc=$$? ;" + " \\\n" + \
               "\t  " + "echo $$rc > " + path_to_node + ".status.log ;" + " \\\n" + \
               "\t  " + "exit $$rc" + "\n" + \
               "\t" + "touch " + path_to_node + ".done.log" + "\n"

    return node_str

# takes in a list of nodes and returns a string for all by_node targets
def get_all_nodes(nodes):
    all_by_node_str =  ""
    for node in nodes:
        all_by_node_str += get_node(node) + "\n"
    return all_by_node_str

# takes in a pair of nodes and return a string by_edge for that pair of nodes
def get_edge(node0, node1):
    path_to_edge = root + "/by_edge/" + node0 + "/" + node1 + "/cat_node_ids"
    path_to_node0 = root + "/by_node/" + node0 + "/echo_node_id.done.log"
    path_to_node1 = root + "/by_node/" + node1 + "/echo_node_id.done.log"

    edge_str = path_to_edge + ".done.log:" + " \\\n" + \
               "  " + path_to_cat_node_script + " \\\n" + \
               "  " + path_to_node0 + " \\\n" + \
               "  " + path_to_node1 + "\n" + \
               "\t" + "rm -rf " + path_to_edge + "*" + "\n" + \
               "\t" + "mkdir -p " + path_to_edge + "\n" + \
               "\t" + path_to_cat_node_script + " " + path_to_edge + " " + node0 + " " + node1 + " \\\n" + \
               "\t  " + ">" + path_to_edge + ".out.log" + " \\\n" + \
               "\t  " + "2>" + path_to_edge + ".err.log ;" + " \\\n" + \
               "\t  " + "rc=$$? ;" + " \\\n" + \
               "\t  " + "echo $$rc > " + path_to_edge + ".status.log ;" + " \\\n" + \
               "\t  " + "exit $$rc" + "\n" + \
               "\t" + "touch " + path_to_edge + ".done.log" + "\n"
               
    return edge_str

# takes in a list of nodes and returns a string for alla
def get_all_edges(nodes):
    all_edges_str = ""
    if len(nodes) >= 2:
        for i in range(0, len(nodes) - 1):
            all_edges_str += get_edge(nodes[i], nodes[i+1]) + "\n"
    return all_edges_str
    
# execution starts here
if len(argv) == 4:
    script, graph, sequence, results = argv

    path_to_write_node_sentence = root + "/by_sequence/" + sequence + "/write_node_sentence.done.log"
    path_to_write_edges = root + "/by_sequence/" + sequence + "/write_edges.done.log"

    with open(sequence) as f:
        nodes = [line.strip() for line in f]

    out_str = "# Rendered from " + graph + " operating on " + sequence + "\n\n"
    out_str += "RESULTS_ROOT=" + results + "\n\n"
    out_str += get_all()                      # get all target
    out_str += get_all_nodes(nodes)           # append by_node
    out_str += get_all_edges(nodes)          # append by_edge
    #out_str += get_all_by_sequence(nodes)    # append by_sequence

    out_file_name = sequence.split('.')[0]
    out_file = open(out_file_name + ".mk", "w")
    out_file.write(out_str)
    out_file.close()
else:
    print "Usage: python sequemake.py [sequemake graph] [lineage sequence] [results]"


