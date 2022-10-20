# LibrePCB Website

This repository contains the sources official website of LibrePCB.

Hosted pages:

- HTML output of `master`: https://librepcb.org/
- HTML output of other branches: https://librepcb.org/_branches/

## Development

### With Docker On Linux

If you have Docker available on a Linux system, just run one of these
scripts:

```
./build.sh          # Build page into 'public' directory
./run_server.sh     # Build & host the page on http://localhost:1313/
```

### On Other Systems

The website is made with [Hugo](https://gohugo.io/). It does not need to be
installed, you can just download it as a portable binary. For instructions,
refer to their [documentation](https://gohugo.io/getting-started/installing/).

To build and review the website locally, just run one of the following
commands in the root directory of this repository:

```
hugo -F             # Build page into 'public' directory
hugo server -F      # Build & host the page on http://localhost:1313/
```
