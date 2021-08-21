# Errors while using Pre-Setup Python Environment

## Overview

If you encounter errors when using the pre-setup Python environment, follow this troubleshooting guide for possible solutions.

## Possible Errors

#### **ModuleNotFoundError**

If you encounter an error similar to the one shown below, there is a good chance that the package has not been installed correctly:

```
$ ModuleNotFoundError: No module named 'your_module_name'
```

To fix this, you will normally be able to install the package through `pip`.  By following the instructions on installing the package from [PyPI · The Python Package Index](https://pypi.org/), you should be able to solve this issue.

For certain Python packages, you may require a specialised version for the Jetson Nano. This includes packages like NumPy and TensorFlow.  Follow the manual [Setting up a new Jetson Nano Environment](documentation/manual/environment_setup/jetson_nano_env_setup.md), to find out how to install these specific packages.

If you have multiple packages which are causing errors, you may find it easier to install the packages through the `jetson_requirements.txt` file.  In your virtual environment, run the command below:

```
$ pip install -r jetson_requirements.txt
```

This will install all the packages at the specific version specified in the file.  This method could cause errors with other packages that you have installed as they may be different versions so use this method at your own risk.

If previous methods to fix your issue do not work, setting up a new environment using the manual here [here](documentation/manual/environment_setup/jetson_nano_env_setup.md) can also help fix your issue.