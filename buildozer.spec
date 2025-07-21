[app]

# (str) Title of your application
title = PlanetFit

# (str) Package name
package.name = planetfit

# (str) Package domain (must be unique)
package.domain = org.planetfit

# (str) Source code where your main.py is located
source.dir = .

# (str) The main .py file to use as the main entry point
source.main = main.py

# (str) Version of your application
version = 1.0

# (int) Version code (used in Android)
version.code = 1

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE

# (list) Application requirements (Python modules)
requirements = python3,kivy

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (bool) Indicate if the app should be fullscreen or not
fullscreen = 1

# (str) Entry point for the app (if it's not main.py)
# entrypoint = main.py

# (bool) Hide the statusbar
android.hide_statusbar = 1

# (bool) Copy .apk to current directory after build
copy_to_current = 1

# (bool) Include source code in apk (for debugging)
# android.include_source = false

# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Theme (black, light, etc.)
# android.theme = @android:style/Theme.NoTitleBar

# (str) Android entry point, default is ok
# android.entrypoint = org.kivy.android.PythonActivity

# (list) Custom java .jar dependencies
# android.add_jars = libs/*.jar

# (list) Android bootstrap (use 'sdl2' or 'webview')
android.bootstrap = sdl2

# (bool) Use --private data storage (deprecated)
# android.private_storage = false

# (bool) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK API to build with
android.api = 33

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK build tool version
android.build_tools = 34.0.0

# (str) Command to run after build (optional)
# postbuild_command = ...

# (bool) Enable AndroidX support
android.enable_androidx = 1

# (bool) Enable View Binding support
# android.enable_viewbinding = 0
