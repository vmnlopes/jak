## Jade Application Kit

[![Join the chat at https://gitter.im/JadeApplicationKit/Lobby](https://badges.gitter.im/JadeApplicationKit/Lobby.svg)](https://gitter.im/JadeApplicationKit/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c79991176d484d50960a36007749b6a6)](https://www.codacy.com/app/vmnlop/Jade-Application-Kit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vmnlopes/Jade-Application-Kit&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/vmnlopes/Jade-Application-Kit.svg?branch=master)](https://travis-ci.org/vmnlopes/Jade-Application-Kit)

Official documentation: Work in progress!

## Introduction

## This is a DEV Preview not finish but it works!
Development may be slow as i am busy!

 JAK is built in Python 3 on top of GTK3 and Webkit2.
 It is only dependent on PyGi module you should have it pre packaged in any linux distro!
  
You can write hybrid Web and Desktop applications on Linux in a webview, including but not limited to DOCKS, Widgets, or any other sort of apps.
 This works same way as Node Webkit or Electron with a few diferences.
 
## Faqs
 
 * Wy was this build we already have software that does that?
 
  * Other available software did not fullfill my needs. This was build out of my desire of learning python, since i love the syntax and i am building some applications with python and HTML and got fed up off building webviews over and over!
  
 * Does this comes with a server?
  
  * NO, you dont need a server to build a HTML5, Javascript, CSS3 Application.
  * But if you require one, you can use any server you like or even build your own!
  
 * Do i need to know Python?
  
  * NO!
 
 * Is this cross platform?
 
  THIS WAS NOT TESTED OR IS OFFICIALY SUPPORTED FOR NOW!
  * There are packages for your Linux distro, for Windows head to [Pygi website](https://wiki.gnome.org/action/show/Projects/PyGObject) and MacOx i tink you have to compile it, instructions [here](https://wiki.gnome.org/action/show/Projects/GTK+/OSX/Building) and [here](https://wiki.gnome.org/Projects/GTK+/OSX/Python).

 * Does it work with PyPy
 
  * Perhaps! there is a version of PyGobject for PyPy, but that was not tested.
  
## Features
 * You can use any scripting language you like (PHP, Python, Ruby, Javascript)!
 * Use HTML5, CSS3 or Webgl.
 * Use any backend server or none at all!
 * Have your applications run in the browser with websockets using the GTK Broadway backend.
 
## Instalation
using pip
```
sudo pip install jak
```
using Git
```
git clone https://github.com/vmnlopes/Jade-Application-Kit.git
cd ./Jade-Application-Kit
chmod +x ./jak
```
## Usage

Wen pointing to a folder JAK will look for index.html in your application root.
```
jak /path/to/application/directory
```
```
jak http://Address
```
```
debug mode --> jak -d  myAppRoot
help       --> jak -h
```
JAK Will look for 2 files in the root of you app, app.json and window.css.
 * window.css can be used to customize the window look if you want to, this is not required as it uses the defaul GTK Theme look.
 
 * app.json options
   
    * hint_type   you got 3 options.
      * dock can be used to create panels or widgets. 
      * desktop will spawn a fullscreen undecorated window that will stay below all windows.
      * leave blank for a normal application window.

    * fullscreen 
      * leave blank and above sizes will be used or type yes
    * resizable  
      * leave blank or type "no"
    * decorated 
      * leave blank for decorations or type "no"
    * transparent 
      * leave blank for normal or type "yes"  
    * debug 
      * leave blank or type "yes", you can also use (-d option in the command line).
 
 ```
 your app.json should look like this!
 
 {
  "app": {
  
  "name":        "my application name",
  "description": "some description",
  "version":     "0.1",
  "author":      "your name",
  "url":         "your application url",
  "license":     "GPL",
  "help":        ""
  
  },
  
  "window": {
    "icon":        "your icon path",
    "hint_type":   "dock", 3 options --> dock, desktop or leave blank for normal apps
    "width":       800,
    "height":      600,
    "fullscreen":  "yes"
    "resizable":   "no",  
    "decorated":   "no",  
    "transparent": "yes"  
    
  },
  
  "webkit": {
  
    "debug":  "yes"   
  }
}
```

## Known Issues
 * broadway backend segfaults.
 * Transparent windows are exprimental, window shadows that should not be there wen using transparent window in Dock mode.
 * missing options in app.json will throw an error and crash you app.
 * theres no way of positioning windows in the screen that was not implemented yet but it will be.
 
## SUGESTIONS ARE WELCOME!

## License

*Copyright (c) 2015-2016, Vitor Lopes. All rights reserved.*

JAK is covered by the GPL license.
