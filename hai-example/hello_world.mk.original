#Rendered from hello_world.sequemk operating on hello_world.sequence

RESULTS_ROOT=results

all: \
  $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.done.log \
  $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.done.log

$(RESULTS_ROOT)/by_node/Hello/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/Hello/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/Hello/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/Hello/echo_node_id Hello \
	  >$(RESULTS_ROOT)/by_node/Hello/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/Hello/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/Hello/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/Hello/echo_node_id.done.log

$(RESULTS_ROOT)/by_node/comma/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/comma/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/comma/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/comma/echo_node_id comma \
	  >$(RESULTS_ROOT)/by_node/comma/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/comma/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/comma/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/comma/echo_node_id.done.log

$(RESULTS_ROOT)/by_node/world/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/world/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/world/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/world/echo_node_id world \
	  >$(RESULTS_ROOT)/by_node/world/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/world/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/world/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log

$(RESULTS_ROOT)/by_node/bang/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/bang/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/bang/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/bang/echo_node_id bang \
	  >$(RESULTS_ROOT)/by_node/bang/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/bang/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/bang/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/bang/echo_node_id.done.log

$(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.done.log: \
  src/cat_node_ids.sh \
  $(RESULTS_ROOT)/by_node/Hello/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/comma/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids
	mkdir -p $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids
	src/cat_node_ids.sh $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids Hello comma \
	  >$(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.done.log

$(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.done.log: \
  src/cat_node_ids.sh \
  $(RESULTS_ROOT)/by_node/comma/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids
	mkdir -p $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids
	src/cat_node_ids.sh $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids comma world \
	  >$(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.done.log

$(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.done.log: \
  src/cat_node_ids.sh \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/bang/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids
	mkdir -p $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids
	src/cat_node_ids.sh $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids world bang \
	  >$(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.done.log

$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.done.log: \
  src/write_node_sentence.sh \
  $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.done.log \
  $(RESULTS_ROOT)/by_node/Hello/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/comma/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/bang/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence*
	mkdir -p $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence
	src/write_node_sentence.sh $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence hello_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_node_sentence.done.log

$(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.done.log: \
  src/list_node_ids.sh
	rm -rf $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids*
	mkdir -p $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids
	src/list_node_ids.sh $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids hello_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/hello_world.sequence/list_node_ids.done.log

$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.done.log: \
  src/write_edges.sh \
  $(RESULTS_ROOT)/by_edge/Hello/comma/cat_node_ids.done.log \
  $(RESULTS_ROOT)/by_edge/comma/world/cat_node_ids.done.log \
  $(RESULTS_ROOT)/by_edge/world/bang/cat_node_ids.done.log
	rm -rf $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges*
	mkdir -p $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges
	src/write_edges.sh $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges hello_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/hello_world.sequence/write_edges.done.log
