---
date: 2022-10-03
title: LibrePCB 0.1.7 Released
author: U. Bruhin
---

Finally it's time again to announce a new release -- LibrePCB 0.1.7 brings
several new features and a lot of usability improvements! This might be the
last release of the 0.1.x series as LibrePCB 0.2.x development is ongoing
as well. But, never say never ;-)

***Note for macOS users:** Our official binaries do not run on macOS 10 anymore.
You need macOS 11 Big Sur or later (or compile LibrePCB from sources).*

### Highlights

#### Measure Tool ([#995](https://github.com/LibrePCB/LibrePCB/pull/995))

Measuring distances in the footprint- and board editors is one of the features
I have been asked for many times. For good reasons, since it is very useful
and thus provided in every serious EDA tool.

LibrePCB now provides a feature-rich ruler in all editors to measure angles and
distances in both metric and imperial units. Thanks to automatic snapping, it's
also possible to measure drill diameters, pad sizes, restrings etc. precisely:

{{< imglink "Measure Tool" "board_editor_measure_tool.gif" >}}

For details, check out the
[corresponding pull request](https://github.com/LibrePCB/LibrePCB/pull/995).
Tip: Once you measured a distance, just press `Ctrl+C` to copy the
measured distance into the clipboard for pasting it e.g. in a calculator.

#### Powerful Print/PDF/Image Export ([#947](https://github.com/LibrePCB/LibrePCB/pull/947))

There was already a PDF and SVG export for schematics and boards available --
but it was *very* limited. In fact, it had no configuration option at all.
Thus for many needs it was not that helpful.

Now this export is replaced by a completely new, highly configurable,
feature-rich export dialog. The main improvements are:

- Configurable page size, orientation & margins
- Configurable scale factor, rotation & mirror
- Configurable colors of background and layers
- Multi-page board export with custom layer sets (e.g. for assembly drawings)
- Support for pixmap output formats (e.g. PNG) with configurable DPI
- Support copying images to clipboard instead of writing to file
- Responsive live preview & non-blocking export operation

{{< imglink "PDF Export Dialog" "board_editor_pdf_export.gif" >}}

For the complete feature list including several screenshots, check out the
[corresponding pull request](https://github.com/LibrePCB/LibrePCB/pull/947).

#### EAGLE Library Import ([#936](https://github.com/LibrePCB/LibrePCB/pull/936))

We all know that libraries are one of the reasons why we don't like switching
to another EDA tool since it would take a lot of time to create all the
personal libraries again. But if you used EAGLE, we have good news! It's now
possible to import whole EAGLE libraries (`*.lbr` with XML format of EAGLE 6
or later) very easily:

{{< imglink "EAGLE Import Wizard" "eagle_library_import.gif" >}}

The import has been tested with several libraries of various EAGLE versions,
but we can't guarantee that it's working properly with any `*.lbr` file.
Please don't hesitate to
[open an issue](https://github.com/LibrePCB/LibrePCB/issues/new/choose) if
you experience an incompatibility.

#### Improved, Configurable Keyboard Shortcuts ([#986](https://github.com/LibrePCB/LibrePCB/pull/986), [#987](https://github.com/LibrePCB/LibrePCB/pull/987), [#988](https://github.com/LibrePCB/LibrePCB/pull/988))

Keyboard shortcuts were another weak point of LibrePCB which I have been asked
for many times. Most tools and actions did not have a shortcut at all,
configuration was not possible and there was no overview about the available
shortcuts.

This release massively changes that situation. There are dozens of
keyboard shortcuts added, they are now fully configurable in the workspace
settings and to always have a quick reference available, LibrePCB is now
able to generate a nice shortcut reference PDF on the fly:

{{< imglink "Shurtcuts Reference" "keyboard_shortcuts_reference.png" "keyboard_shortcuts_reference.pdf" >}}

#### Gerber X3 Pick&Place Export ([#1004](https://github.com/LibrePCB/LibrePCB/pull/1004))

Maybe you already heard about
[Gerber X3](https://www.ucamco.com/en/gerber/gerber-x3), maybe not -- it is a
relatively new export format for pick&place files, based on the well known
Gerber format. In fact, it is exactly the same as Gerber X2, just with some
additional attributes required for purchasing and automated assembly, for
example the part numbers (MPN). The nice thing about this format is that
it is machine-readable, but can also be opened in a standard Gerber viewer
to see a human-readable assembly plan:

{{< imglink "Gerber X3" "gerber_x3_viewer.png" >}}

Some assembly houses already support this format, so it might be good to know
that LibrePCB is now able to generate such files. Unfortunately we don't have a
real part number management yet, but in the mean time you can (optionally)
specify the corresponding information manually in the schematic editor by
adding custom attributes named `MANUFACTURER` and `MPN` to the components.
These attributes will then be respected by the Gerber X3 export.

---

### Changelog

#### Control Panel:

- Allow to hide/dismiss message banners
  ([#1036](https://github.com/LibrePCB/LibrePCB/pull/1036))
- Remove recommendation about licenses when creating a new project
  ([#1033](https://github.com/LibrePCB/LibrePCB/pull/1033))
- Fix UX flaws due to blocking UI when opening project
  ([#958](https://github.com/LibrePCB/LibrePCB/pull/958))

#### Library Editor:

- Add EAGLE library import wizard
  ([#936](https://github.com/LibrePCB/LibrePCB/pull/936))
- Add dedicated tool for drawing arcs
  ([#1011](https://github.com/LibrePCB/LibrePCB/pull/1011))
- Improve polygon tools with Shift modifier, overlay and status messages
  ([#1009](https://github.com/LibrePCB/LibrePCB/pull/1009))
- Fix possible crash when closing tabs while a tool was active
  ([#1010](https://github.com/LibrePCB/LibrePCB/pull/1010))
- Fix possibly unrelated symbol/component/package search results
  ([#1049](https://github.com/LibrePCB/LibrePCB/pull/1049))

#### Schematic Editor:

- Keep state of "Add Component"-dialog and make auto-open optional
  ([#951](https://github.com/LibrePCB/LibrePCB/pull/951),
   [#957](https://github.com/LibrePCB/LibrePCB/pull/957),
   [#983](https://github.com/LibrePCB/LibrePCB/pull/983))
- Show info banner how to add components if schematic is empty
  ([#1040](https://github.com/LibrePCB/LibrePCB/pull/1040))
- Fix copy&paste of multi-symbol components
  ([#985](https://github.com/LibrePCB/LibrePCB/pull/985))

#### Board Editor:

- Polish PCB fabrication output dialog
  ([#1032](https://github.com/LibrePCB/LibrePCB/pull/1032))
- Implement attributes `BOARD_INDEX` and `BOARD_DIRNAME`
  ([#1015](https://github.com/LibrePCB/LibrePCB/pull/1015))
- Avoid creating vias with drill larger than size
  ([#963](https://github.com/LibrePCB/LibrePCB/pull/963))
- Fix modifying rotation of mirrored devices
  ([#955](https://github.com/LibrePCB/LibrePCB/pull/955))
- Fix half-filled plane if outline is not a closed path
  ([#961](https://github.com/LibrePCB/LibrePCB/pull/961))
- Fix visible tooltips for invisible items
  ([#962](https://github.com/LibrePCB/LibrePCB/pull/962))
- Fix adding vertices to last plane edge
  ([#1022](https://github.com/LibrePCB/LibrePCB/pull/1022))

#### Import/Export:

- Add Gerber X3 pick&place export
  ([#1004](https://github.com/LibrePCB/LibrePCB/pull/1004))
- Support joining tangent polylines when importing a DXF
  ([#960](https://github.com/LibrePCB/LibrePCB/pull/960))
- By default, skip devices without pads in BOM/pick&place export
  ([#1002](https://github.com/LibrePCB/LibrePCB/pull/1002))
- Generate NPTH drill file even if there are no NPTH drills
  ([#1012](https://github.com/LibrePCB/LibrePCB/pull/1012))

#### CLI:

- Add support for pick&place export
  ([#1005](https://github.com/LibrePCB/LibrePCB/pull/1005))
- Add `open-project` option `--board-index`
  ([#1017](https://github.com/LibrePCB/LibrePCB/pull/1017))
- Add `open-project` option `--remove-other-boards`
  ([#1016](https://github.com/LibrePCB/LibrePCB/pull/1016))
- Improve argument parsing & console output formatting
  ([#1014](https://github.com/LibrePCB/LibrePCB/pull/1014))

#### Miscellaneous:

- Implement new, more powerful print / image export feature
  ([#947](https://github.com/LibrePCB/LibrePCB/pull/947),
   [#973](https://github.com/LibrePCB/LibrePCB/pull/973))
- Implement distance measure tool in all editors
  ([#995](https://github.com/LibrePCB/LibrePCB/pull/995))
- Refactor & highly improve keyboard navigation
  ([#986](https://github.com/LibrePCB/LibrePCB/pull/986),
   [#1019](https://github.com/LibrePCB/LibrePCB/pull/1019),
   [#1025](https://github.com/LibrePCB/LibrePCB/pull/1025),
   [#1038](https://github.com/LibrePCB/LibrePCB/pull/1038),
   [#1043](https://github.com/LibrePCB/LibrePCB/pull/1043))
- Make keyboard shortcuts configurable in workspace settings
  ([#987](https://github.com/LibrePCB/LibrePCB/pull/987))
- Add "Keyboard Shortcuts Reference" menu item to all editors
  ([#988](https://github.com/LibrePCB/LibrePCB/pull/988))
- Implement "Find" and "Find Next/Previous" in all editors
  ([#984](https://github.com/LibrePCB/LibrePCB/pull/984))
- Add "apply" button to via- and component properties dialog
  ([#952](https://github.com/LibrePCB/LibrePCB/pull/952))
- Support configuring custom web browser, file manager and PDF reader
  ([#694](https://github.com/LibrePCB/LibrePCB/pull/694),
   [#996](https://github.com/LibrePCB/LibrePCB/pull/996),
   [#1035](https://github.com/LibrePCB/LibrePCB/pull/1035))
- Show waiting spinner in tree/list views during library scan
  ([#1037](https://github.com/LibrePCB/LibrePCB/pull/1037))
- Auto-refresh all category tree views after workspace library scan
  ([#950](https://github.com/LibrePCB/LibrePCB/pull/950))
- Make polygon/plane vertex handle size independent of zoom
  ([#1021](https://github.com/LibrePCB/LibrePCB/pull/1021))
- Automatically abort blocking tool in other editor
  ([#1026](https://github.com/LibrePCB/LibrePCB/pull/1026))
- Center text in all progress bars
  ([#1020](https://github.com/LibrePCB/LibrePCB/pull/1020))
- Save only modified workspace settings to file, keeping unknown settings
  ([#964](https://github.com/LibrePCB/LibrePCB/pull/964))
- Improve item selection behavior in all editors
  ([#1031](https://github.com/LibrePCB/LibrePCB/pull/1031))
- Improve formatting & consistency of logging messages
  ([#1023](https://github.com/LibrePCB/LibrePCB/pull/1023))
- Make project library updater a real dialog
  ([#1034](https://github.com/LibrePCB/LibrePCB/pull/1034))
- Polish some UI details, fixing several issues on macOS
  ([#1043](https://github.com/LibrePCB/LibrePCB/pull/1043))
- Fix some inconsistent behavior in editors
  ([#982](https://github.com/LibrePCB/LibrePCB/pull/982))
- Fix rotation & height of some symbol / pin texts
  ([#967](https://github.com/LibrePCB/LibrePCB/pull/967))
- Fix some minor rounding issues
  ([#954](https://github.com/LibrePCB/LibrePCB/pull/954),
   [#959](https://github.com/LibrePCB/LibrePCB/pull/959))

#### Building/Packaging/Deployment:

- Build official macOS binaries on macOS 11 Big Sur
  ([#1003](https://github.com/LibrePCB/LibrePCB/pull/1003))
- Enable HiDPI support for macOS in `Info.plist`
  ([#945](https://github.com/LibrePCB/LibrePCB/pull/945))
- Patch AppImages to remove dependency to `libfuse2`
  ([#1018](https://github.com/LibrePCB/LibrePCB/pull/1018))
- Allow in-source builds
  ([#931](https://github.com/LibrePCB/LibrePCB/pull/931))
- Fix potential numeric issues with `-march=haswell`
  ([#991](https://github.com/LibrePCB/LibrePCB/pull/991))
- Fix unbundling `muparser`
  ([#937](https://github.com/LibrePCB/LibrePCB/pull/937),
   [#970](https://github.com/LibrePCB/LibrePCB/pull/970))
- Fix & improve unbundling of GTest/GMock
  ([#1013](https://github.com/LibrePCB/LibrePCB/pull/1013))
- Update image licenses
  ([#941](https://github.com/LibrePCB/LibrePCB/pull/941))

#### Internal:

- Refactor organization of sources, static libraries and namespaces
  ([#939](https://github.com/LibrePCB/LibrePCB/pull/939))
- Refactor database classes, fixing some minor issues
  ([#949](https://github.com/LibrePCB/LibrePCB/pull/949))
- Detect workpace `data` directory which will be used in LibrePCB 0.2.x
  ([#979](https://github.com/LibrePCB/LibrePCB/pull/979))
- Fix duplicate graphics items code & improve renderings
  ([#969](https://github.com/LibrePCB/LibrePCB/pull/969),
   [#975](https://github.com/LibrePCB/LibrePCB/pull/975),
   [#981](https://github.com/LibrePCB/LibrePCB/pull/981))
- Fix possible (theoretical) crash during project library error handling
  ([#968](https://github.com/LibrePCB/LibrePCB/pull/968))

---

### Download

The release can be downloaded for all major operating systems from our download
page:

#### https://librepcb.org/download/

Have fun with this new release, I hope the new features are useful for you :-)
If you like it, I'd highly appreciate if you consider making a small
[donation](/donate) to support the ongoing development {{< icon "icon-heart" >}}
