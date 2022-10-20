---
date: 2018-04-21
title: LibrePCB Meets FontoBene
author: U. Bruhin
---

Finally! LibrePCB has a fully functional stroke font which can be used on PCBs.
So now you can place designators or other text items on silkscreen (or other
layers) which of course are then exported into the generated Gerber files. The
new font file format [FontoBene](https://github.com/fontobene/fontobene/) was
developed especially for LibrePCB.

{{< imglink "Board Texts" "board_texts.png" >}}

### Why a stroke font instead of OTF/TTF?

It may sound strange to implement a primitive stroke font in 2018 when we
actually have much more powerful TrueType and OpenType fonts since many years.
But there are still reasons to stick with the good old stroke fonts.

One reason is that OpenType and TrueType fonts are very complex and thus require
high effort to integrate them into LibrePCB. For example the Gerber export is
not as trivial as you may expect because Gerber supports neither fonts nor
Bézier curves. On the other side, fonts consisting only of a bunch of lines are
extremely easy to export into Gerber files.

Beside their simplicity, stroke fonts even have a clear advantage compared to
OTF/TTF. Since you can set the stroke width to a value greater than or equal to
the minimum silkscreen line width specified by your PCB manufacturer, you can be
sure that the text items are printed properly and thus are perfect readable.

{{< imglink "Text Properties" "board_editor_text_properties.png" >}}

### Introducing FontoBene

Unfortunately we were not happy with the available stroke font formats because
of several reasons. [Hershey](https://en.wikipedia.org/wiki/Hershey_fonts) and
[NewStroke](https://vovanium.ru/sledy/newstroke/en) fonts have many edges
because they only consist of straight line segments. LFF from LibreCAD and CXF
from QCad look much smoother because they support circular arc segments, but
unfortunately there aren't any clear specifications available and the existing
fonts have non-permissive, partly even unknown licenses.

So we started to create
[clear specifications](https://github.com/fontobene/fontobene/blob/master/SPECIFICATION.md)
for a new stroke font file format, called [FontoBene](https://github.com/fontobene/fontobene/).
Because the project is completely independent from any software project (even
from LibrePCB), our hope is that it will also be used by other projects some time.

{{< img alt="FontoBene" src="fontobene.png" >}}

Currently LibrePCB uses the [NewStroke](https://vovanium.ru/sledy/newstroke/en)
font which we [converted to FontoBene](https://github.com/fontobene/fontobene-fonts/pull/4),
mainly because it is available under the CC0 Public Domain license. This means
that we currently don't yet take advantage of having support for circular arc
segments. The goal is to improve the font step by step.

### Self-Contained Projects

In contrast to other EDA tools, LibrePCB embeds the used font files into each
project. When creating a new project, The font files from the applications
installation directory are just copied into the projects directory.

The main advantage of this concept is that it makes projects more self-contained,
i.e. projects are not affected at all if we modify or even replace the font
files bundled with the application. So there is no risk to break existing
projects by modifying the applications font files.

Another advantage is that users are free to modify the font files of specific
projects. For example if our font is missing a glyph you would need, or if you're
unhappy with the look of some glyphs, you can just modify the font files in your
project to fix it. Other EDA tools do not allow users to modify their (built-in)
fonts.

### Links

- Pull request #246: [Implement stroke texts for footprints and boards](https://github.com/LibrePCB/LibrePCB/pull/246),
- Issue #165: [Decide how to implement fonts in footprints and boards](https://github.com/LibrePCB/LibrePCB/issues/165)
- FontoBene repository: https://github.com/fontobene/fontobene/
