[![ci]][ci_link]

# Interactive CYOA Tutorial
A complete and comprehensive guide to using the Interactive CYOA Creator by
MeanDelay.

View it live at one of these links:
* https://icctutorial.pages.dev/ – The recommended URL
* https://upasadena.github.io/interactive-cyoa-tutorial/ – Not recommended. The
  reason is threefold:
    1. [Root-relative links][rrl] are broken, as they were made with the
       pages.dev URL (and any other top-level domain) in mind, and…
    2. It's a much longer name (cf.
    https://icctutorial.pages.dev/extending-your-cyoa/ VS
    https://upasadena.github.io/interactive-cyoa-tutorial/extending-your-cyoa/)
    3. It's harder to memorize, because not only do you have to memorize
       `interactive-cyoa-creator`, but you have to memorize my username as
       well.

## TODO
See [here](./docs/appendix/about.md#todo).

## Contributing
To contribute to this, simply fork this repository, make your changes, and
open a pull request.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for specifics.

## Building locally
To build this tutorial locally, first install `mkdocs-material` (visit
[here](https://squidfunk.github.io/mkdocs-material/getting-started/) to learn
more about installing it):

### Virtual environment
You may need to set up a virtual environment if you're deploying on your own
machine due to conflicts of dependencies:

```sh
python -m venv venv
./venv/Scripts/activate
```

### Prerequisites
#### Automatic installation
Leverage `requirements.txt`:

```sh
pip install -r ./requirements.txt
```

This may take a while for the first time.

#### Manual installation
Install the latest mkdocs-material beta release:

```sh
git clone --depth 1 -b 9.2.0b1 https://github.com/squidfunk/mkdocs-material/
pip install --force -e ./mkdocs-material/
```

Install the plugins:

```sh
pip install mkdocs-minify-plugin mkdocs-git-authors-plugin mkdocs-git-revision-date-localized-plugin
```

### Building from git clone
If you cloned the repository, you're all set!

Run:
* `mkdocs serve` to serve it (with changes being automatically applied), or
* `mkdocs build` to build a static version which can be run without serving
each time and without mkdocs.

### Building from source code
If you didn't use `git clone`, and instead downloaded the source from the
Releases page, then you'll need to initiate a Git repository:

```sh
# change for whatever version you downloaded
cd interactive-cyoa-tutorial-0.1.0/
git init; git add .; git commit -m "Initial commit"
mkdocs serve # serve
mkdocs build # or build
```

### Deactivating the virtual environment

```sh
deactivate
```

<!-- URLs -->
[ci]: https://github.com/upasadena/interactive-cyoa-tutorial/actions/workflows/ci.yml/badge.svg
[ci_link]: https://github.com/upasadena/interactive-cyoa-tutorial/actions/workflows/ci.yml
[rrl]: https://mor10.com/html-basics-hyperlink-syntax-absolute-relative-and-root-relative/

<!-- BUFFER -->