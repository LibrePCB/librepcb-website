---
date: 2021-11-02
title: LibrePCB 0.1.6 Released
author: U. Bruhin
---

After a whole year of development, we are very happy to finally announce
LibrePCB 0.1.6, which contains a lot of useful improvements!

### Highlights

#### LibrePCB Fab ([#927](https://github.com/LibrePCB/LibrePCB/pull/927))

One major goal of the LibrePCB project is to make creating PCBs easier and
faster by removing unnecessary complexity of the PCB design workflow. However,
orderding PCBs with Gerber/Excellon files is still a hurdle, especially for
users not familiar yet with the traditional PCB production data workflow.

To remove this hurdle, we integrated a new service, called
[LibrePCB Fab](https://fab.librepcb.org/about), into the schematic- and board
editors. It allows to order PCBs in a very simple, fast way -- without
worrying about Gerber or Excellon files at all!

{{< imglink "Order PCB" "board_editor_order_pcb.gif" >}}

Although this service is intended mainly for beginners, it is actually even
useful for experienced users since it saves quite some time when ordering PCBs,
at least if you don't need the higher flexibility of the traditional
Gerber/Excellon export.

&nbsp;

#### DXF Import ([#917](https://github.com/LibrePCB/LibrePCB/pull/917))

This release finally adds an import for DXF files, the industry standard for
2D mechanical drawings. Instead of drawing polygons like package dimensions
or board outlines manually, you can now simply import them from a DXF file
right into the package- symbol- or board editor. Circles can optionally be
converted to holes, which is useful to import mounting holes together with
the board outlines.

For example, creating an Arduino Shield is now much easier once you got its
outline as a DXF:

{{< imglink "DXF Import" "board_editor_dxf_import.gif" >}}

&nbsp;

#### Migration to CMake ([#798](https://github.com/LibrePCB/LibrePCB/pull/798))

Although this change is not directly relevant for LibrePCB users, it is still
noteworthy because of its impact for LibrePCB developers and package
maintainers.

Until LibrePCB 0.1.5, we used qmake as build system since it is the official
build system of Qt 5. But unfortunately, we had several issues with it,
especially regarding the integration and optional unbundling of third party
libraries.

Since CMake is the de facto standard for C++ projects, we have now migrated
LibrePCB to CMake as well. This allowed us to highly improve the way how
third party libraries can now be unbundled, which is very useful for package
maintainers. Note that even Qt 6 switched to CMake, one more good reason for
this step ;-)

