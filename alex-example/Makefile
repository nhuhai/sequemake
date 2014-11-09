#!/usr/bin/make -f

#This Makefile runs the entire example program.
#It assumes the existence of a program that hasn't been written yet, sequemake.py.

PYTHON = python3

all: all.done.log

#The Hello World Makefile was hand-written, but could be generated with this commented-out rule.
#hello_world.mk: sequemake.py salutations_world.sequemk hello_world.sequence
#	$(PYTHON) sequemake.py salutations_world.sequemk hello_world.sequence results

#Goal: Generate the Goodbye World Makefile.  It should end up looking similar to hello_world.mk.
goodbye_world.mk: sequemake.py salutations_world.sequemk goodbye_world.sequence
	$(PYTHON) sequemake.py salutations_world.sequemk goodbye_world.sequence results

all.done.log: goodbye_world.mk hello_world.mk
	$(MAKE) -f hello_world.mk
	$(MAKE) -f goodbye_world.mk
	touch all.done.log
