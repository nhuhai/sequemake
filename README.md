# SequeMake

The `hai-example/` directory contains a "Hello world" workflow.  That workflow takes a sequence with nodes "Hello", "comma", "world", and "bang" and does a few simple concatenations.  A similar sequence "Goodbye", "world", "dot" would re-use some of the Hello results in its own running.
 
The`sequemake.py` script, translates salutations_world.sequemk and hello_world.sequence into hello_world.mk.  When `sequemake.py` is written, running `make` in the `hai-example/` directory will create a file, `all.done.log`.  The basic interface to `sequemake.py` should be:

* `$1` - A file specifying the SequeMake graph, usually with an extension `.sequemk`.
* `$2` - A file specifying the data lineage sequence.  A straightforward way of specifying the sequence is using the file name's as the sequence name, listing one node ID per line, and just leaving implicit that an edge joins each line in file order.
* `$3` - The results root directory.  The standalone Makefile that SequeMake generates will create an entire results hierarchy, so for now it seems best to specify this results hierarchy at Makefile-generation time.

example: python salutations_world.sequemk hello_world.sequence results

## API notes

Note that the argument API that should be maintained for the workflow shell scripts is as follows (see example scripts in `example/src/*.sh`):

* `$1` - Output directory.
* `$2` - Major identifier - `node_id` for a node script, `sequence_id` for a sequence script, and initial node `node_id0` for an edge script.
* `$3` - Minor identifier - the edge-terminal `node_id1` for an edge script.  Unused in node and sequence scripts.

It is to be decided whether `list_node_ids.sh` should be a global requirement for any sequemake script.  Listing node identifiers in a file has turned out to be a simple way of consistently accessing the sequence order when needed.