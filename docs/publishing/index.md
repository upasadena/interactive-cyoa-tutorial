---
comments: true
icon: material/publish
---

# Publishing
Now that your CYOA has been build, we need to discuss how to publish it to the
world at large. 

As Interactive CYOAs made in the ICC do not need 

## Where should I publish?
There are many possible sites to host and formats to publish your Interactive
in, and we'll go over how to do so in this section.

There are quite a few sites that will publish your Interactive. In this
tutorial we'll only be discussing options that cost no money whatsoever.

Many people use either [Neocities] or [GitHub]. I recommend using GitHub, as it
allows you to make an unlimited amount of sites from the same account, with
each site having a larger free size limit.

If you wanted to make or have made an NSFW Interactive however, I recommend
using [Neocities]. [GitHub]'s [Sexually Obscene Content] policy means that
pornography (for the sake of pornography; educational and instructional use is
fine) cannot be hosted there. [Neocities], on the other hand, has no such
policy.

In the end, it's up to you to choose whichever site works best for your use
case.

### Table of Comparison

| Website                | Site Limit    | Size Limit                                                                                                      | Bandwidth Limit (per month)         | Bandwidth Speed                       | File limits                                                                                             | Other notes                                       |
| ---------------------- | ------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [Cloudflare Pages]     | Unlimited     | Depends on GitHub or GitLab                                                                                     | - Unlimited                         |                                       | Pages only supports files up to 26.2 MB in size                                                                  | - 1 build at a time<br>- **500 builds per month** |
| [GitHub Pages][GitHub] | Unlimited[^1] | - 5 GB per repository<br>- 1 GB per site<br>- 25 MB per file (web upload)<br>- 500 MB per file (git cli upload) | - 100 GB (soft limit)[^2]           | Fast transfer speeds                  | Any file type, but does not run server-side code such as PHP files, whereas paid Neocities supports PHP |                                                   |
| [Neocities]            | 1 per account | - 1 GB per account<br>- 50 GB per account                                                                       | - 200 GB (free)<br>- 3000 GB (paid) | Slower transfer speeds for free users | HTML files, CSS files, Javascript files, Markdown files, XML files, text files, fonts and images        |                                                   |
| [GitLab Pages][GitLab] | Unlimited[^1] | - 5 GB per repository                                                                                           | - 100 GB                            |                                       |                                                                                                         |                                                   |

## Why can I not view it locally?
See [here][local-cyoa-problem].

## Versioning
!!! note

    This is entirely optional, and mostly relevant to users who decide to host
    their interactive in a Git repository, such as on sites like GitHub and
    GitLab.

    However, you may find this useful if you're interested in learning how to
    standardize your versions.

It may be useful for users to have a consistent versioning scheme. I recommend
reading about [semantic versioning](https://semver.org/).

The basic summary is as follows:

!!! quote

    Given a version number MAJOR.MINOR.PATCH, increment the:

    * MAJOR version when you make incompatible changes
    * MINOR version when you add functionality in a backward compatible manner
    * PATCH version when you make backward compatible bug fixes

Whenever a major or minor version is incremented, the following versions must
be reset to 0: `1.2.3` → `1.3.0` → `1.3.1` → `2.0.0`, and so on.

### Initial development
!!! quote

    Major version zero (0.y.z) is for initial development. Anything MAY change
    at any time. The public API SHOULD NOT be considered stable.

Projects start at version `0.1.0` when being initially developed, and stay in
major version 0 until ready for public release.

Anything goes in the initial development phase, but you could:

* Increment the minor number when making breaking changes: `0.1.3` → `0.2.0` →
`0.3.0`, and so on.
* Increment the patch number when adding either backward-compatible
functionality or bug fixes: `0.3.0` → `0.3.1` → `0.3.2`, and so on.

### Post-release
When you are finally ready to release your Interactive CYOA to the public, the
version becomes `1.0.0`.

<!-- ??? quote

    Patch version Z (x.y.Z | x > 0) MUST be incremented if only backward
    compatible bug fixes are introduced. A bug fix is defined as an internal
    change that fixes incorrect behavior. -->

After adding only bug fixes and minor changes, increment the patch version:
`1.0.0` → `1.0.1` → `1.0.2`, and so on.

After adding new, backward-compatible changes, increment the minor version:
`1.0.2` → `1.1.0` → `1.2.0`, and so on.

After adding breaking, incompatible changes, increment the major version:
`1.2.0` → `2.0.0` → `3.0.0`, and so on.

!!! note

    Changes that would count as incompatible would be, for example:

    * Changing Row and Choice IDs, meaning any person looking to import
        their previous Backpack IDs would only be able to do so in `0.x.x` if
        they made it in Major version 0, or `1.x.x` if they made it in Major
        version 1.
    * Deleting rows or choices, such that users can't import their previous
    choices and expect the same result.
    * Changing requirements for existing choices.

Because of this predictable versioning, users can judge whether they would be
able to use previous builds, or if they should either make a new one, or
import their old one and try to pick up the pieces.

!!! note

    The version doesn't increment with each change you make, but it increments
    each time you release your next version.

## Changelog
On the note of versioning, it's a good idea to keep a "changelog": a list of
what's new and changed since the previous versions. You can have this changelog
be built into your Interactive or post it in the subreddit comments section,
for example.

It's important for your users to know what has changed since the last time they
played, so that they have a good idea of what to look forward to, and what may
make their previous build incompatible.

You can see the changelog of the ICC in the [Help and Instructions menu][HAI],
and you can see the changelog of this tutorial in the [About] page.

[About]: /appendix/about/#changelog

<!-- Footnotes -->
[^1]: You can create an unlimited amount of public or private repositories,
which can each act as their own site.
[^2]: You can go over this limit, but GitHub may decide to take down your site.

<!-- URLs -->
[Neocities]: https://neocities.org/
[GitHub]: https://github.com/
[GitLab]: https://about.gitlab.com/
[Cloudflare Pages]: https://pages.cloudflare.com/
[HAI]: /basics/#help-and-instructions
[Sexually Obscene Content]: https://docs.github.com/en/site-policy/acceptable-use-policies/github-sexually-obscene-content
[local-cyoa-problem]: /appendix/troubleshooting/#i-tried-to-open-indexhtml-on-my-computer-but-the-cyoa-wont-load

<!-- BUFFER -->