# Blender-openSCAD - Blender 💌 OpenSCAD
---

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
*VERY WIP*

## Video Tutorial
📽️ (Youtube)[https://www.youtube.com/watch?v=aZq8ZlmqHJo]


Blender-openSCAD renamed slightly to avoid confusion with the original where the word "blend" was ambigious. Contacted original authors to get status updates. 

 So far thee 'master' branch was renamed to 'main' which is regarded as less-offensive neo-venacular.
 
 Github issues have been enabled and pull requests for ideas/contributions are welcome to this repo. 

The blender project is being integrated with the
 (elasticdotventures/awesome-openscad) RUST/wasm cargo installer for openSCAD.

The historical openSCAD package available on [PyPI](https://pypi.python.org/pypi/BlendSCAD), was installed with pip and this will be installed with cargo. 

Development on the original python seems to be halted; it is hoped that this fork can attach this plugin to communities and take openSCAD in novel directions. 

This fork has the following design goals:

* Ease of Use, quick painless less technically complex install into Blender
	* RUST cargo for Linux/Unix
	* Windows win-get, chocolatey nsis or equivalent

* Compatibility with [VSCode] for editing & synchronization of versions & language service provider intellisense (code checker), import/export pipeline on build. 

* Unified compositional component library that can be embedded for discovering parameterically defined objects & tools. 

## from @3DLIRIOUS/blendSCAD

* [SolidPython](https://github.com/SolidCode/SolidPython) &amp; the goal is for the same scripts to run on each.

* Add new OpenSCAD features, such as text. Aiming for full compatibility with OpenSCAD; the only significant issue at the moment appears to be the Minkowski function.

* Add Blender-only extras and enhancements, such as the ability to work with vertex colors or textures to support 3D printable full color models, and additional modifiers such as Solidify.

* The BlendSCAD Panel will not be supported at the moment, and won't be kept up to date with changes in the underlying module. This may be picked back up again in the future.

Installing in Blender's Python 3 with pip; Blender doesn't come with pip, so we have to install it first:
1. Download [get-pip.py](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)
2. Install pip
```sh
"C:\Program Files\Blender Foundation\Blender\2.78\python\bin\python.exe" get-pip.py
```
3. Install BlendSCAD
```sh
"C:\Program Files\Blender Foundation\Blender\2.78\python\bin\python.exe" -m pip install BlendSCAD
```

The above path is for Blender 2.78 installed in the default location on Windows; modify accordingly for your OS.

The original README is shown below:

---
Blender is a powerful piece of Open Source software which is also useful in the 3D printing space. Coming from OpenSCAD or Tinkercad, there are some issues at the first glance:

*   Revisiting and changing a model seems to be difficult - Joining meshes is less attractive than grouping/ungrouping objects
*   Undo functionality is not that advanced.
*   The parametric approach of OpenSCAD is very powerful and yet easy to learn. Blender's Python console is something you may not even be aware of and parameterizing your first objects with OpenSCAD is definitely much easier.
*   Blender's UI (i.e. the default theme)is way too dark to provide this warm and welcome feeling of Tinkercad or OpenSCAD :-)

This little project started as a proof of concept implementation as I'm just familiarizing myself with Blender and Python. Meanwhile it has matured quite a bit and is a really nice enhancement for Blender.  
Here is a screenshot to show the basic idea: ![](imgs/ScreenshotBlender.png)

### OpenSCAD code

Btw: It's the OpenJSCAD logo

<pre>module logodemo() {
  scale([10,10,10]) {  
    translate([0,0,1.5]) {
     union() {
       difference() {
         cube(size=3, center=true);
         sphere(r=2, center=true);
      }
      intersection() {
          sphere(r=1.3, center=true);
          cube(size=2.1, center=true);
      }
	 }
   }
  }
}
logodemo();
</pre>

![](imgs/Openscad.png)

### Translated to BlendSCAD

...with added some color and treated as two grouped objects

<pre>def logodemo():  
	scale([10,10,10], 
	   translate([0,0,1.5] 
		 , group(   
			 color(purple, difference(
				 cube([3,3,3], center=true)
			   , sphere(r=2, center=true)
			 ))
		   , color(yellow, intersection(
				 sphere(r=1.3, center=true)
			   , cube([2.1,2.1,2.1], center=true)
		   ))	  
		 )
	 )
	)

logodemo()
</pre>

![](imgs/Logo_BlenderSCAD.png)

I've started developing BlendSCAD on Blender 2.68/2.69\. The current version works fine with Blender 2.68 to the recent 2.74 and may still work on older Blender releases (not tested, though). OS wise, I'm using Blender on Windows7 64bit, but also tested it on Ubuntu (well sideloaded on an Android tablet).

## Install Instructions

Installing BlendSCAD is fairly simple: Meanwhile, I've split the project into a python module _blendscad_, default user prefs and startup files for the _config_ folder and the BlendSCAD panel to be placed in the _addons_ folder. Just installing the module is fine, the other two parts can be considered optional. Furthermore, there is a demo script _blendscad_demo.py_ and some more demo files in the _tests_ and _examples_ folders.

#### The blendscad module

First, place the blendscad directory in Blender's module path:

<pre>[installpath]\blender-2.69\2.69\scripts\modules\blendscad
or
[installpath]\blender-2.74\2.74\scripts\modules\blendscad
</pre>

As an alternative, you can also set a path in the console or the demo script to the folder containing the modules.  

#### UI Look and Feel

You can use my **startup.blend** and **userpref.blend** files from the config subfolder optionally. These will provide my Blender Theme adjustments and screen area setup as shown in the screenshot above. Place the content of the "config" folder into the Blender's config folder:

<pre>%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\2.69\config
or
%USERPROFILE%\AppData\Roaming\Blender Foundation\Blender\2.74\config
</pre>

if you are using Windows (Otherwise, refer to the Blender documentation).

#### BlendSCAD panel

Well, this exeeds the original scope of providing OpenSCAD like operations and is rather similar to working with TinkerCAD. If you want to give it a try, install the addon and activate it in the user preferences:

<pre>[installpath]\blender-2.69\2.69\scripts\addons\blendscad_toolbar.py
or
[installpath]\blender-2.74\2.74\scripts\addons\blendscad_toolbar.py
</pre>

#### Getting started

SAVE all open work first, better go to a clean document. Open the demo script _blendscad_demo.py_ in Blender's internal text editor and uncomment the demo section you want to try out. Simply use "run script". This is the easiest way. You can also save your script as part of a .blend file. Again, caution, there is a line in most of my demo scripts to wipe all objects of the open scene first for rapid testing. Congratulations, Blender is now your OpenSCAD-like IDE. You can even have the code compile while typing (Check "Live Edit" in the editor)

#### Alternatively, run via Python Console

This option is preferred if you use an external editor for the code.

<pre>#Optionally, first clear command history in Python Console:
bpy.ops.console.clear(history=True)
filename = "<your path="">/BlendSCAD.py
exec(compile(open(filename).read(), filename, 'exec'))</your> </pre>

In general, I recommend to start Blender from a command line (Windows or Linux). This way you see all error messages and warnings.

#### A few hints

Blender files usually grow with all unlinked objects. It will garbage clean whenever you save and reopen the document. In order to make the "Live Edit" option work reasonable, I explicitly force the deletion (unlink) of intermediate objects and meshes (e.g. before union). Therefore, the files should stay cleaner than while editing a blender file in the usual way.  

A last word of "warning": Pay attention to where your source file is saved. _ALT+S_ will save the file in the editor, _CTRL+S_ will save the "materialized" version of that file inside blender. Changes may be lost if you resync.

### Supported:

*   cube
*   cylinder
*   sphere
*   circle
*   square
*   polygon
*   polyhedron

*   translate
*   rotate
*   mirror
*   scale
*   resize
*   color

*   union
*   difference
*   intersection

*   projection
*   *linear_extrude
*   rotate_extrude
*   hull

*   surface
*   import_, import_stl , *import_dxf
*   export, export_stl, *export_dxf

*   hexagon
*   octagon
*   ellipsoid
*   rcube
*   roundedBox

*   special variables: fs, fa, fn (~ $fs, $fa, $fn)
*   string functions: echo, str, *search
*   math functions: lookup, rands, sign, sin , cos,...

### Extras

*   join, split
*   group, ungroup
*   clone, destruct

*   round_edges
*   dissolve

*   +several (OpenSCAD) demos
*   ...

### Missing

*   minkowski
*   norm
*   multimatrix
*   ...

## The BlendSCAD Panel

This is currently the most active area of my development - subject to change ;-) I wanted to have some interactivity to try some additional operators and tweaks easily. As this is a really simple to do in Blender, I've defined a panel. This is how the first version looked like:

![](imgs/Panel.png)

It mainly reuses some code I've written for the BlendSCAD enhancements. A very handy thing are the multi-object boolean operations: 3 clicks to have a cube, a cylinder and a sphere on the screen, a couple of clicks to align them, selecting several objects (Shift+Right Mouse), then just hit one of the Boolean buttons. Behind the scenes, it will create the required modifiers and apply them. A great productivity gain, I would say. Give it a try. Almost as convenient as Tinkercad (Group and Hole and Undo/Ungroup) still to be done. The object cleanup (using limited dissolve) really cleans up most resulting geometry.  

In general, most operations will be applied to the set of selected objects.  

Object selection differs from the default Blender setup. I've changed the assignment of the mouse selection in order to make tablet operations (without a keyboard) possible.

Speaking of geometry: The user will not even realize when the code is switching from Object to Edit mode (something not always straight forward in Blender, especially when scripting via Python?). There is a Debug-Button which will toggle displaying all object edges even in object mode. Blender could/can be so easy!

As I need to see the "real" console output anyways, I've decided to switch from the single window-multiple area approach to a triple window approach.

![](imgs/BlenderIDE2.png)

Just tweak the paths in the text opening in the startup code (right) and run it. This will make the Panel appear - no full-fledged add-on at the time being.



