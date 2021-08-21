# Errors During NumPy Installation

## Overview

If you encounter the error below, follow this troubleshooting guide to fix the issue.

## Potential Issues

```
ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly. 
```

We can install NumPy with superuser privileges.

```
$ sudo pip install numpy
```

You can then create a symbolic link from your system’s NumPy into your virtual environment site-packages. To be able to do that you would need the installation path of numpy, which can be found out by issuing a NumPy uninstall command, and then canceling it as follows:

```
$ sudo pip uninstall numpy
Uninstalling numpy-1.18.1:
  Would remove:
    /usr/bin/f2py
    /usr/local/bin/f2py
    /usr/local/bin/f2py3
    /usr/local/bin/f2py3.6
    /usr/local/lib/python3.6/dist-packages/numpy-1.18.1.dist-info/*
    /usr/local/lib/python3.6/dist-packages/numpy/*
Proceed (y/n)? n
```

Note that you should type **`n`** at the prompt as you do not want to proceed with the removal of NumPy.  Then, note down the installation path (`/usr/local/lib/python3.6/dist-packages/numpy/*`), and execute the following commands (replacing the paths as needed):

```
# Change virtual environment name as needed
# In this case our virtual environment is called nano-env
$ cd ~/.virtualenvs/nano-env/lib/python3.6/site-packages/
$ ln -s ~/usr/local/lib/python3.6/dist-packages/numpy numpy
$ cd ~
```

At this point, NumPy is sym-linked into your virtual environment.