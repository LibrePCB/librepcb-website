---
date: 2018-11-04
title: LibrePCB 0.1.0 RC2 Released
author: U. Bruhin
---

After two weeks of testing, we have a new release candidate ready with some
bugfixes and usability improvements:


### Changelog

#### Control Panel:
- Hide non-existent recent and favorite projects
- Hide debug tools in workspace settings dialog

#### Library Manager:
- Don't show 100% progress while extracting ZIP

#### Library Editor:
- Fix saving of component symbol position/rotation
  ([#356](https://github.com/LibrePCB/LibrePCB/issues/356))

#### Schematic Editor:
- Fix resizing of "Add Component" dialog caused by long device names

#### Board Editor:
- Fix crash when trying to connect trace to pad without net
- Fix too high default width of the dock widget at the right
- Fix possibly hidden layers in footprint preview of the "Place Devices" dock
- Show warning in the "Place Devices" dock if no matching device found in
  library
- Set default board size to 100x80mm
- Set default grid interval to 0.635mm

#### Miscellaneous:
- Allow deselecting items while keeping other items selected
  ([#361](https://github.com/LibrePCB/LibrePCB/pull/361))
- Add attribute units "current" and "power"

#### New languages:
- Esperanto (8% translated)
- Italian (20% translated)


### Download

The release candidate can be downloaded for all major operating systems at our
download page:

#### https://librepcb.org/download/
