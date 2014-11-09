from sys import argv

if len(argv) == 4:
    script, graph, sequence, results = argv
    root = "$(RESULTS_ROOT)"

    with open(sequence) as f:
        nodes = f.readlines()

    outStr = ""
    outStr += "# Rendered from " + graph + " operating on " + sequence + "\n\n"
    outStr += "RESULTS_ROOT=" + results + "\n\n"
    outStr += "all: "
    outStr += root + "/by_sequence/" + sequence + "/write_node_sequence_done.log " + \
              root + "/by_sequence/" + sequence + "/write_edges.done.log"

    outFile = open("out.mk", "w")
    outFile.write(outStr)
    outFile.close()
else:
    print "Usage: python sequemake.py [sequemake graph] [lineage sequence] [results]"


