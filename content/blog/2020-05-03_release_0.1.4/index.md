---
date: 2020-05-03
title: LibrePCB 0.1.4 Released
author: U. Bruhin
---

This minor release is one more important step to make LibrePCB more powerful
and to improve usability of the user interface.


### Highlights

#### Usability Improvements

The user interface got many usability improvements to make creating libraries
and projects more efficient. For example the schematic- and board editors now
allow searching for symbols resp. devices
([#671](https://github.com/LibrePCB/LibrePCB/pull/671)):

{{< imglink "Search Symbol" "schematic_editor_search.gif" >}}

Furthermore, all input fields for length values (line width, drill diameter,
coordinate etc.) are now displayed in the unit configured in the workspace
settings ([#684](https://github.com/LibrePCB/LibrePCB/pull/684)). The unit of
each input field can even be changed individually and gets saved and restored
automatically. And you can now enter mathematical expressions and optionally
append a unit (e.g. "mm") which will then be evaluated:

{{< imglink "Search Symbol" "length_input_unit.gif" >}}

#### Pick&Place and SVG Export

This release adds a pick&place CSV file export
([#639](https://github.com/LibrePCB/LibrePCB/pull/639)) so LibrePCB is now
also suitable to design PCBs which will be assembled by pick&place machines:

{{< imglink "Pick&Place Export" "pickplace_export_dialog.png" >}}

In addition, an SVG export has been implemented for both, schematics and
boards ([#656](https://github.com/LibrePCB/LibrePCB/pull/656)). This allows to
postprocess them in a vector graphics tool for various purposes.

À propos file export: The BOM CSV export is now comma-separated instead of
semicolon-separated ([#678](https://github.com/LibrePCB/LibrePCB/pull/678)).
This improves compatibility with CSV readers.


### Compatibility Note

LibrePCB 0.1.4 uses exactly the same file format for projects as all previous
0.1.x releases and are thus fully compatible.

However, previous versions had a bug which allowed to have linebreaks in net
names ([#603](https://github.com/LibrePCB/LibrePCB/issues/603)). This has been
fixed in 0.1.4, and since we expect (or hope…) no projects to be affected by
this bug, no automatic upgrade mechanism has been implemented. If you still
run into the issue that a project cannot be opened with LibrePCB 0.1.4, the
affected net names need to be fixed manually. Please don't hesitate to
[contact us](https://librepcb.org/discuss/) to get help with the migration.


### Changelog

#### Library Editor:
- Add "filter" toolbar to filter element lists
  ([#673](https://github.com/LibrePCB/LibrePCB/pull/673))
- Support moving elements to other library
  ([#638](https://github.com/LibrePCB/LibrePCB/pull/638))
- Show warning in device editor if no pads are connected
  ([#680](https://github.com/LibrePCB/LibrePCB/pull/680))

#### Schematic Editor:
- Add SVG export for sheets
  ([#656](https://github.com/LibrePCB/LibrePCB/pull/656))
- Add "search" toolbar to find symbols in sheets
  ([#671](https://github.com/LibrePCB/LibrePCB/pull/671))
- Add possibility to rename sheets
  ([#640](https://github.com/LibrePCB/LibrePCB/pull/640))
- Fix possibly wrapping of items in schematic pages dock
  ([#685](https://github.com/LibrePCB/LibrePCB/pull/685))

#### Board Editor:
- Add pick&place file export
  ([#639](https://github.com/LibrePCB/LibrePCB/pull/639))
- Add SVG export for boards
  ([#656](https://github.com/LibrePCB/LibrePCB/pull/656))
- Add "search" toolbar to find devices in boards
  ([#671](https://github.com/LibrePCB/LibrePCB/pull/671))
- Sort items in "Change Device" context menu
  ([#677](https://github.com/LibrePCB/LibrePCB/pull/677))
- Fix duplicate vertices when drawing polygons
  ([#672](https://github.com/LibrePCB/LibrePCB/pull/672))
- Fix possibly disappearing airwires in some situations
  ([#687](https://github.com/LibrePCB/LibrePCB/pull/687))

#### BOM Export:
- Use comma instead of semicolon as separator
  ([#678](https://github.com/LibrePCB/LibrePCB/pull/678))

#### Miscellaneous:
- Deny newlines in net names and other identifiers
  ([#637](https://github.com/LibrePCB/LibrePCB/pull/637))
- Speed up UUID validation and thus the library scan
  ([#651](https://github.com/LibrePCB/LibrePCB/pull/651))
- Respect configured workspace length unit in editors
  ([#684](https://github.com/LibrePCB/LibrePCB/pull/684))
- Respect configured grid unit in statusbar of editors
  ([#689](https://github.com/LibrePCB/LibrePCB/pull/689))
- Improve keyboard navigation in dialogs
  ([#690](https://github.com/LibrePCB/LibrePCB/pull/690))
- Use wizard to create and switch workspace from ControlPanel
  ([#688](https://github.com/LibrePCB/LibrePCB/pull/688))
- Split workspace chooser and workspace initialization wizard
  ([#652](https://github.com/LibrePCB/LibrePCB/pull/652))
- Fix falling back to system language for untranslated strings
  ([#645](https://github.com/LibrePCB/LibrePCB/pull/645))
- Various internal code improvements and refactoring
- Many translation improvements and fixes

#### Installer:
- Change default installation directory on macOS to `/Applications`
  ([#644](https://github.com/LibrePCB/LibrePCB/pull/644))

#### New languages:
- [Czech](https://www.transifex.com/librepcb/librepcb-application/language/cz/)
  (93% translated)
- [Chinese (Taiwan)](https://www.transifex.com/librepcb/librepcb-application/language/zh_TW/)
  (99% translated)


### Download

The release can be downloaded for all major operating systems from our download
page:

#### https://librepcb.org/download/
