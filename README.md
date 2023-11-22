# Linux window management tool

Sets windows parameters based on the provided config.

### Requirements

- python
- wmctrl

### Config

```
[google chrome]             // window name, will be searched for in the `wmctrl -l` output
x = 1920                    // X position
y = 420                     // Y position
w = 1920                    // width
h = 1036                    // height
maximize = True             // if True, maximizes the window in a set position
ignoremaximizeoff = False   // if True, windows maximized before running the script won't be moved
```

### Usage

```
Usage: window-manager.sh [-p PATH] [-c PATH]

   -p   path to the window-manager folder
   -c   path to the .ini config file
```

### .desktop file

You can use `window-manager.desktop` found in the projects root, and pin it to your taskbar for easier access. Remember to fill out path configuration in that file.
