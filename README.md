Open In Total Commander
===========================
Author: Björn Carlsson
License: MIT
https://github.com/HackerBaloo/SublimeOpenInTotalCommander

About
-----
A sublime plugin that allows you to open selected file 
(by pressing'ctrl+shift+o') in Total Commander
or other app if you tweek the settings a bit.

Usage
-----
All you need to do is to press 'ctrl+shift+o' and 
Open in Total Commander will open the selected file in Total Commander 
or another app if you have changed the  settings

Configuration
-------------
Default:
	// Environment variabel with path to Total Commander
    // if sublime is started from Total Commander you already have 
    // COMMANDER_PATH 
    "path_environment_variable": "COMMANDER_PATH",
    "executable": "TOTALCMD.EXE",
    // {path} refers to open file/buffer
    "aruments": "/O /P=L /L=\"{path}\""

On linux if  have tried this:
    // Environment variabel with path to Total Commander
    // if sublime is started from Total Commander you already have 
    // COMMANDER_PATH 
    "path_environment_variable": "",
    "executable": "/usr/bin/nautilus",
    // {path} refers to active file/buffer
    "aruments": "{path}"


Installation
------------
**With Package Control:** The easiest way to install Open In Total Commander is
by using the [Package Control plugin]
(http://wbond.net/sublime_packages/package_control).

**Without Git:** Download the latest source from 
[GitHub](https://github.com/HackerBaloo/SublimeOpenInTotalCommander) and copy 
the Open In Total Commander folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone https://github.com/HackerBaloo/SublimeOpenInTotalCommander

The "Packages" directory can be found in the following locations:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

