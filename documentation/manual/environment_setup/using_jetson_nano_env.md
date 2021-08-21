# Using the Jetson Nano Environment

## Linux Details

|||
|--|--|
|**Username** | ``cs31`` |
|**Password**  | ``cs31teamproject`` |
|**Set-up virtual environment**|``nano-env``|
|**Directory with repository**|``/home/cs31``|

## Getting started guide

The Jetson Nano environment has been set-up for the repository and is ready with very little extra configuration.

#### Changing Password

To change the password on a UNIX system you can either go into the settings menu or use the command prompt.

To use the command prompt, open the command prompt with the command `Ctrl + Alt + T`. Type the command below.

```
passwd
```

You will then be able to follow the on-screen prompts. Here is a sample output.
```
Changing password for cs31
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```
#### Changing username

To change the username on a UNIX system, follow this guide [here](https://www.linuxuprising.com/2019/04/how-to-change-username-on-ubuntu-debian.html).

#### Display Manager

Currently, the Jetson Nano is running LXDE display manager to improve performance and use less RAM. This can be changed back to GNOME display manager by running the command below.

```
 $ sudo dpkg-reconfigure lightdm
```
This will bring up a menu where you can select gdm3 as the display manager.

#### Using virtual environment

The Jetson Nano uses the Virtual Environment tool `virtualenv` and `virtualenvwrapper`. 

To use the pre-set-up virtual environment, run the command below:

```
$ workon nano-env
```

This will change your Python environment to the virtual environment `nano-env`.

#### Max performance

To get the best performance out of the Jetson Nano while running the scripts, run the commands below:

```
$ sudo nvpmodel -m 0
$ sudo jetson_clocks
```

These commands will have to be run every time you turn on the Jetson Nano again to get the maximum performance from the Jetson Nano.

While running the code you may find it useful to monitor memory, GPU or CPU performance. You can use the `jtop` to view this information. To use `jtop`, run the command below.

```
$ jtop
```

A swap file has been set-up to reduce the chance the system will run out of memory.

#### Running the code

The repository is already downloaded onto the Jetson Nano. To access the project's repository on the Jetson Nano, navigate to the home directory. This can be done with the following command.

```
$ cd ~
```

This should take you to `/home/cs31`. You can now navigate to the repository named `cs31-main`. This can be done with the command below:

```
$ cd cs31-main
```  

The Jetson Nano is an inference device, we recommended that the Jetson Nano is not used for training for this reason.

Details on how to run the mask detector can be found [here](documentation/manual/running_software_andtraining_model/running_facemask_detector.md).
Make sure that the camera has been plugged into the Jetson Nano before running the code and you are working on the `nano-env` virtual environment.

---
If you are having issues with using your camera, follow our troubleshooting guide [here](documentation/troubleshooting/errors_with_camera_config.md).

If you are having issues with using the pre-set-up Python environment, follow our troubleshooting guide [here](documentation/troubleshooting/errors_using_python_env.md).