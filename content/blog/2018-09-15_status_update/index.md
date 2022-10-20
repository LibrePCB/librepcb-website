---
date: 2018-09-15
title: Status Update 2018-09-15
author: U. Bruhin
---

The last blog post is already a few months ago, and many things happened in the
meantime. Thus I would like to inform you about the current status of the
project, what happened in past and what the next tasks are.


### New Logo

Our logo was originally downloaded from a free icon portal. Although it was
legal (thanks to its permissive license), it's not a good idea to use a free
icon as a logo. Because we didn't have the copyright on it, it was not
guaranteed to be exclusively used by us (other projects could use the same icon
too).

As the [corresponding issue](https://github.com/LibrePCB/LibrePCB/issues/6) was
unresolved for more than three years (it was our 6th issue!), we decided to
start a [design contest at 99designs](http://99d.me/c/iab2) to get a new logo.
And here's the winning design:

{{< img alt="New Logo" src="new_logo.png" >}}

Sure, it's quite similar to the old logo, just nicer ;-) Probably that's because
I already liked the old logo, and maybe also a little bit because it was (too)
hard for me to go with a completely different logo than the one we had for
several years... Anyway, I hope you like the new logo as much as I do :)


### Latest Changes

It would be too much to explain all the changes from the last months, thus here
just a list of the most important pull requests merged:

- [Use Jinja-like attribute substitution syntax](https://github.com/LibrePCB/LibrePCB/pull/254)
- [Improve PCB fabrication output generator](https://github.com/LibrePCB/LibrePCB/pull/255)
- [Add ability to place NPTH drills on boards](https://github.com/LibrePCB/LibrePCB/pull/258)
- [Implement airwires (aka "rats nests")](https://github.com/LibrePCB/LibrePCB/pull/260)
- [Provide installer for nightly builds](https://github.com/LibrePCB/LibrePCB/pull/267)
- [Use Transifex for translations](https://github.com/LibrePCB/LibrePCB/pull/273)
- [Bundle fonts used in schematics together with LibrePCB](https://github.com/LibrePCB/LibrePCB/pull/282)
- [Add command-line tool "librepcb-cli"](https://github.com/LibrePCB/LibrePCB/pull/299)
- [Refactor net segments concept and board/schematic editors](https://github.com/LibrePCB/LibrePCB/pull/321)

The last one sounds innocent, but that's actually the change which (finally)
made the board editor really usable (it fixed many annoying bugs).


### Next Steps

With all the changes from above, our
[milestone 0.1](https://github.com/LibrePCB/LibrePCB/milestone/1) is nearly
complete. That means that we are now feature-complete for our first release!

So you can expect the first official stable release very soon :-)

The open tasks are now:

1. [Define a development and release workflow](https://github.com/LibrePCB/LibrePCB/pull/326)
2. [Prepare and test file format upgrade procedure](https://github.com/LibrePCB/LibrePCB/issues/185)
3. Review the whole file format and make the last changes if needed
4. Create and publish the first release!

So, stay tuned :)
