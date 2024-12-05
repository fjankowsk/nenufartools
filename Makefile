BLK         =   black
MAKE        =   make
PIP         =   pip3

BASEDIR     =   $(CURDIR)
SRCDIR      =   ${BASEDIR}/nftools

help:
	@echo 'Makefile for nftools'
	@echo 'Usage:'
	@echo 'make black           reformat the code using black code formatter'
	@echo 'make clean           remove temporary files'
	@echo 'make install         install the package locally'
	@echo 'make uninstall       uninstall the package'

black:
	${BLK} *.py */*.py */*/*.py

clean:
	rm -f ${SRCDIR}/*.pyc
	rm -f ${SRCDIR}/apps/*.pyc
	rm -rf ${SRCDIR}/__pycache__
	rm -rf ${SRCDIR}/apps/__pycache__
	rm -rf ${BASEDIR}/build
	rm -rf ${BASEDIR}/dist
	rm -rf ${BASEDIR}/nftools.egg-info
	rm -rf ${BASEDIR}/tests/__pycache__

install:
	${MAKE} clean
	${MAKE} uninstall
	${PIP} install .
	${MAKE} clean

uninstall:
	${PIP} uninstall --yes nftools

.PHONY: help black clean install uninstall