---
date: 2019-04-21
title: LibrePCB 0.1.1 Released
author: U. Bruhin
---

There was a lot of progress the last months, and now it's time to provide a new
release containing all the improvements. In this release, especially the
library editor was heavily improved to make it more powerful and easier to
use. See the highlights and the detailed changelog below.

**Thanks a lot to all contributors and sponsors for pushing LibrePCB one step
further!**


### Highlights

#### Design Rule Check for Library Elements ([#381](https://github.com/LibrePCB/LibrePCB/pull/381))

In virtually every EDA tool it's easy to make mistakes when creating library
elements like symbols or packages. Usually you notice such mistakes later in the
schematic or board editors because of the ERC or DRC, so you have to go back
to the library editor which costs time and nerves. Many projects try to solve
this problem using documentation and design guidelines. But humans are generally
lazy and don't like to read those guidelines.

LibrePCB 0.1.1 goes a different way: It shows potential problems with library
elements right in the library editor, so you can fix them immediately, i.e.
before they are used in any schematic or board. And even better, for many of the
warnings, the library editor provides the corresponding fix with just one click!
Let's see how it works:

{{< imglink "Library Element Checks" "library_editor_rulecheck.gif" >}}<br/><br/>

#### More Powerful Symbol Variants ([#430](https://github.com/LibrePCB/LibrePCB/pull/430))

