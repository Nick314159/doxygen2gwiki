all: direxamples
	cheetah compile --nobackup -R --idir templates/ --odir src/doxygen2gwiki/templates

direxamples:
	cd examples && make
