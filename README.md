# NenuFAR Tools #

A few simple Python tools for NenuFAR.

## Installation ##

`pip install git+https://github.com/fjankowsk/nenufartools.git@main`

Replace `pip` by `pip3` depending on your Python installation.

## Usage ##

```console
$ nftools-check-active-ms -h
usage: nftools-check-active-ms [-h] [-p] prefix

Check the mini-arrays active in a NenuFAR observations.

positional arguments:
  prefix        The prefix of the meta data files to process (e.g. 20241202_110000_20241202_130000_MULTIFREQUENCY).

optional arguments:
  -h, --help    show this help message and exit
  -p, --pulsar  Exclude the distant mini-arrays for pulsar observations, which use the core only. (default: False)
```
