---
date: 2019-11-30
title: LibrePCB 0.1.3 Released
author: U. Bruhin
---

This release adds a lot of (long-awaited) new features and important bugfixes
to LibrePCB.


### Highlights

#### Design Rule Check for Boards ([#581](https://github.com/LibrePCB/LibrePCB/pull/581))

Finally the board editor got a design rule check! It checks a PCB for common
mistakes like missing connections, too small clearances (or shorts), or too
thin copper elements. A new dock widget shows the reported messages and
clicking on a message displays the issue in the board view.

{{< imglink "DRC" "board_editor_drc.gif" >}}<br/>

Please note that the new design rule options are not yet saved to files, so
you have to re-enter them after opening the project the next time. This will
be implemented in the next major release of LibrePCB.

#### BOM Export ([#499](https://github.com/LibrePCB/LibrePCB/pull/499))

Now it's also possible to export the bill of materials (BOM) of a LibrePCB
project to a CSV file. In addition to some predefined columns, you can add
arbitrary component attributes as additional columns to the CSV:

{{< imglink "DRC" "bom_export_dialog.png" >}}

#### Print Boards ([#567](https://github.com/LibrePCB/LibrePCB/pull/567))

Boards can now be printed and exported to PDF, with respecting the currently
visible layers. This allows for example to create assembly plans like this:

{{< imglink "DRC" "board_editor_assembly_plan.png" >}}


### Changelog

#### Library Editor:
- Add mirror functionality to symbol/package editors
  ([#569](https://github.com/LibrePCB/LibrePCB/pull/569))
- Show footprint pad names in package editor
  ([#570](https://github.com/LibrePCB/LibrePCB/pull/570))
- Add more widgets to package text drawing command toolbar
  ([#521](https://github.com/LibrePCB/LibrePCB/pull/521))
- Adjust default values of symbol and package elements
  ([#523](https://github.com/LibrePCB/LibrePCB/pull/523))
- Remove underscore from predefined text placeholders
  ([#555](https://github.com/LibrePCB/LibrePCB/pull/555))
- Fix possibly missing message box when closing tab
  ([#563](https://github.com/LibrePCB/LibrePCB/pull/563))

#### Schematic Editor:
- Add BOM export dialog
  ([#499](https://github.com/LibrePCB/LibrePCB/pull/499))
- Allow changing pre-selected device of components
  ([#565](https://github.com/LibrePCB/LibrePCB/pull/565))
- Provide more options when renaming net segments
  ([#532](https://github.com/LibrePCB/LibrePCB/pull/532))
- Initialize `*.lppz` export filename with default value
  ([#524](https://github.com/LibrePCB/LibrePCB/pull/524))
- Fix missing device when adding component multiple times
  ([#561](https://github.com/LibrePCB/LibrePCB/pull/561))

#### Board Editor:
- Add design rule check
  ([#581](https://github.com/LibrePCB/LibrePCB/pull/581))
- Add PDF export and print support
  ([#567](https://github.com/LibrePCB/LibrePCB/pull/567))
- Add tool to measure wire length
  ([#564](https://github.com/LibrePCB/LibrePCB/pull/564))
- Allow to hide copper planes
  ([#531](https://github.com/LibrePCB/LibrePCB/pull/531))
- Allow rotating while moving items
  ([#533](https://github.com/LibrePCB/LibrePCB/pull/533))
- Add device context menu item "snap to grid"
  ([#525](https://github.com/LibrePCB/LibrePCB/pull/525))
- Fix missing plane cut-out for board outlines in footprints
  ([#501](https://github.com/LibrePCB/LibrePCB/pull/501))
- Fix invisible zero-width circles/polygons
  ([#502](https://github.com/LibrePCB/LibrePCB/pull/502))
- Fix wrong rotation of mirrored pads in plane cut-outs
  ([#509](https://github.com/LibrePCB/LibrePCB/pull/509))

#### Gerber Export:
- Add support for non-square octagon pads
  ([#507](https://github.com/LibrePCB/LibrePCB/pull/507))
- Always use multi-quadrant mode for arcs
  ([#504](https://github.com/LibrePCB/LibrePCB/pull/504))
- Fix possibly wrong position of circles in footprints
  ([#508](https://github.com/LibrePCB/LibrePCB/pull/508))

#### CLI:
- Add `--strict` option
  ([#583](https://github.com/LibrePCB/LibrePCB/pull/583))

#### Miscellaneous:
- Implement pinch to zoom in all graphics views
  ([#477](https://github.com/LibrePCB/LibrePCB/pull/477))
- Add menu items to toggle visibility of dock widgets
  ([#487](https://github.com/LibrePCB/LibrePCB/pull/487))
- Support copying and moving rows in polygon editor dialogs
  ([#489](https://github.com/LibrePCB/LibrePCB/pull/489))
- Auto-select attribute unit when entering unit in value field
  ([#491](https://github.com/LibrePCB/LibrePCB/pull/491))
- Replace spinboxes/comboboxes with unit-aware edit widgets
  ([#520](https://github.com/LibrePCB/LibrePCB/pull/520))
- Provide `*.tar.gz` archive with pre-built binaries for deployment on Linux
  ([#571](https://github.com/LibrePCB/LibrePCB/pull/571))
- Fix broken settings when closing windows with OpenGL enabled
  ([#503](https://github.com/LibrePCB/LibrePCB/pull/503))
- Fix possible crash when re-opening symlinked projects
  ([#573](https://github.com/LibrePCB/LibrePCB/pull/573))
- Fix possibly wrong grab area of various graphics items
  ([#582](https://github.com/LibrePCB/LibrePCB/pull/582))

#### New languages:
- [Slovak](https://www.transifex.com/librepcb/librepcb-application/language/sk/)
  (98% translated)
- [French](https://www.transifex.com/librepcb/librepcb-application/language/fr/)
  (4% translated)


### Download

The release can be downloaded for all major operating systems on our download
page:

#### https://librepcb.org/download/
