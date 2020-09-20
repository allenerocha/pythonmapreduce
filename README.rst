pythonmapreduce
###############

.. image:: https://img.shields.io/travis/allenerocha/pythonmapreduce
    :alt: Travis (.org)
    :target: https://travis-ci.org/allenerocha/pythonmapreduce
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style: black
    :target: https://github.com/psf/black
.. image:: https://codecov.io/gh/allenerocha/pythonmapreduce/branch/master/graph/badge.svg
    :alt: Codecov
    :target: https://codecov.io/gh/allenerocha/pythonmapreduce
.. image:: https://img.shields.io/badge/license-AGPLv3-green
     :alt: License:AGPLv3
    :target: https://www.gnu.org/licenses/agpl-3.0.en.html

Python implementation of the MapReduce concept using books sourced from https://www.gutenberg.org/

Features
========
This application currently does:

* Read input files or directories.
* Parse the given file(s).
* Filtering out all multiple spaces.
* Removal of all punctuation.
* A statistical analysis of the average characters and words per line.
* A statistical analysis of the median characters and words per line.
* Scatter plot generation of the statistical analyses.


Sample outputs:
===============
Using the data sets in the ./data/ directory, a static analysis is done to calculate the average and median character counts per line (c/l) and the average and median word counts per line (w/l).

.. image:: https://raw.githubusercontent.com/allenerocha/pythonmapreduce/master/sampleoutputs/average-chars.svg
    :alt: Average c/l
    :target: https://github.com/allenerocha/pythonmapreduce/blob/master/sampleoutputs/average-chars.svg
    :width: 100%
    :align: center

.. image:: https://raw.githubusercontent.com/allenerocha/pythonmapreduce/master/sampleoutputs/median-chars.svg
    :alt: Median c/l
    :target: https://github.com/allenerocha/pythonmapreduce/blob/master/sampleoutputs/median-chars.svg
    :width: 100%
    :align: center

.. image:: https://raw.githubusercontent.com/allenerocha/pythonmapreduce/master/sampleoutputs/average-words.svg
    :alt: Average w/l
    :target: https://github.com/allenerocha/pythonmapreduce/blob/master/sampleoutputs/average-words.svg
    :width: 100%
    :align: center

.. image:: https://raw.githubusercontent.com/allenerocha/pythonmapreduce/master/sampleoutputs/median-words.svg
    :alt: Average w/l
    :target: https://github.com/allenerocha/pythonmapreduce/blob/master/sampleoutputs/median-words.svg
    :width: 100%
    :align: center

TODO
====
Features to be implemented:

* Mapping standard input.
* Filtering standard input.
* Reducing the data.
