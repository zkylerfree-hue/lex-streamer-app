[app]

title = LEX-Ω
package.name = lexomega
package.domain = org.lex
version = 0.1
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.androidx = True
android.accept_sdk_license = True
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
