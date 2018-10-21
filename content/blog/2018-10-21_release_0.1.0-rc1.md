---
date: 2018-10-21
title: LibrePCB 0.1.0 RC1 Released
author: U. Bruhin
---

**Great news: Our first official release candidate is out! :-)**

If you didn't try LibrePCB already, now is the time to start using (or at least
testing) LibrePCB for your next projects – we would love to get your feedback!


### Project Status

Please keep in mind that this is our very first release candidate, so you may
encounter one or another bug or missing feature. Nevertheless, we think the
application is in a very usable state now – you can download and create
libraries, draw schematics, route multilayer PCBs and export Gerber files.
Unfortunately features like DRC, BOM export or buses are not implemented yet,
they will be provided in a future release.

If you encounter bugs, we would be happy if you report them to
[our issue tracker](https://github.com/LibrePCB/LibrePCB/issues). As it's only
a release *candidate*, there is some time to fix the most critical issues until
the first *stable* release.


### File Format Stability

Until now, we always communicated that the file format is not considered stable.
Any change in the file format could break older projects, so generally it was
not recommended to use LibrePCB productively.

With this first release candidate we consider the file format to be stable,
so any future release should be able to open libraries and projects created
with this release candidate. Only if there is an extremely critical issue with
the file format we may still do a breaking change before publishing the stable
0.1.0 release – but that's very unlikely :)

***ATTENTION:*** *The file format is only considered stable for official releases
– any intermediate version (e.g. from nightly builds) may not be upgradeable in
the next release! So if you already used our nightly builds (or other binaries
built from the `master` branch), you have to switch to official releases now.
Nightly builds must really not be used for productive work. See
[developers information](https://developers.librepcb.org/df/d30/doc_developers.html) and
[release workflow documentation](https://developers.librepcb.org/da/dbc/doc_release_workflow.html)
for details.*


### Libraries

Our official and ready-to-use libraries can easily be installed with the library
manager integrated in LibrePCB. But as these libraries currently only contain
very few elements, we would be very happy to get pull requests
[at the corresponding repositories](https://github.com/LibrePCB-Libraries) to
add much more elements!


### Download

The release candidate can be downloaded for all major operating systems at our
new download page:

#### https://librepcb.org/download/

Many thanks to all the contributors and sponsors making this release possible!
It was hard work of more than five years to bring out this first release. We
would really appreciate if you supported the development either with
contributions or donations (e.g. at [Patreon](https://www.patreon.com/librepcb)).
Every dollar helps to keep this huge project alive ;-)

And now: Happy testing! :-)
