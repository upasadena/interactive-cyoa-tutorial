# CONTRIBUTING

## How to contribute
You can contribute in two ways:

1. Directly via GitHub/Git, or
2. Commenting in some fashion (whether on the site itself, messaging me,
   commenting on a Reddit post, or anywhere else)

I will be going into how to contribute if you are new to the first message.

### Create a GitHub account
First, [create an account](https://github.com/signup).

### Fork the repository
Because you won't have write permissions by default, you will have to make
changes on a [fork][gh-fork].

To fork the repository, either
[open the repo](https://github.com/upasadena/interactive-cyoa-tutorial)
and press the **Fork** button in the top right, or go to
[this link](https://github.com/upasadena/interactive-cyoa-tutorial/fork) to
fork it automatically.

This will make a local copy of the project on your own account.

### Make your changes
From there, edit your local copy with the changes you want to make. Once that
is done, [open a pull request][gh-open-pr]. This will allow me to check your
changes, and implement them if they are helpful (stuff like spam or
mass-deletion without cause is not).

If there have been changes to the main repository in the meantime,
[sync the fork][gh-sync-fork].

## Licence
By submitting content to this repository, you hereby agree that your
contributions will be made under the [CC0 1.0][licence] licence (the Public
Domain). If you are not aware of what that entails, please see
[here][licence-details].

## Acknowledgements
Feel free to include yourself in
[the Authors list](./docs/appendix/about/index.md) in your pull request, and if
your pull request is merged you will be added.

## Technical Limits
Cloudflare Pages only supports files up to `26.2 MB` in size. If it's above and
it's a media file, please compress it. Source files shouldn't be above that
size to begin with.

## Checking
Check for dead links by using `mkdocs-linkcheck`.

Install that like so:

```sh
pip install mkdocs-linkcheck
```

Use it like so:

```sh
 mkdocs-linkcheck -r -v .
```

## Manual of Style
Please adhere to this style guide when editing the tutorial content.

### Language
This tutorial is written in [Oxford English spelling] (British English
with -ize and -yse endings).

#### Complexity
This tutorial was primarily written for beginners and those who are learning or
looking to learn, so it's important that you clearly explain concepts that may
seem simple to you, as if introducing someone new to this topic for the very
first time.

However, don't be too overzealous with this and start treating the readers as 5
year olds. We don't want to come off as arrogant.

#### Tone
Try to write in a formal, instructive tone in the tutorial content. Jokes and
informal speech aren't quite appropriate in the tutorial itself, but, of
course, may freely be in the comments section.

#### Pronouns
Prefer referring to the person reading the tutorial as "you".

When a gender is unknown or variable (such as, say, when gender is a chosen
option in a CYOA), use the 3rd person singular epicene pronouns **they/them**
rather than the masculine default **he/him** to refer to them.

Always prefer **they/them** to **he or she** (or vice versa) or **s(he)**,
as this excludes non-binary people or people who prefer to use other pronouns.

#### Punctuation
Use the [Oxford comma]:

* **DO** this: Tom, Dick<b>,</b> and Harry
* **DON'T** do this: Tom, Dick and Harry

#### Line length limit
In Markdown files, you'll quickly notice that words do not go past 79 lines.
This is to ensure clear reading on smaller monitors, a stylistic choice, and a
way to ensure that code is readable and not spread out.

There *are* exceptions of course, such as URLs (but only at the bottom of a
page), quotes (that cannot be broken up), and tables.

### Date and Time

#### Time Zone
The time zone used when writing dates and times should either be UTC, have the
time zone indicated in brackets (like this), or, when unknown, have (unknown
time zone) be put after it. 

#### Time Format
Prefer 24 hours time, like **05:30** and **16:48**, rather than **5:30 a.m.**
and **4:48 p.m.**

#### Date Format
When writing in long form, write like **20 July 1981**.

When writing numerically, write according to **YYYY-MM-DD**, like
**1981-07-20**. 

### Exceptions
Exceptions to this style guide can be made if it's someone or something being
quoted.

<!-- URLs -->
[Oxford English spelling]: https://en.wikipedia.org/wiki/Oxford_spelling
[licence]: ./LICENSE-CONTENT
[licence-details]: https://icctutorial.pages.dev/appendix/about/#content
[Oxford comma]: https://en.wikipedia.org/wiki/Serial_comma
[gh-fork]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
[gh-open-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[gh-sync-fork]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork

<!-- BUFFER -->