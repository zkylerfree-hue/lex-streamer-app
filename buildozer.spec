[app]

# (str) Title of your application
title = Lex Streamer App

# (str) Package name
package.name = lexstreamer

# (str) Package domain (needed for android packaging)
package.domain = org.lex

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = tests, bin, venv

# (list) Application requirements
# تم تحديد إصدار بايثون مستقر لتفادي مشاكل البناء مع النسخ التجريبية
requirements = python3==3.10.12,kivy,openssl,requests

# (str) Supported orientations
orientation = portrait

# (list) The orientation for the app
# orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Supported orientations (default to landscape for tablets and portrait for phones)
# supported_orientations = 1,2,3,4

# (list) List of extra java jar files to add
# android.add_jars = foo.jar,bar.jar

# (list) List of java files to add to the android project (can be .java or .dir)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aar =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (string) 
# android.ant_vars =

# (list) 
# android.setup_py_dirs =

# (str) 
# android.manifest.intent_filters =

# (str) 
# android.manifest.application_attributes =

# (str
