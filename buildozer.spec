[app]

# (str) Title of your application
title = Lex Streamer App

# (str) Package name
package.name = lexstreamer

# (str) Package domain (needed for android packaging)
package.domain = org.lex

# (str) Source directory where your app lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = tests, bin, venv

# (str) Application versioning (version numbering)
version = 0.1

# (list) Application requirements
# تم تحديد إصدار بايثون ومكتبة أوبن إس إس إل لضمان الاستقرار وعدم التعليق
requirements = python3==3.10.12,kivy,openssl,requests

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Target API version for your application
android.api = 33

# (str) Minimum API version
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android archs to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin
