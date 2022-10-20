---
date: 2017-10-30
title: LibrePCB Has Switched to S-Expressions
author: U. Bruhin
---

One major goal of LibrePCB is to use human readable files to represent libraries,
projects and so on. This is important to let the user understand what the EDA
tool actually does when modifying a schematic or board. In addition, a good file
format is essential for version control systems to keep track of changes in
libraries and projects.

But LibrePCB doesn't just want to have *some* human readable file format. It
wants to use the **best possible** file format for our specific needs!

### XML and Similar Formats

Until now, LibrePCB used [XML](https://en.wikipedia.org/wiki/XML) as file format.
But unfortunately we were not very happy with it, because of several reasons:

- The XML specifications are **rather complex** (we used only a small subset of
  the available features). In [this blog post](https://blog.pragmatists.com/xml-be-cautious-69a981fdc56a)
  you can see that this complexity can even be dangerous!
- The syntax is **quite verbose** (it even contains redundant information,
  e.g. `<size>2.54</size>`).
- Available XML generators typically provide **only little control over the
  formatting** of the generated XML files. This leads to either very long files
  (many linebreaks) or very long lines (only few linebreaks). Both is bad for
  readability.

Other file formats (or their generators) have similar issues, so it seems that
the only reasonable solution is to use a custom file format, or at least a
custom generator.

### S-Expressions with Custom Generator

To avoid completely reinventing the wheel, we decided to use the
[S-Expressions](http://people.csail.mit.edu/rivest/Sexp.txt) file format.
[KiCad](http://kicad-pcb.org) uses this file format
[since version 4.0](http://kicad-pcb.org/post/release-4.0.0/), and it seems that
it's really well suited for the use case of an EDA tool.

S-Expressions are *very* simple to understand, but still powerful enough for
LibrePCB. And the syntax is not verbose, but still expressive.

With a custom S-Expressions generator, we are now able to control every little
bit of the format of our generated files. Here you can see the difference
between the old XML file format and the new S-Expressions file format:

{{< imglink "XML vs. S-Expressions" "xml_vs_s_expressions.png" >}}

*Note: Even if the S-Expressions file has 6 lines more than the XML file, it's
~16% smaller in size!*

### Links

- Issue #150: [LibrePCB file format discussion](https://github.com/LibrePCB/LibrePCB/issues/150)
- Issue #192: [Switch from XML to S-Expressions file format](https://github.com/LibrePCB/LibrePCB/issues/192)
- Pull request #193: [Switch from XML to S-Expressions file format](https://github.com/LibrePCB/LibrePCB/pull/193)
