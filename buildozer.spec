[app]

# (str) Title of your application
title = My Pygame App

# (str) Package name
package.name = mypygameapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) 
source.dir =. 

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# These requirements will be translated into permissions on Android
# and bundled data on iOS.
requirements = android,python3,pygame>=2.0.2.dev8,kivy

# (str) Presplash image to use for the application
presplash.filename = data/presplash.png

# (str) Icon file to use for the application
icon.filename = data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = landscape

# (list) List of service to declare
#services =

# (str) Primary service to run (can be none if single service app)
#service =

# (str) Log level (debug, info, warning, error, critical)
log.level = debug

#  Flags to keep p4a attributes to use in later processes
#  p4a.option_name=option_value

#  List of rules to enable or disable the use of specific p4a recipe:
#  python.host_pip_requirements = logs_rolling_file_handler

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is out of date
warn_on_root = 1

# (int) Number of processes to use for building
# Leave blank to auto-detect or set to a specific number:
# max_workers = 4

#    ---------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,**/__pycache__
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#**/__pycache__
#

#    -----------------------------
#    Profiles
#
#    You can extend section / keys with profiles
#    For example, you want to deploy a scanner exclusively for Android
#    and run the installer with different options for each platform.
#    The syntax for a profile is as follows:
#
#    [profile:unitTest]
#    source.include_patterns = **/*.py
#
#    [profile:android]
#    requirements.source.skip_upload = True
#    services = scanner:1,upload:0
#
#    Each profile is a section that can extend or override
#    the main section or sub sections values depending on the key used.

#    -----------------------------
#    Buildozer commands
#
#    To better understand buildozer files, please visit:
#    https://buildozer.readthedocs.org/en/latest/manual.html
#
#    To understand how a sample is built in buildozer, please visit:
#    https://buildozer.readthedocs.org/en/latest/backend.html#sample-build
#
#    -----------------------------
#    Getting packages
#
#    To fetch some python packages, dependencies or package recipes
#    you may read buildozer's readme to see the getting_package_recipe
#    setup example. Checkout https://buildozer.readthedocs.org/
#

# This is the buildozer.spec file. You can edit and adapt it to your needs
# assuming you have installed buildozer and the python-for-android requirements