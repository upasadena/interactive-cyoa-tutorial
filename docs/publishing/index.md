---
comments: true
---

# Publishing
Now that your CYOA has been build, we need to discuss how to publish it to the
world at large. There are many possible sites to host and formats to publish
your Interactive in, and we'll go over how to do so in this section.

## Where to publish?
There are quite a few sites that will publish your Interactive. In this
tutorial we'll only be discussing options that cost no money whatsoever.

Many people use either [Neocities] or [GitHub]. I recommend using GitHub, as
it allows you to make an unlimited amount of sites from the same account, with
each site having a larger free size limit.

### Table of Comparison
| Website     | Site Limit    | Size Limit                                                                                                 | Bandwidth Limit (per month)         |
| ----------- | ------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [Neocities] | 1 per account | - 1 GB per account<br>- 50 GB per account                                                                  | - 200 GB (free)<br>- 3000 GB (paid) |
| [GitHub]    | Unlimited[^1] | - 5 GB per repository/1 GB per site<br>- 25 MB per file (web upload)<br>- 500 MB per file (git cli upload) | - 100 GB (soft limit)\*\*           |
| [GitLab]    | Unlimtied[^1] | - 5 GB per repository                                                                                      | - 100 GB                            |

[^1]: You can create an unlimited amount of public or private repositories, 

## What is Git?
Git is a **version control system** (VCS). It is a program that tracks changes


## Versioning
It may be useful to users to have a consistent versioning scheme. I recommend
reading about [semantic versioning](https://semver.org/).

The basic summary is as follows:

!!! quote

    Given a version number MAJOR.MINOR.PATCH, increment the:

    * MAJOR version when you make incompatible changes
    * MINOR version when you add functionality in a backward compatible manner
    * PATCH version when you make backward compatible bug fixes

For example:
* 0.1.0 is the very first version that you create
* Bug fixes and minor changes increment the PATCH number: 0.1.1, 0.1.2, and so
on and so forth
* Adding new choices, rows, et cetera would increment the MINOR number: 0.2.0,
0.3.0, and so on
* Making massive changes, such that different versions are incompatible would
warrant incrementing the MAJOR number: 1.0.0, 2.0.0, and so on
    * Changes that would count as incompatible would be, for example:
        * Changing Row and Choice IDs, meaning any person looking to import
        their previous Backpack IDs would only be able to do so in 0.\*.\* if
        they made it in Major version 0, or 1.\*.\* if they made it in Major
        version 1.
        * Deleting rows or choices, such that users can't import their previous
        choices and expect the same result.
        * Changing requirements for existing choices.
    * Because of this predictable behaviour, users can judge whether they would
    be able to use previous builds, or if they should either make a new one,
    or import their old one and see what

!!! note

    The version doesn't increment with each change you make, but it increments
    each time you release all your changes in one go.

## Changelogs
On the note of versioning, it's a good idea to keep a "changelog": a list of
what's new and changed since the previous versions.

You can have this changelog be built into your Interactive or post it in the
subreddit comments section, for example. It's important for your users to know
what has changed since the last time they played, so that they have a good idea
of what to look forward to, and what may make their previous build
incompatible.

<!-- URLs -->
[Neocities]: https://neocities.org/
[GitHub]: https://github.com/
[GitLab]: https://about.gitlab.com/