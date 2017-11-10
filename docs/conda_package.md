Building conda packages with conda skeleton
========

* Build conda package
```
$ conda skeleton pypi pydaily
$ conda-build pydaily
$ conda install --use-local pydaily
$ anaconda upload pydaily.tar.bz2-path
```

* Converting the conda package to other systems
```
$ conda-convert pydaily.tar.bz2-path -p all
$ binstar upload linux-32/pydaily.tar.bz2
$ binstar upload linux-64/pydaily.tar.bz2
$ binstar upload win-32/pydaily.tar.bz2
$ binstar upload win-64/pydaily.tar.bz2
```
* Setting automatically upload a successful build to Anaconda.org
```
conda config --set anaconda_upload yes
'''

**References**
* [Building conda packages with conda skeleton](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html)
* [My Anaconda Landscape] (https://anaconda.org/pingjunchen/dashboard)
