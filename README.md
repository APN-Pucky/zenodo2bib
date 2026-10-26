# zenodo2bib

[![PyPI - Version](https://img.shields.io/pypi/v/zenodo2bib.svg)](https://pypi.org/project/zenodo2bib)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zenodo2bib.svg)](https://pypi.org/project/zenodo2bib)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)
- [Examples](#examples)

## Installation

```console
pip install zenodo2bib
```

## License

`zenodo2bib` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Examples

Accepts a Zenodo record ID, DOI, or URL and prints that record's BibTeX entry:

```console
$ zenodo2bib 23666615
@software{poinsinet_de_sivry_houle_2026_23666615,
  author       = {Poinsinet de Sivry-Houle, Martin},
  title        = {RosettaX: reproducible flow-cytometry calibration
                   workflows
                  },
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v0.10.8},
  doi          = {10.5281/zenodo.23666615},
  url          = {https://doi.org/10.5281/zenodo.23666615},
}
```

```console
$ zenodo2bib "https://zenodo.org/records/23666615"
```

```console
$ zenodo2bib "10.5281/zenodo.23666615"
```

Anything else is treated as a free-text search against the Zenodo search API, printing a BibTeX entry for each matching record:

```console
$ zenodo2bib pylhe
@software{lukas_heinrich_2026_23082467,
  author       = {Lukas Heinrich and
                  Matthew Feickert and
                  Eduardo Rodrigues and
                  Alexander Puck Neuwirth},
  title        = {scikit-hep/pylhe: v2.1.0},
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v2.1.0},
  doi          = {10.5281/zenodo.23082467},
  url          = {https://doi.org/10.5281/zenodo.23082467},
}
```