LibrePCB uses component symbol variants to support different graphical
representations for the same component, for example to distinguish between
American and European norms. See
[this talk at FOSDEM](https://www.youtube.com/watch?v=vu-h5y6tK34) (slides
[here](https://archive.fosdem.org/2018/schedule/event/cad_librepcb/attachments/slides/2267/export/events/attachments/cad_librepcb/slides/2267/librepcb_slides.pdf))
for details.

Although this was already implemented in LibrePCB 0.1.0, it was not very
powerful yet because in the "Add Component" dialog you had to select the
desired symbol variant manually every time. As typically the European symbol
variants were selected by default, it was especially annoying for Americans.

Now with the 0.1.1 release you can specify your preferred norm in the project
settings, which will make the "Add Component" dialog pre-select the symbol
variant which matches your preferred norm automatically! If you like to use
American symbols, just add the norm "IEEE 315" to your project settings:

{{< imglink "Project Settings Dialog" "project_settings_dialog_norm.png" >}}<br/><br/>

#### Transactional File System ([#422](https://github.com/LibrePCB/LibrePCB/pull/422))

This change is not directly visible to users, but it's still noteworthy because
it's a very fundamental refactoring of the file system access of libraries and
projects. The file system access is now transaction-based, which has several
advantages:

- More reliable save/autosave mechanism, making libraries and projects even more
  robust against file access issues or application crashes.
- Cleaner software architecture, leading to less error-prone code.
- Much more future-proof as it allows to implement features which were not
  possible until now.

### Critical Bugfixes

Obround pads which are higher than wide (i.e. `height > width`) were rendered
wrong in the package and board editors of LibrePCB 0.1.0. In particular, their
orientation on screen was wrong by 90 degrees, while the Gerber output was
correct. This release fixes the wrong orientation, so if you have any pad
affected by this bug, it will now appear 90° rotated compared to the 0.1.0
release. See issue [#424](https://github.com/LibrePCB/LibrePCB/issues/424) for
details.


### Changelog

#### Library Manager:
- Add "select all" checkbox to install/update all libraries at once
  ([#415](https://github.com/LibrePCB/LibrePCB/pull/415))
- Various small layout improvements / memorize window geometry
  ([#402](https://github.com/LibrePCB/LibrePCB/pull/402))

#### Library Editor:
- Add rule check for library elements
  ([#381](https://github.com/LibrePCB/LibrePCB/pull/381))
- Add clipboard functionality (cut/copy/paste) to symbol and package editors
  ([#442](https://github.com/LibrePCB/LibrePCB/pull/442))
- Add search field to symbol/package/component chooser dialogs
  ([#443](https://github.com/LibrePCB/LibrePCB/pull/443))
- Support undo/redo also for library element metadata
  ([#375](https://github.com/LibrePCB/LibrePCB/pull/375))
- Make tabs closable with middle mouse button
  ([#388](https://github.com/LibrePCB/LibrePCB/pull/388))
- Add context menus to overview tab
  ([#380](https://github.com/LibrePCB/LibrePCB/pull/380),
  [#425](https://github.com/LibrePCB/LibrePCB/pull/425))
- Display element name in "save" action
  ([#419](https://github.com/LibrePCB/LibrePCB/pull/419))
- Disable menu items if not needed for the opened element
- Change default package line width to 0.2mm
  ([#413](https://github.com/LibrePCB/LibrePCB/pull/413))
- Sort component signal dropdown in device editor by name
  ([#427](https://github.com/LibrePCB/LibrePCB/pull/427))
- Fix possibly outdated information in component signal editor
  ([#398](https://github.com/LibrePCB/LibrePCB/pull/398))
- Fix layout issues of symbol-, package-, and component chooser dialogs
  ([#439](https://github.com/LibrePCB/LibrePCB/pull/439))
- Start library rescan if library modified

#### Schematic Editor:
- Add project settings dialog
  ([#430](https://github.com/LibrePCB/LibrePCB/pull/430))
- Pre-select symbol variant in "Add Component" dialog by norm
  ([#430](https://github.com/LibrePCB/LibrePCB/pull/430))
- Improve search in "Add Component" dialog
  ([#444](https://github.com/LibrePCB/LibrePCB/pull/444))
- Fix unreadable text in ERC dock widget with Qt 5.12
  ([#437](https://github.com/LibrePCB/LibrePCB/pull/437))

#### Board Editor:
- Fix empty view after removing a board
  ([#431](https://github.com/LibrePCB/LibrePCB/pull/431))

#### CLI:
- Add support for opening `*.lppz` project files
  ([#433](https://github.com/LibrePCB/LibrePCB/pull/433))
- Allow to specify custom fabrication output settings
  ([#434](https://github.com/LibrePCB/LibrePCB/pull/434))
- Add `open-library` command
  ([#435](https://github.com/LibrePCB/LibrePCB/pull/435))

#### Miscellaneous:
- Make runnable on FreeBSD
  ([#417](https://github.com/LibrePCB/LibrePCB/pull/417))
- Remove backward compatibility to pre-0.1 file format
  ([#420](https://github.com/LibrePCB/LibrePCB/pull/420))
- Refactor file access with a transactional file system
  ([#422](https://github.com/LibrePCB/LibrePCB/pull/422))
- Refactor/improve workspace libraries handling
  ([#400](https://github.com/LibrePCB/LibrePCB/pull/400))
- Use separate `*.sqlite` files for each database version
  ([#401](https://github.com/LibrePCB/LibrePCB/pull/401))
- Load category trees from database instead of file system
  ([#421](https://github.com/LibrePCB/LibrePCB/pull/421))
- Filter all category trees to show only relevant entries
  ([#426](https://github.com/LibrePCB/LibrePCB/pull/426))
- Fix possible wrong orientation of obround pads
  ([#428](https://github.com/LibrePCB/LibrePCB/pull/428))
- Fix cell height issues of several tables on high DPI displays
  ([#429](https://github.com/LibrePCB/LibrePCB/pull/429))
- Add support for exporting projects to `*.lppz` archives
  ([#433](https://github.com/LibrePCB/LibrePCB/pull/433))
- Update default layer colors
  ([#440](https://github.com/LibrePCB/LibrePCB/pull/440))
- Update Fontobene stroke fonts
  ([#438](https://github.com/LibrePCB/LibrePCB/pull/438))

#### New languages:
- [Polish](https://www.transifex.com/librepcb/librepcb-application/language/pl/)
  (29% translated)
- [Chinese](https://www.transifex.com/librepcb/librepcb-application/language/zh_CN/)
  (14% translated)
- [Spanish](https://www.transifex.com/librepcb/librepcb-application/language/es/)
  (0% translated)


### Download

The release can be downloaded for all major operating systems on our download
page:

#### https://librepcb.org/download/
