[app]
title = AB Scientific Calculator
package.name = abscientificcalc
package.domain = com.ab.scientific
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,sympy,numpy,scipy,Pillow,reportlab,requests,urllib3,charset-normalizer,idna,certifi

orientation = portrait
fullscreen = 0
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1