Special thanks to [@dbrgn](https://github.com/dbrgn/) for the huge effort
spent for this migration!

---

### Changelog

#### Library Editor:

- Allow copying elements to other library
  ([#911](https://github.com/LibrePCB/LibrePCB/pull/911))
- Provide "Snap To Grid" context menu item
  ([#867](https://github.com/LibrePCB/LibrePCB/pull/867))
- Stop rejecting overlapping package pads, just warn about them
  ([#876](https://github.com/LibrePCB/LibrePCB/pull/876))
- Remove checkbox text "required/optional" in component signals editor
  ([#875](https://github.com/LibrePCB/LibrePCB/pull/875))
- Make GUI of remote libraries completely read-only
  ([#918](https://github.com/LibrePCB/LibrePCB/pull/918))
- Ignore delete command if no items selected
  ([#899](https://github.com/LibrePCB/LibrePCB/pull/899))

#### Schematic Editor:

- Snap wires to pins/junctions off the grid
  ([#877](https://github.com/LibrePCB/LibrePCB/pull/877))

#### Board Editor:

- Improve "Place Devices" dock and add new features to it
  ([#892](https://github.com/LibrePCB/LibrePCB/pull/892))
- Hide tabs if there are less than two boards
  ([#898](https://github.com/LibrePCB/LibrePCB/pull/898))
- Do not reject placing vias on top of other items
  ([#878](https://github.com/LibrePCB/LibrePCB/pull/878))
- Fix staying in the device placement tool
  ([#794](https://github.com/LibrePCB/LibrePCB/pull/794))
- Fix crash after adding a device to a board failed
  ([#855](https://github.com/LibrePCB/LibrePCB/pull/855))
- Fix some strange trace layer change behavior
  ([#926](https://github.com/LibrePCB/LibrePCB/pull/926))

#### ERC/DRC:

- Hide empty categories in ERC dock
  ([#897](https://github.com/LibrePCB/LibrePCB/pull/897))
- Support partial DRC checks & quick re-run from dock widget
  ([#907](https://github.com/LibrePCB/LibrePCB/pull/907))
- Fix loading maximum stopmask drill diameter from DRC rules
  ([#786](https://github.com/LibrePCB/LibrePCB/pull/786))

#### Import/Export:

- Add DXF import to package-, symbol- and board editors
  ([#917](https://github.com/LibrePCB/LibrePCB/pull/917))
- Improve Gerber files compatibility with manufacturers
  ([#881](https://github.com/LibrePCB/LibrePCB/pull/881))
- In BOM export, show whether devices are in sync with schematic
  ([#888](https://github.com/LibrePCB/LibrePCB/pull/888))
- Do not include `output/` directory in `*.lppz` export
  ([#929](https://github.com/LibrePCB/LibrePCB/pull/929))

#### CLI:

- Log fatal error messages to `stderr`
  ([#816](https://github.com/LibrePCB/LibrePCB/pull/816))

#### Miscellaneous:

- Add dialog to start ordering a PCB
  ([#927](https://github.com/LibrePCB/LibrePCB/pull/927))
- Allow overriding workspace path by environment variable
  ([#817](https://github.com/LibrePCB/LibrePCB/pull/817))
- Allow opening locked workspace/project/library in some cases
  ([#871](https://github.com/LibrePCB/LibrePCB/pull/871))
- Ask for new workspace path if workspace failed to open
  ([#906](https://github.com/LibrePCB/LibrePCB/pull/906))
- Only autosave project if there were changes
  ([#912](https://github.com/LibrePCB/LibrePCB/pull/912))
- Improve error messages when project library update fails
  ([#824](https://github.com/LibrePCB/LibrePCB/pull/824))
- Don't provide "Hidden Grab Areas" layer when not reasonable
  ([#831](https://github.com/LibrePCB/LibrePCB/pull/831))
- Set library-/board editor tab bars on MacOS to document mode
  ([#930](https://github.com/LibrePCB/LibrePCB/pull/930))
- Fix missing holes in footprint previews
  ([#796](https://github.com/LibrePCB/LibrePCB/pull/796))
- Fix wrong schematic editor colors when OpenGL is enabled
  ([#921](https://github.com/LibrePCB/LibrePCB/pull/921))

#### Packaging/Deployment:

- Add support for OpenBSD
  ([#804](https://github.com/LibrePCB/LibrePCB/pull/804))
- Drop support for Qt < 5.5
  ([#885](https://github.com/LibrePCB/LibrePCB/pull/885))
- Allow overriding default workspace path by environment variable
  ([#905](https://github.com/LibrePCB/LibrePCB/pull/905))
- Display TLS library version in about dialog
  ([#923](https://github.com/LibrePCB/LibrePCB/pull/923))
- Update official binary releases to Qt 5.15.2 and OpenSSL 1.1.1
  ([#925](https://github.com/LibrePCB/LibrePCB/pull/925))

#### Internal:

- Migrate from qmake to CMake
  ([#798](https://github.com/LibrePCB/LibrePCB/pull/798))
- Use built-in markdown support when using Qt >=5.14
  ([#779](https://github.com/LibrePCB/LibrePCB/pull/779))
- Replace sexpresso library with own implementation
  ([#802](https://github.com/LibrePCB/LibrePCB/pull/802))

---

### Download

The release can be downloaded for all major operating systems from our download
page:

#### https://librepcb.org/download/

Thanks to all contributors for making this awesome release possible!
