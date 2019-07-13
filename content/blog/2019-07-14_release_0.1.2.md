---
date: 2019-07-14
title: LibrePCB 0.1.2 Released
author: U. Bruhin
---

This is mainly a bugfix release which fixes some usability, compatibility and
functional issues of the 0.1.1 release.


### Highlights

#### Support latest build environments

The dependencies `quazip`, `googletest`, `optional` and `type_safe` were
updated ([#476](https://github.com/LibrePCB/LibrePCB/pull/476)) and some
deprecation warnings were fixed
([#478](https://github.com/LibrePCB/LibrePCB/pull/478)). Now LibrePCB also
compiles with GCC 9.x and Qt 5.13 without any warnings.

Since we migrated from Travis-CI to Azure Pipelines
([#458](https://github.com/LibrePCB/LibrePCB/pull/458)), CI is now able to
build on Ubuntu 19.04 with GCC 9.x to ensure compatibility with recent build
environments.

#### Improved table widgets

The table widgets -- especially in the library editor -- behaved a bit strange
and sometimes even buggy. After refactoring the implementation of
the observer pattern in low-level classes
([#449](https://github.com/LibrePCB/LibrePCB/pull/449)), we were able to replace
most `QTableWidget` tables by `QTableView` using
[Qt's model/view framework](https://doc.qt.io/qt-5/model-view-programming.html)
([#456](https://github.com/LibrePCB/LibrePCB/pull/456)). This heavily improves
the usability and stability of our table widgets, see details in the changelog
below.


### Changelog

#### Library Editor:
- Rename library overview context menu item "copy" to "duplicate"
  ([#447](https://github.com/LibrePCB/LibrePCB/pull/447))
- Preselect pin name when opening symbol pin properties dialog
  ([#453](https://github.com/LibrePCB/LibrePCB/pull/453))

#### Schematic Editor:
- Fix net label offset after mirroring
  ([#451](https://github.com/LibrePCB/LibrePCB/pull/451))

#### Board Editor:
- Fix unintended tool change after double click on footprint
  ([#464](https://github.com/LibrePCB/LibrePCB/pull/464))
- Fix inconsistent appearance of polygons between editor and Gerber export
  ([#479](https://github.com/LibrePCB/LibrePCB/pull/479))

#### Miscellaneous:
- Change predefined norms to "IEC 60617" + "IEEE 315"
  ([#455](https://github.com/LibrePCB/LibrePCB/pull/455))
- Enable scrolling with both axis when pressing Ctrl
  ([#467](https://github.com/LibrePCB/LibrePCB/pull/467))
- Refactor all table widgets using Qt's model/view framework
  ([#456](https://github.com/LibrePCB/LibrePCB/pull/456)):
  - Fix application crashes with newer Qt versions when editing table content
  - Fix possibly outdated table content when underlying data changes (e.g. on
    undo/redo)
  - Sort tables where reasonable (some tables even allow the user to sort by
    specific column)
  - Slightly improved error handling when entering invalid data into table cells
  - In some tables, allow inserting multiple rows at once (e.g. the term "1..5"
    creates 5 rows, from "1" to "5")
  - Various other small improvements

#### New languages:
- [Turkish](https://www.transifex.com/librepcb/librepcb-application/language/tr/)
  (6% translated)


### Download

The release can be downloaded for all major operating systems on our download
page:

#### https://librepcb.org/download/
