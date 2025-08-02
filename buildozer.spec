[app]
title = Isaan Language Learning
package.name = isanlanguage
package.domain = org.isanlanguage
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0
requirements = python3,kivy==2.1.0,pyjnius==1.4.2,cython==0.29.36
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app@android]
android.accept_sdk_license = True
android.arch = arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.build_tools_version = 31.0.0
android.ndk_api = 21
