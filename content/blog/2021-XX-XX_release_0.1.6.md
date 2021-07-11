---
date: 2021-XX-XX
title: LibrePCB 0.1.6 Released
author: U. Bruhin
---

### Highlights

- UuidGenerator: Add quazip build dependency
  ([#788](https://github.com/LibrePCB/LibrePCB/pull/788))
- Update quazip submodule
  ([#790](https://github.com/LibrePCB/LibrePCB/pull/790))
- BoardDesignRules: Fix loading max. stopmask drill diameter
  ([#786](https://github.com/LibrePCB/LibrePCB/pull/786))
- Board editor: Fix staying in the "place device" tool
  ([#794](https://github.com/LibrePCB/LibrePCB/pull/794))
- Only set QUAZIP_STATIC for static builds
  ([#789](https://github.com/LibrePCB/LibrePCB/pull/789))
- Use built-in markdown support when using Qt >=5.14
  ([#779](https://github.com/LibrePCB/LibrePCB/pull/779))
- CI: Work around broken macOS builds
  ([#797](https://github.com/LibrePCB/LibrePCB/pull/797))
- Fix missing holes in footprint previews
  ([#796](https://github.com/LibrePCB/LibrePCB/pull/796))
- Replace sexpresso library with own implementation
  ([#802](https://github.com/LibrePCB/LibrePCB/pull/802))
- Refactor deserialization & pass file format version
  ([#803](https://github.com/LibrePCB/LibrePCB/pull/803))
- SystemInfo: Add support for OpenBSD
  ([#804](https://github.com/LibrePCB/LibrePCB/pull/804))
- librepcb-cli: Log fatal messages to stderr
  ([#816](https://github.com/LibrePCB/LibrePCB/pull/816))
- Enforce locale en_US for all unit tests
  ([#821](https://github.com/LibrePCB/LibrePCB/pull/821))
- Improve error messages when project library update fails
  ([#824](https://github.com/LibrePCB/LibrePCB/pull/824))
- Don't provide "Hidden Grab Areas" layer when not reasonable
  ([#831](https://github.com/LibrePCB/LibrePCB/pull/831))
- Fix typos in comments
  ([#835](https://github.com/LibrePCB/LibrePCB/pull/835))
- Document license of icons
  ([#811](https://github.com/LibrePCB/LibrePCB/pull/811))
- Fix crash after adding a device to a board failed
  ([#855](https://github.com/LibrePCB/LibrePCB/pull/855))
- CI: Update to latest runners and Docker images
  ([#857](https://github.com/LibrePCB/LibrePCB/pull/857))
- Library editor: Provide "snap to grid" context menu item
  ([#867](https://github.com/LibrePCB/LibrePCB/pull/867))
- SQLiteDatabaseTest: Simplify flaky concurrency test case
  ([#874](https://github.com/LibrePCB/LibrePCB/pull/874))
- Allow opening locked workspace/project/library in some cases
  ([#871](https://github.com/LibrePCB/LibrePCB/pull/871))
- Component editor: Remove checkbox text "required/optional"
  ([#875](https://github.com/LibrePCB/LibrePCB/pull/875))
- Package editor: Stop rejecting but warn about overlapping pads
  ([#876](https://github.com/LibrePCB/LibrePCB/pull/876))
- Schematic editor: Snap wires to pins/junctions off the grid
  ([#877](https://github.com/LibrePCB/LibrePCB/pull/877))
- Board editor: Do not reject placing vias on top of other items
  ([#878](https://github.com/LibrePCB/LibrePCB/pull/878))
- Allow the CLANGFORMAT environmental variable to override clang-format.
  ([#880](https://github.com/LibrePCB/LibrePCB/pull/880))
- Refactor and improve gerber export for better compatibility
  ([#881](https://github.com/LibrePCB/LibrePCB/pull/881))
- Try to fix flaky functional test test_overview_tab.py
  ([#884](https://github.com/LibrePCB/LibrePCB/pull/884))
- Drop support for Qt < 5.5
  ([#885](https://github.com/LibrePCB/LibrePCB/pull/885))
- BOM Export: Show whether devices are in sync with schematic
  ([#888](https://github.com/LibrePCB/LibrePCB/pull/888))
- Library Editor: fix typo
  ([#889](https://github.com/LibrePCB/LibrePCB/pull/889))
- Board editor: Refactor and improve "Place Devices" dock
  ([#892](https://github.com/LibrePCB/LibrePCB/pull/892))
- Fix potential errors or crash when migrating workspace file format
  ([#896](https://github.com/LibrePCB/LibrePCB/pull/896))
- ERC messages dock: Hide empty root nodes (categories)
  ([#897](https://github.com/LibrePCB/LibrePCB/pull/897))
- Library editor: Ignore delete command if no items selected
  ([#899](https://github.com/LibrePCB/LibrePCB/pull/899))
- Board editor: Hide tabs if there are less than two boards
  ([#898](https://github.com/LibrePCB/LibrePCB/pull/898))
- xxx
  ([#xxx](https://github.com/LibrePCB/LibrePCB/pull/xxx))
- xxx
  ([#xxx](https://github.com/LibrePCB/LibrePCB/pull/xxx))
- xxx
  ([#xxx](https://github.com/LibrePCB/LibrePCB/pull/xxx))
- xxx
  ([#xxx](https://github.com/LibrePCB/LibrePCB/pull/xxx))
- xxx
  ([#xxx](https://github.com/LibrePCB/LibrePCB/pull/xxx))


### Changelog

#### Library Manager:


#### Library Editor:


#### Schematic Editor:


#### Board Editor:


#### ERC:


#### Miscellaneous:



### Download

The release can be downloaded for all major operating systems from our download
page:

#### https://librepcb.org/download/

Thanks to all contributors for making this awesome release possible!
