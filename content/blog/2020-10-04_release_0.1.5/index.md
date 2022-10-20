---
date: 2020-10-04
title: LibrePCB 0.1.5 Released
author: U. Bruhin
---

We are happy to announce LibrePCB 0.1.5 with several long awaited new features
in the library-, schematic- and board editors!


### Highlights

#### Copy&Paste in Schematic- and Board Editors

Finally the clipboard functionality cut, copy and paste are available in the
schematic- and board editors
([#724](https://github.com/LibrePCB/LibrePCB/pull/724),
[#754](https://github.com/LibrePCB/LibrePCB/pull/754))! Just use the keyboard
shortcuts Ctrl+X to cut, Ctrl+C to copy and Ctrl+V to paste schematic- or board
items. In the board editor, it's even possible to paste polygons copied from a
footprint in the library editor.

#### Usability Improvements In All Editors

This release contains a lot of usability improvements, which makes creating
library elements, schematics and boards much easier. Especially drawing traces
and placing vias was one of the weaknesses of LibrePCB -- until now! The tools
to draw traces and place vias have been heavily improved, for example:

- Traces snap to pads and vias even if they are off the grid
- The layer can be switched while drawing a trace, vias are inserted
  automatically
- Vias automatically take the closest net while placing
- Inserted vias are automatically connected to the traces underneath
- Trace and via properties can be changed with keyboard shortcuts while drawing
  a trace

{{< imglink "Draw Trace" "board_editor_draw_trace.gif" >}}

Another inconvenience was that the outline of planes and polygons could only
be modified by specifying the exact vertex coordinates. Now this is much easier
since vertices can be moved, inserted and removed graphically right in the
editors.


### Changelog

#### Library Manager:
- Fix error when downloading a library after an aborted download
  ([#775](https://github.com/LibrePCB/LibrePCB/pull/775))

#### Library Editor:
- Implement "Select All" (Ctrl+A)
  ([#723](https://github.com/LibrePCB/LibrePCB/pull/723))
- Support cycling selection through items under cursor by pressing Shift
  ([#757](https://github.com/LibrePCB/LibrePCB/pull/757))
- Support rotate/mirror/flip while moving items
  ([#769](https://github.com/LibrePCB/LibrePCB/pull/769))
- Support modifying polygons graphically
  ([#773](https://github.com/LibrePCB/LibrePCB/pull/773))
- Copy all categories when duplicating a library element
  ([#765](https://github.com/LibrePCB/LibrePCB/pull/765))
- Fix "Could not move X to Y" error when moving library element
  ([#715](https://github.com/LibrePCB/LibrePCB/pull/715))
- Fix crash when going back in "New Component" wizard
  ([#719](https://github.com/LibrePCB/LibrePCB/pull/719))

#### Schematic Editor:
- Implement clipboard cut/copy/paste
  ([#724](https://github.com/LibrePCB/LibrePCB/pull/724))
- Implement "Select All" (Ctrl+A)
  ([#723](https://github.com/LibrePCB/LibrePCB/pull/723))
- Support cycling selection through items under cursor by pressing Shift
  ([#757](https://github.com/LibrePCB/LibrePCB/pull/757))
- Support cycling through results of the search toolbar
  ([#756](https://github.com/LibrePCB/LibrePCB/pull/756))
- Make component toolbar norm-aware by using preferred symbol variant
  ([#768](https://github.com/LibrePCB/LibrePCB/pull/768))
- Fix leaving tool with when pressing right mouse click while moving
  ([#761](https://github.com/LibrePCB/LibrePCB/pull/761))

#### Board Editor:
- Implement clipboard cut/copy/paste
  ([#754](https://github.com/LibrePCB/LibrePCB/pull/754))
- Implement "Select All" (Ctrl+A)
  ([#723](https://github.com/LibrePCB/LibrePCB/pull/723))
- Heavily improve the "Draw Trace" tool
  ([#733](https://github.com/LibrePCB/LibrePCB/pull/733),
   [#751](https://github.com/LibrePCB/LibrePCB/pull/751),
   [#753](https://github.com/LibrePCB/LibrePCB/pull/753),
   [#749](https://github.com/LibrePCB/LibrePCB/pull/749))
- Heavily improve the "Add Via" tool
  ([#736](https://github.com/LibrePCB/LibrePCB/pull/736))
- Support cycling selection through items under cursor by pressing Shift
  ([#748](https://github.com/LibrePCB/LibrePCB/pull/748))
- Support cycling through results of the search toolbar
  ([#756](https://github.com/LibrePCB/LibrePCB/pull/756))
- Support modifying polygons graphically
  ([#773](https://github.com/LibrePCB/LibrePCB/pull/773))
- Support modifying plane outlines graphically
  ([#774](https://github.com/LibrePCB/LibrePCB/pull/774))
- Don't remove complete trace when changing a device
  ([#746](https://github.com/LibrePCB/LibrePCB/pull/746))
- Fix possibly outdated displayed texts of devices
  ([#770](https://github.com/LibrePCB/LibrePCB/pull/770))
- Fix possibly outdated displayed net names
  ([#771](https://github.com/LibrePCB/LibrePCB/pull/771))

#### ERC:
- Disregard schematic-only components in net pin count
  ([#745](https://github.com/LibrePCB/LibrePCB/pull/745))

#### Miscellaneous:
- Add support for Solaris based systems
  ([#713](https://github.com/LibrePCB/LibrePCB/pull/713))
- Allow unbundling of some vendored libraries
  ([#698](https://github.com/LibrePCB/LibrePCB/pull/698),
   [#742](https://github.com/LibrePCB/LibrePCB/pull/742))
- Fix too restrictive format version check of FontoBene files
  ([fontobene-qt5#673](https://github.com/fontobene/fontobene-qt5/pull/4))
- Various internal code refactorings & improvements
  ([#720](https://github.com/LibrePCB/LibrePCB/pull/720),
   [#760](https://github.com/LibrePCB/LibrePCB/pull/760),
   [#767](https://github.com/LibrePCB/LibrePCB/pull/767), ...)


### Download

The release can be downloaded for all major operating systems from our download
page:

#### https://librepcb.org/download/

Thanks to all contributors for making this awesome release possible!
