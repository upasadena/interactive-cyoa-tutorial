---
comments: true
icon: material/file-question-outline
---

# About
Thank you for viewing this tutorial! This page isn't a part of the tutorial,
but rather a general information page about the tutorial itself.

This website is available in these locations:

* [https://icctutorial.pages.dev][icct] – Recommended,
  shorter and easier to remember
* [https://upasadena.github.io/interactive-cyoa-tutorial/][icct-alt] – Backup,
  root-relative links don't work

[icct-alt]: https://upasadena.github.io/interactive-cyoa-tutorial/

## Authors
Authors are people who have directly contributed to the text, via the Git
repository for this site.

<!-- 
Tip: You can use the syntax @GitHubUsername and MkDocs will automatically link
to you.
-->

* @upasadena, the original creator

## Contributors
Contributors are those who are credited and acknowledged as having contributed
to this tutorial from the time of its official release.

* None as of yet

## Roadmap
### TODO
- [ ] Finish the base tutorial
    - [x] Finish the Introduction section
    - [x] Finish the Basics section
    - [x] Finish the Mechanics section
        - [x] Rows
        - [x] Objects / Choices
        - [x] Addons
        - [x] Backpack & Choice Import
        - [x] IDs & Requirements
        - [x] Points & Scores
        - [x] Images
        - [x] Defaults
        - [x] Words
        - [x] Buttons (& Variables)
        - [x] Groups
    - [ ] Finish the Styling section
        - [ ] Design – Basically like, design theory
        - [x] Style Templates
        - [ ] Colours – How you should choose colour, where to put it
        - [x] Backgrounds
            - [ ] Link to static background in Reference, or vice versa
        - [ ] Text
        - [ ] Rows / Row Design (to not confuse it with Mechanics/Rows)
            - [ ] Row Images
        - [ ] Choices / Choice Design (see above)
            - [ ] Choice Images
        - [ ] Filters
        - [ ] Point Bar
        - [ ] Multi-Choice
        - [ ] The Backpack
        - [ ] Private Styling
    - [x] Finish the Creating Your CYOA section
        - [ ] Section detailing actual mechanical design choices, such as
        whether to include perks, drawbacks, balancing, etc. Essentially the
        Mechanics equivalent to the Styling section's Design page.
    - [x] Finish the Extending Your CYOA section
    - [x] Finish the Publishing section
        - [x] Publishing (page)
        - [x] Static
        - [x] Neocities
        - [x] GitHub
    - [ ] Finish the Reference section
    - [ ] Finish the Troubleshooting section
    - [x] Finish the Resources section – Will this and the above two ever truly
      be finished?
- [ ] Add a End-of-tutorial Project where there's a step by step remake of a
CYOA.
- [ ] After the ICCT is written, go through the main tutorial and add
everything that is possible into the Mechanics
    * e.g., in the Backgrounds page, make a section on making static
      backgrounds, and link to the Reference
- [ ] Chill with the quotes, and instead rewrite the quotes into information in
  my own words.
- [ ] Add my own custom Viewer js file, this time adding:
    - [ ] `alt` attribute for `<img>`s
    - [ ] `referrerpolicy` attribute for `<a>` links
- [ ] Change template example images in the **Style Templates** section to
  include buttons that are being pressed, images, and other elements
- [ ] Specify that content indicated by a `!!! quote` admonition and in code
  blocks (when explicitly said or noted as quoted) as not licensed under the
  content licence.
- [ ] Finish the **Publishing** section and then upload it to Reddit
    - [x] Finish the **Publishing** section
    - [ ] Upload it to Reddit
        - [ ] I may have to upload it to r/NSFWCYOA instead of
          r/makeyourchoice, considering the fact that I both include some NSFW
          images and also link to a lot of NSFW material in the Resources
          section
- [ ] Add the version of the Tutorial in the header or footer somewhere
- [ ] In the **Design** section, speak imperatively. Say **Do this** and
  **Don't do that** instead of just quoting people and pointing toward them. I
  need to put all the data all in one spot.
- [ ] Add Cheat Engine example to **Extending Your CYOA**
- [ ] End all list items in **Resources** with full stops or without (for
  consistency)
- [ ] Add speed comparison between Neocities and GitHub
- [ ] Under *Styling/Backgrounds* add examples of where the image upload
  buttons are if you didn't stay zoomed out, and instead zoomed back in to show
  the image upload bugged choices
- [ ] Make a script like [here][script-dc] which receives a URL or
  `project.json`, goes through all links to images, fetches them, then converts
  them into Base64 encoded images and puts them locally. Make it open-source
  and MIT.
- [x] Add Lt Ourovmov's Viewer to the `static/` folder with the other Viewer
  files
    - [ ] Use that Viewer with my GitHub template
    - [ ] Merge it with the other modded Viewer I have to create the Ultimate®
      Viewer
- [ ] Make a macro to list all files in a directory, and use it for `static/`
- [ ] Add red outlines around the buttons in the **Basics** section, as that of
  all places should be clearer

### Completed

- [x] Compress all the gifs to limit bandwidth, but not enough such that the
  gifs lose legibility. Use `gifsicle` in a python script.
- [x] Find a way to count words and characters
- [x] Make a chapter detailing how to actually *create* ICYOAs
    - [x] Section on OCR, including my command line tool, caveats, etc
    - [x] Section on finding the text, seeing if there's a Google Doc –
      Mentioning possibly asking the authors for a text version
    - [x] Section on handwriting it
    - [x] Advice on asking the author if they have a Google Doc of it, so that
      you can more easily copy it?
- [x] Consider changing the content licence to CC0 (Public Domain).
- [x] Add tip block when talking about the Viewer, mentioning that projects
  automatically start at the `index.html`, meaning they don't need to include
  that in the title (and it looks nicer)
- [x] Delete unneeded JavaScript

### Scrapped

- [ ] Add JavaScript to show when, from now, a release happened
- [ ] Standardize "after"/"result"/"with" and "before"/"without" etc
  tabbed titles
- [ ] Delete ideologically-driven information, such as git. The people most
likely do not need nor want to know that.
- [ ] Add a section detailing how to get pages.dev, netlify.app, etc.
- [ ] Add surge.sh hosting option (unlimited bandwidth)

## Changelog

<!--
Changelog template:
-->

<!-- 
Reading Time calculation:
seconds = num_words / 265 * 60 + img_weight * num_images

WPM is 265 by default
-->

<!--
### v0.0.0 (WIP)
_Released on DATE at TIME UTC_

{{ words_format(word_count=00000, images=000) }}

* 

[Download the source code][dl-VERSION]{ .md-button }
-->

### v0.18.0 (WIP)
<!-- _Released on DATE at TIME UTC_ -->

<!-- {{ words_format(word_count=00000, images=000) }} -->

* Added links to `static/`
* Switch to using the Git commit as the date shown on releases now, rather than
  the GitHub release
* Posted this to Reddit! (TODO: link)
* Updated Resources
* Made stats publicly viewable
* Adjusted word count stat from previous release (in accordance with the rule
  up top)
* Updated mkdocs-material from version 9.2.0b1 to 9.5, moving from beta
  channels to the official channels
* Also updated the other packages to their latest versions
* Added an `install_requirements.sh` script to make it easier for me to update to
  newer versions of packages
* Expanded on the **CONTRIBUTING.md** document in order to facilitate new GitHub
  users
* Made minor changes to Mechanics/Images
* Fixed links
* Minor change to Points and Scores
* Added **Exported Local** images to the Images section
* Specified year in the Introduction
* Corrected word in the Introduction
* Added to TODO
* Fixed cache not working (inefficient build times before now, damn :/)
    * Improved build times by ~0-30s, which is about a 33% improvement
* Minor fix to Words
* Added Dynamic Background stuff in the reference
* Updated Modded Viewer to allow `#!html <div>`s now
* Add to the Reference
* Got rid of the manual author insertion, as the new mkdocs-material seems to
  do that for you
* Tidied up the progress indicator section by removing the bytes example and
  adding a tip for clarification
* Added more to the Git CLI tutorial for clarification on where to run the
  commands
* Added Tools section to the Resources page
* Added AvifCyoaCompressor and InteractiveCyoaVerifier to Tools
* Added Lt Ouroumov's modded creator to tools
* Added clarification of the order of Word IDs and Point IDs when displaying
  points
* Added an alternative indicator to the extending your cyoa section
* Added mention of Lt Ouroumov's viewer in the Viewer download section
* Added ICC+ to resources, and copied Lt Ouromov's creator and the ICC+ to the
  very front page.
* Added mirrors to the two additional viewers in the static folder.
* Removed release date-time and word count for the latest version of the ICCT.
* Removed Javascript from the Reference section as there is nothing there for
  now
* Cleaned up the Reference so that only the easiest methods for doing something
  are included
* Linked to a hex code colour picker in the Reference
* Added PNG-MAN's tutorial for playing CYOAs offline to the tutorial
* Removed reference to launchcode01dl's modded CYOAs, as they have taken it
  down.
* Added information about pressing ++s++ to search in the Introduction
* Added IntCyoaAutosaver to the tools list and added synergy with RegExp
  Download Organizer
* Added mobile browser errors to the Troubleshooting page, and referenced it in
  the Extending Your CYOA page
* Explicit mention of how to import CSS through files
* Updated code for the mobile fix
* Added links to more OCR programs
* Minor fixes

[Download the source code][dl-VERSION]{ .md-button }

### v0.17.0
_Released on 2023-08-08 at 04:03:17 UTC_

{{ words_format(word_count=29814, images=358) }}

* Started work on and finished the **Backgrounds** section
* Added and modified **GitHub** with fixes, as well as adding a reset section
* Changed **Github** to **GitHub** in the navigation
* Small fix in `README.md`
* Spelling correction in **Buttons and Variables**
* Fixed **Buttons and Variables** talking about **Images** at the Reference
  message at the end
* Compressed 7 more gifs
* Updated `static` directory index
* Grammar and spelling checked
* Added DnD style skill check in Reference
* Added some more stuff to the Reference
* Added `.vscode/extensions.json` in order to recommend extensions that are
  both:
    1. Compatible with `.vscode/settings.json`, and
    2. Help with writing and contributing to this project
        * Spell-checker added
* Preemptively added `docs/styling/backgrounds.md` because I have some ideas
* Added some more TODOs to the Reference
* Added `reddit_post.md`, the Markdown for the (future) Reddit post in the
  `/static` folder
* Added a **Download tutorial for offline use** button so that people didn't
  have to visit the website
* Added icons to the buttons in the `index.md` page
* Changed icons for dark and light mode toggles in order to be more clear about
  what the buttons do
* Added some scripts to help with virtual environments on Linux
* Updated **Resources** page
* Moved the **About/Licence** section down to the very bottom
* Fixed a relative link in the **Introduction**
* Deleted old `_copyright.html` partial that wasn't in use
* Removed "made by" section for `static_background.css`
* Add Moirai Interactive to CYOA Creators list
* Added link to archived Miraheze ICCT
* Added `(WIP)` markers to chapters in preparation of Reddit release
* Added `image_downloader_fix.js` to the Static folder
* Swapped position of "Get a list of Point Types" and "Change how many points I
  have" in the Reference
* Add `#!html <strong>` and `#!html <em>` tags to the HTML section of the
  Reference, though it is not explicitly stated that they should be preferred
  due to semantics. Also there is no strong and emphasized example.
* Add links to the Modded Viewer from the HTML and CSS sections of the
  Reference

[Download the source code][dl-0.17.0]{ .md-button }

### v0.16.0
_Released on 2023-07-21 at 07:27:04 UTC_

{{ words_format(word_count=26436, images=329) }}

* Started on and finished the **GitHub** page
* Actually swapped **Neocities** and **GitHub** in the nav this time
* Expanded on the Publishing section of the TODO section
* Removed casual speech from Words and fixed a minor typo
* Added a modded css Viewer file that changes the Point Bar icon colours
* Beautified the fixed app.js and chunks-vendor.css files because it makes them
  easier to work with and only adds a negligible increase in space
* Got rid of unneeded `dev-requirements.txt`, `get_reading_time.py`, and
  `enter_venv.ps1` files
* Added `docs/images/bin` folder for other images I want to ignore, and moved
  the favicon in there
* Moved workflow to Linux
* Decided that version release times will be based on Git logs of the last
  commit from now on
* Other minor fixes

[Download the source code][dl-0.16.0]{ .md-button }

### v0.15.0
_Released on 2023-07-20 at 08:10:12 UTC_

{{ words_format(word_count=23390, images=284) }}

* Started work on and finished the **Neocities** page
* Finished **Static** page as it was incomplete
* Added to **Design** page
* Changed the licence of all content to the [CC0] Public Domain licence
* Moved Licence section in the About page up above TODO and Changelog
* Put TODO under the Roadmap section, and separated TODO into TODO and
  Completed to better get rid of unneeded text
* Added a video tutorial to **Backpack and Choice Import** which helps the
  **Static** publishing page
* Added a lot to the Reference
* Updated lots of other sections
* Added Choice Copying that undoubtedly would have been in the lost **Copying**
  section
* Changed README.md to talk about why [https://icctutorial.pages.dev][icct] is
  the preferable URL
* Added abbreviations for Cf. and cf.
* Added to the Reference
* Added a `requirements.txt` file so that it's easier to self-host this website
* Upgraded `mkdocs-material` from 9.2.0b0 to 9.2.0b1
* Changed GitHub actions workflow to use requirements.txt
* Compressed gifs once more
* Deleted `mkdocs-material` folder that I hosted locally, now that
  requirements.txt would make it defunct
* Deleted `venvold/`, another local folder
* Moved all of the top-level scripts into the `scripts/` directory for
  organizational purposes
* Made a new cross-platform word count python script
* Realized that the old word count script was counting **EVERYTHING** in the
  root directory, including docs belonging to venv and mkdocs-material.
  Rerunning it only within `docs/` changed the total from `121,255` (0.14.0) to
  `21,359` (whilst developing 0.15.0). It appears I had vastly overestimated my
  word count.
* Finally deleted the `old/` directory
* Spelling corrections
* Moved the **Authors** field from below the comments section to above it, in
  line with the "Last update" and "Created" metadata.
* Fixed some dead links
* Updated Words fields on the About page with the more accurate amount of
  plaintext words typed (as opposed to all words counting the Markdown)
* Added word count for v0.12.0 and below
* Updated Introduction#Sharing, introducing a new sharing tip
* Added an Archive to the Resources section
* Reordered Troubleshooting text
* Added `mkdocs-macros-plugin` to the codebase, allowing for arbitrary
  insertion of macros for easier coding
* Made a `youtube_embed()` macro to make it easier to embed YouTube videos
* Change `requirements.txt` such that it now allows semantic versioning
  upgrades. Not sure if all packages use semantic versioning though
* Officially implemented _Reading Time_ under Releases, using macros
* Swapped **Neocities** and **GitHub** positions because of two reasons:
    1. Complex topics should come last, and
    2. More people would probably be comfortable using Neocities
* Modified `count_words.py` since I no longer need it to ask for input

[icct]: https://icctutorial.pages.dev

[Download the source code][dl-0.15.0]{ .md-button }

---

Content released under here is licensed under [CC BY-SA 4.0].

---

### v0.14.0
_Released on 2023-07-17 at 05:13:53 UTC_

<!-- _Words: 121,255_ -->
_Words: 24,023_

* Added and finished the **Style Templates** section
* Added and finished the **Creating Your CYOA** section
* Added a note to Words
* Added the ICC comments section to the Resources section
* Moved **Extending Your CYOA** section above **Publishing**, as publishing
  should be the last thing you do
* Added PS script to automatically enter into the virtual environment

[Download the source code][dl-0.14.0]{ .md-button }

### v0.13.2
_Released on 2023-07-13 at 12:41:52 UTC_

<!-- _Words: 119,262_ -->
_Words: 22,496_

* Fixed Words stat on About page
* Fixed minor Mechanics TOC issue
* Rewritten a small portion of Buttons & Variables
* Fixed Backpack and Choice Import reference sentence referring to "Defaults"
  instead

[Download the source code][dl-0.13.2]{ .md-button }

### v0.13.1
_Released on 2023-07-13 at 12:09:14 UTC_

<!-- _Words: 119,215_ -->
_Words: 22,456_
<!-- Somehow lost words ^^^ ? -->

* Added more Resources
* Changed links in the Introduction to be less intrusive
* Added more limitations in the Introduction
* Minor CONTRIBUTING fix
* Fixed **Mechanics** section not having removed TODO sections
* Miscellaneous changes

[Download the source code][dl-0.13.1]{ .md-button }

### v0.13.0
_Released on 2023-07-13 at 11:40:35 UTC_

<!-- _Words: 119,092_ -->
_Words: 22,475_

* **FINISHED MECHANICS SECTION!!!**
* Finished **Groups** page's first revision
* Compressed gifs using script again
* Moved **Backpack and Choice Import** page from the bottom of **Mechanics** to
  underneath **Addons**, as it's a more elementary concept
* Updated README.md to include instructions on building from a Release
* Added Mermaid graphs in **IDs and Requirements**
* Added more Resources
* Added a project-wide word count script for Linux (not my code)
* Miscellaneous additions

[Download the source code][dl-0.13.0]{ .md-button }

### v0.12.0
_Released on 2023-07-13 at 05:17:40 UTC_

_Words: 21,918_

* Finished first revision of the **Backpack and Choices Import** page
* Changed **Buttons** to **Buttons and Variables**
* Modified **Buttons** a bit
* Re-edited the **Publishing** page, though it's still not yet complete
* Miscellaneous stuff

[Download the source code][dl-0.12.0]{ .md-button }

### v0.11.0
_Released on 2023-07-13 at 03:57:16 UTC_

_Words: 21,304_

* Added **Buttons** page's first revision
* Added more examples (or TODO examples) to the Reference. I expect examples
  or pictures for every single entry there by `v1.0.0`
* Moved Allowed HTML tags, Allowed Attributes, and Allowed Styles into the
  Reference section
* Added **Icons** to each page title in the Navigation Bar
* Found a new tutorial that has a lot of stuff to add
* Compressed all gifs, saving 110 MB / 28.8% of space (script in repo)
* Added `UTC` to the last two releases' dates
* Changed Purpose to Background and expanded on it in the Introduction
* Using privacy-friendly stats now
* Split Background into Rationale and Background in the About menu
* Added `at` to the previous release date
* Deleted old `_main.html` template that was useless
* Added some abbreviations
* Added more to the Styling
* Created a **Colours** page, that is of yet still unfinished (will finish
  after Styling section is finished)
* Fixed miscellaneous stat bug (I think)
* Miscellaneous additions and fixes

[Download the source code][dl-0.11.0]{ .md-button }

### v0.10.0
_Released on 2023-07-10 at 11:59:17 UTC_

_Words: 18,641_

* Finished the first revision of the **Extending Your CYOA** section
* Added some abbreviations

[Download the source code][dl-0.10.0]{ .md-button }

### v0.9.0
_Released on 2023-07-10 at 07:09:35 UTC_

_Words: 17,248_

* Added and finished **Words** section
* Ticked Addons of the TODO because I'm dumb
* Added Addons as completed on the Mechanics index
* Fixed my release dates not following the YYYY-MM-DD format
* Deleted **Copying** section, will be adding to Rows
* Added missing functionality to Rows section, adding links to main pages
* Realized I had skipped some Object functions purely because I was going to
  address them in their other sections. So I made a title and linked them to
  where they are actually hosted.
* Moved a whole section of the Words tutorial to the Reference
* Added Web Programming resources in Resources
* Added a bit to the Reference
* Finished Static Background section
* Fixed some dead links (have to get a tool to check for that)

[Download the source code][dl-0.9.0]{ .md-button }

### v0.8.0
_Released on 2023-07-10 at 00:47:05 UTC_

_Words: 15,387_

* Finished the **Addons** section
* Fixed the "Last update" not working as intended
* Fixed missing Viewer file
* Reordered Mechanics section in TODO
* Added `authors` section down the bottom, which will show the contributor
  percentage if there is more than one author.
* Changed Reference text to make more sense
* Miscellaneous fixes

[Download the source code][dl-0.8.0]{ .md-button }

### v0.7.0
_Released on 2023-07-09 at 11:40:35 UTC_

_Words: 15,343_

* Finished the first revision of the **Defaults** section
* Miscellaneous fixes

[Download the source code][dl-0.7.0]{ .md-button }

### v0.6.1
_Released on 2023-07-09 at 11:21:29 UTC_

_Words: 15,064_

* Finished first revision of the **Image** section
* Added the Troubleshooting section on the official TODO, made a start on it
* Moved **Reference**, **About**, and **Troubleshooting** pages into the
  **Appendix**
* Added `(TODO)` and `(WIP)` prefixes to the Reference
* Added Sharing section back to the Introduction
* Moved the TODO from the README.md to the About page
* Added **Resources** section.
* Enabled Task Lists for the TODO section
* Added the **Design** section under **Styling**
* Fixed a few bad links
* Minor typograpgical fixes

What happened to `v0.6.0`? I forgot to `push` my changes before making a
release :P

[Download the source code][dl-0.6.1]{ .md-button }

### v0.5.1
_Released on 2023-07-07 at 09:11:38 UTC_

_Words: 11,664_

* Finally completed the **IDs and Requirements** section 
* Enabled comments for the **Points and Scores** section
* Updated Mechanics's Table of Contents
* Added a script `loop_serve.ps1` because mkdocs kept crashing when I moved
files while it was building the site

[Download the source code][dl-0.5.1]{ .md-button }

### v0.5.0
_Released on 2023-07-07 at 07:55:19 UTC_

_Words: 11,264_

* Added **Points & Scores** section, finished first revision
* Changed Objects section title from "Objects" to "Objects / Choices"
* Realized that I had not, in fact, finished **IDs and Requirements**
    * Updated headings but have not finished filling it out
* Added code block copying functionality

[Download the source code][dl-0.5.0]{ .md-button }

### v0.4.0
_Released on 2023-07-07 at 05:12:04 UTC_

_Words: 10,165_

* Finished **IDs and Requirements** section
* Fixed Mechanics' TOC
* Added previous version's information here
* Created Basics section and separated the Introduction/Preface from it
* Added links to the Reference section at the bottom of each section
* Adjusted CONTRIBUTING.md
* Other miscellaneous changes

[Download the source code][dl-0.4.0]{ .md-button }

### v0.3.1
_Released on 2023-07-07 at 02:07:22 UTC_

_Words: 9,756_

* Created a CONTRIBUTING.md so contributors know what they need to
* Switched from AGPLv3 for the entire project to AGPLv3 for the source only,
  and CC BY-SA 4.0 for the content
* Added massive TODO check list in the README.MD
* Added building instructions
* Added an About page with information on the tutorial itself
* Added comment sections to all pages, not just the very front page
* Added a lot of images to the IDs & Requirements sections, with it nearly
  being done
* Added a table of contents to the Mechanics section, I'll do it to all places
  from now on
* Did a lot of work to the Publishing section
* Filled in a lot of the Reference section
* Updated abbreviations list
* Updated Manual of Style to include time and date formats

[Download the source code][dl-0.3.1]{ .md-button }

---

Content released under here is licensed under the [AGPLv3] licence.

---

### v0.3.0
_Released on 2022-06-17 at 19:48:21 UTC_

_Words: 5,844_

* Added first revision of the **Objects** page
* Tidied up previous stuff

[Download the source code][dl-0.3.0]{ .md-button }

### v0.2.0
_Released on 2022-06-17 at 17:37:11 UTC_

_Words: 5,199_

* Finished first revision of the **Rows** page
* Updated previous Introduction and other miscellaneous changes

[Download the source code][dl-0.2.0]{ .md-button }

### v0.1.0
_Released on 2022-06-17 at 13:40:35 UTC_

_Words: 4,003_

* Initial release
* Completed first revision of the **Introduction** section

[Download the source code][dl-0.1.0]{ .md-button }

## Licence
This site is dual-licensed under the [AGPLv3] and [CC0 1.0][CC0] licences.

### Content
All original content (text, images, etc) in this tutorial is licensed under
the [CC0 1.0][CC0] Universal Public Domain Dedication licence.

Content in this instance is defined as any text located within the `docs/`
directory, both how it is rendered in the website and how it exists within
source files as plaintext. The formatting markup for Markdown belongs to the
[Source Code](#source-code) licence. This means you can freely copy text from
this website, but you cannot freely copy the text along with the Markdown.

**No Copyright**

The person who associated a work with this deed has **dedicated** the work to
the public domain by waiving all of his or her rights to the work worldwide
under copyright law, including all related and neighboring rights, to the
extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission.

---

* In no way are the patent or trademark rights of any person affected by CC0,
  nor are the rights that other persons may have in the work or in how the work
  is used, such as publicity or privacy rights. 
* Unless expressly stated otherwise, the person who associated a work with this
  deed makes no warranties about the work, and disclaims liability for all uses
  of the work, to the fullest extent permitted by applicable law. 
* When using or citing the work, you should not imply endorsement by the author
  or the affirmer.

---

[To summarize](https://choosealicense.com/licenses/cc0-1.0/):

* **Permissions:**
    * **Commercial use:** The licensed material and derivatives may be used for
    commerical purposes.
    * **Distribution:** The licensed material may be distributed.
    * **Modification:** The licensed material may be modified.
    * **Private use:** The licensed material may be used and modified in
    private.
* **Limitations:**
    * **Liability:** This licence includes a limitation of liability.
    * **Patent use:** This licence explicitly states that it does NOT grant any
    rights in the patents of contributors.
    * **Trademark use:** This licence explicitly states that it does NOT grant
    trademark rights, even though licences without such a statement probably do
    not grant any implicit trademark rights.
    * **Warranty:** This licence explicitly states that it does NOT provide any
    warranty.

### Source Code
The source code for this tutorial is licensed under the [AGPLv3] licence
(unless stated otherwise in the source).

[To summarize](https://choosealicense.com/licenses/agpl-3.0/):

* **Permissions:**
    * **Commercial use:** The licensed material and derivatives may be used for
    commerical purposes.
    * **Distribution:** The licensed material may be distributed.
    * **Modification:** The licensed material may be modified.
    * **Patent use:** This licence provides an express grant of patent rights
    from contributors.
    * **Private use:** The licensed material may be used and modified in
    private.
* **Conditions:**
    * **Disclose source:** Source code must be made available when the licensed
    material is distributed.
    * **License and copyright notice:** A copy of the licence and copyright
    notice must be included with the licensed material.
    * **Network use is distribution:** Users who interact with the licensed
    material via network are given the right to receive a copy of the source
    code.
    * **Same licence:** Modifications must be released under the same licence
    when distributing the licensed material. In some cases a similar or
    related licence may be used.
    * **State changes:** Changes made to the licensed material must be
    documented.
* **Limitations:**
    * **Liability:** This licence includes a limitation of liability.
    * **Warranty:** This licence explicitly states that it does NOT provide any
    warranty.

<!-- URLs -->
[AGPLv3]: https://www.gnu.org/licenses/agpl-3.0.en.html
[CC0]: https://creativecommons.org/publicdomain/zero/1.0/
[CC BY-SA 4.0]: https://creativecommons.org/licenses/by-sa/4.0/
[icct]: https://upasadena.github.io/interactive-cyoa-creator/
[script-dc]: https://discord.com/channels/729044904675639398/787118552632393729/1135638576441327736

<!-- Latest download -->
[dl-VERSION]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/heads/main.zip
<!-- Downloads -->
[dl-0.1.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.1.0.zip
[dl-0.2.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.2.0.zip
[dl-0.3.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.3.0.zip
[dl-0.3.1]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.3.1.zip
[dl-0.4.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.4.0.zip
[dl-0.5.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.5.0.zip
[dl-0.5.1]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.5.1.zip
[dl-0.6.1]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.6.1.zip
[dl-0.7.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.7.0.zip
[dl-0.8.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.8.0.zip
[dl-0.9.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.9.0.zip
[dl-0.10.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.10.0.zip
[dl-0.11.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.11.0.zip
[dl-0.12.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.12.0.zip
[dl-0.13.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.13.0.zip
[dl-0.13.1]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.13.1.zip
[dl-0.13.2]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.13.2.zip
[dl-0.14.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.14.0.zip
[dl-0.15.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.15.0.zip
[dl-0.16.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.16.0.zip
[dl-0.17.0]: https://github.com/upasadena/interactive-cyoa-tutorial/archive/refs/tags/v0.17.0.zip

<!-- BUFFER -->
