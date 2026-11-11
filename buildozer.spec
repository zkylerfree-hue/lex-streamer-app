[app]

# (str) Title of your application
title = LEX-Ω

# (str) Package name
package.name = lexomega

# (str) Package domain (needed for android packaging)
package.domain = org.lex

# (str) Version of the application
version = 0.1

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) The list of source directories to include
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Use the AndroidX support library
android.androidx = True

# (bool) Automatic acceptance of SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
