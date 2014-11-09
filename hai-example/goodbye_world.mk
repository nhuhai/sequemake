# Rendered from salutations_world.sequemk operating on goodbye_world.sequence

RESULTS_ROOT=results

all: \
  $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.done.log \
  $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.done.log

$(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id Goodbye \
	  >$(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.done.log

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

$(RESULTS_ROOT)/by_node/dot/echo_node_id.done.log: \
  src/echo_node_id.sh
	rm -rf $(RESULTS_ROOT)/by_node/dot/echo_node_id*
	mkdir -p $(RESULTS_ROOT)/by_node/dot/echo_node_id
	src/echo_node_id.sh $(RESULTS_ROOT)/by_node/dot/echo_node_id dot \
	  >$(RESULTS_ROOT)/by_node/dot/echo_node_id.out.log \
	  2>$(RESULTS_ROOT)/by_node/dot/echo_node_id.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_node/dot/echo_node_id.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_node/dot/echo_node_id.done.log

$(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.done.log: \
  src/cat_node_ids.sh \
  $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids*
	mkdir -p $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids
	src/cat_node_ids.sh $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids Goodbye world \
	  >$(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.done.log

$(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.done.log: \
  src/cat_node_ids.sh \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/dot/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids*
	mkdir -p $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids
	src/cat_node_ids.sh $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids world dot \
	  >$(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.done.log

$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.done.log: \
  src/write_node_sentence.sh \
  $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.done.log \
  $(RESULTS_ROOT)/by_node/Goodbye/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/world/echo_node_id.done.log \
  $(RESULTS_ROOT)/by_node/dot/echo_node_id.done.log
	rm -rf $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence*
	mkdir -p $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence
	src/write_node_sentence.sh $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence goodbye_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_node_sentence.done.log

$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.done.log: \
  src/list_node_ids.sh
	rm -rf $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids*
	mkdir -p $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids
	src/list_node_ids.sh $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids goodbye_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/list_node_ids.done.log

$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.done.log: \
  src/write_edges.sh \
  $(RESULTS_ROOT)/by_edge/Goodbye/world/cat_node_ids.done.log \
  $(RESULTS_ROOT)/by_edge/world/dot/cat_node_ids.done.log
	rm -rf $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges*
	mkdir -p $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges
	src/write_edges.sh $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges goodbye_world.sequence \
	  >$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.out.log \
	  2>$(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.err.log ; \
	  rc=$$? ; \
	  echo $$rc > $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.status.log ; \
	  exit $$rc
	touch $(RESULTS_ROOT)/by_sequence/goodbye_world.sequence/write_edges.done.log
