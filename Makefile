all:
	cheetah compile --nobackup -R --idir templates/ --odir src/doxygen2gwiki/templates

test: direxamples
	mkdir -p wiki
	./doxygen2gwiki -d examples/doxygen/doc/xml -l Examples -l DoxygenManual -p Doxygen -j doxygen2gwiki -i examples/doxygen/code/ -o wiki
	./doxygen2gwiki -d examples/example1/doc/xml -l Examples -l Example1 -p Example1 -o wiki

direxamples:
	cd examples && make
