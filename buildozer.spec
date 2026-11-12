[app]

title = Lex Streamer App
package.name = lexstreamer
package.domain = org.lex
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
version = 0.1
requirements = python3==3.10.12,kivy,openssl,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_root = 1
bin_dir = ./bin
