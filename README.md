# LibrePCB Website

This repository contains the sources official website of LibrePCB.

Hosted pages:

- HTML output of `master`: https://librepcb.org/
- HTML output of other branches: https://librepcb.org/_branches/

## Development

The website is made with [Hugo](https://gohugo.io/). It does not need to be
installed, you can just download it as a portable binary. For instructions,
refer to their [documentation](https://gohugo.io/getting-started/installing/).

Note that it's highly recommended to install the same version as used on our
CI (defined in [`.github/workflows/main.yml`](.github/workflows/main.yml)).

To build and review the website locally, just run the following command in
the root directory of this repository:

```
hugo server
```
