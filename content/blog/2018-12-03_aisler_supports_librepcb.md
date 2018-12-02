---
date: 2018-12-03
title: AISLER Supports LibrePCB Projects
author: U. Bruhin
---

We are very happy to announce that
[AISLER now supports LibrePCB projects](https://aisler.net/partners/librepcb),
so you can upload and review LibrePCB projects directly on their website and
order PCBs and stencils just with a few clicks! :-)

[![LibrePCB Project at AISLER](/img/aisler_demo_brushless_controller.png)](/img/aisler_demo_brushless_controller.png)

### Why AISLER?

AISLER, based in Netherlands, is a smart prototyping service for electronics.
They provide PCBs, stencils and parts for electronic projects for an affordable
price, and everything is made in Germany.

I met Felix and Patrick, the founders of AISLER, at
[FOSDEM 2018](https://archive.fosdem.org/2018/). Patrick held the talk
[Proposal for an open and democratic Design Rule format](https://archive.fosdem.org/2018/schedule/event/cad_dr_format/)
and I gave an [Introduction to LibrePCB](https://archive.fosdem.org/2018/schedule/event/cad_librepcb/).
It turned out that we all have very similar opinions how development and
manufacturing of electronics could (and should) be improved. We all are trying
to bring EDA to a next level, for that reason they founded AISLER and I started
the LibrePCB project.

At FOSDEM Felix and Patrick offered me to integrate support for LibrePCB project
files into their website, to allow ordering PCBs by uploading LibrePCB projects.
And even more: For every order of an uploaded LibrePCB project they make a
donation to support the LibrePCB development!

### Implementation

To make this happen, I created the [LibrePCB CLI](https://docs.librepcb.org/#cli)
which allows to automate the processing of LibrePCB projects. AISLER now uses
that CLI to automatically generate Gerber files of an uploaded LibrePCB project.
These Gerber files are then used to create the preview of the PCB, and to
manufacture it in their fab.

![Analyzing LibrePCB Project](/img/aisler_analyzing_librepcb_project.png)

In order to adjust the fabrication output settings (e.g. filenames) according
their needs, they patch the board file `boards/<BOARDNAME>/board.lp` with their
own settings. So you don't have to make any fabrication output settings by
yourself, they will be overwritten anyway.

### Limitations

As you may know already, LibrePCB allows to have multiple boards in one project.
Currently it's not possible to select the specific board you want to order, so
you will get an error when uploading a project with multiple boards. We will try
to fix this limitation, but in the meantime you could manually adjust the
project's file `boards/boards.lp` to remove all boards except the one you want
to order ;)

In addition, currently you have to manually create a ZIP archive containing the
project directory, and upload that ZIP afterwards. I started to work on a
solution to make this much easier.

Also it's not yet possible for AISLER to export the BOM directly from the
uploaded project because BOM export is still missing in LibrePCB. But you can
still order parts at AISLER by uploading a CSV file with all parts.

### Try it!

Just ZIP and upload your LibrePCB project to [aisler.net](https://aisler.net/)
to see the beautiful preview and to order the PCB :) It would be awesome if you
order PCBs at AISLER as this way you directly support the development of
LibrePCB!

Many thanks to Felix and Patrick from AISLER to make this happen, and for
supporting LibrePCB and other open source projects!
