[![ci]][ci_link]

# Interactive CYOA Tutorial
A complete and comprehensive guide to using the Interactive CYOA Creator by
MeanDelay.

View it live at one of these links:
* https://icctutorial.pages.dev/
* https://upasadena.github.io/interactive-cyoa-tutorial/

## TODO
- [ ] Finish the base tutorial
    - [x] Finish the Introduction section
    - [x] Finish the Basics section
    - [ ] Finish the Mechanics section
        - [x] Rows
        - [x] Objects / Choices
        - [x] IDs & Requirements
        - [x] Points & Scores
        - [ ] Images
        - [ ] Defaults
        - [ ] Addons
        - [ ] Copying
        - [ ] Words
        - [ ] Buttons & Variables
        - [ ] Groups
        - [ ] Backpack & Choice Import
    - [ ] Finish the Styling section
    - [ ] Finish the Publishing section
    - [ ] Finish the Reference section
- [ ] Add a section detailing how to get pages.dev, netlify.app, etc.
- [ ] Add a End-of-tutorial Project where there's a step by step remake of a
CYOA.
- [ ] Add JavaScript to show when, from now, a release happened
- [ ] Delete unneeded JavaScript
- [ ] Find a way to count words and characters
- [ ] Delete ideologically-driven information, such as git. The people do not
need nor want to know that.
- [ ] After the ICCT is written, go through the main tutorial and add
everything that is possible into the Mechanics

## Contributing
To contribute to this, simply fork this repository, make your changes, and
open a pull request.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for specifics.

## Building locally
To build this tutorial locally, first install `mkdocs-material` (visit
[here](https://squidfunk.github.io/mkdocs-material/getting-started/) to learn
more about installing it):

```sh
pip install mkdocs-material
```

Then run:
* `mkdocs serve` to serve it (with changes being automatically applied), or
* `mkdocs build` to build a static version which can be run without serving
each time and without mkdocs.

<!-- URLs -->
[ci]: https://github.com/upasadena/interactive-cyoa-tutorial/actions/workflows/ci.yml/badge.svg
[ci_link]: https://github.com/upasadena/interactive-cyoa-tutorial/actions/workflows/ci.yml