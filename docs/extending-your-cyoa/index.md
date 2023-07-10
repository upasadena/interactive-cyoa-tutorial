---
comments: true
---

# Extending Your CYOA
Congratulations, you have learnt the core mechanics of the Interactive CYOA
Creator! However, this does not mean you are finished yet. There are more
things you could add and modify using external tools and code. This section
deals with all that, and more.

## Progress Indicator
By default, Interactive CYOAs load with a blank white screen. This is fine for
smaller CYOAs, but when it gets larger then depending on their internet speed,
players can become unsure if it will ever load at all.

Therefore, adding a loading progress indicator is strongly recommended for big
projects.

Compare having the progress indicator vs. not having it:

=== "Progress Indicator Present"

    ![](../images/120_progress_indicator_on.gif)

=== "Progress Indicator Absent"

    ![](../images/120_progress_indicator_off.gif)

    <sub>
    And yes, I am aware that that's my CYOA that doesn't have a progress
    indicator :P
    </sub>

### Adding the Progress Indicator
How do you add it to your CYOA then? It's simple, add this to your `index.html`
file, in the `<body>` section, but above `<div id="app">`.

!!! tip

    When it comes to code blocks like the one below, press the button in the
    top right in order to copy the entire block to your clipboard.

```html title="IntCyoaCreator download progress indicator by Agregen"
<!-- Insert the following in the beginning of <body> (on the line above <div id="app">) -->
<div id="indicator">
  <script>
    {
      let _XHR = XMLHttpRequest;
      XMLHttpRequest = class XHR extends _XHR {
        constructor() {
          super();
          this.addEventListener('progress', e => {
            indicator.innerText = " Loading data: " + (!e.total ? `${e.loaded} bytes` :
              `${(100 * e.loaded / e.total).toFixed(2)}%`)
          });
          this.addEventListener('loadend', () => {
            indicator.innerText = ""
          });
        }
      }
    }
  </script>
</div>
<!-- Modifier: replace `${e.loaded} bytes` with `${(e.loaded/1024**2).toFixed(1)} MB` to display size in MB -->
<!-- Modifier: replace the part after " Loading data: " with `${(100 * e.loaded / (e.total||SIZE)).toFixed(2)}%` to
                 always show percentage (SIZE is project.json size in bytes; remember to replace it on every update) -->
```

However, the above script loads in terms of bytes, which isn't really legible
nowadays. Use the below script instead to load in terms of megabytes:

```html title="IntCyoaCreator download progress indicator by Agregen"
<div id="indicator">
  <script>
    {
      let _XHR = XMLHttpRequest;
      XMLHttpRequest = class XHR extends _XHR {
        constructor() {
          super();
          this.addEventListener('progress', e => {
            indicator.innerText = " Loading data: " + (!e.total ? `${(e.loaded/1024**2).toFixed(1)} MB` :
              `${(100 * e.loaded / e.total).toFixed(2)}%`)
          });
          this.addEventListener('loadend', () => {
            indicator.innerText = ""
          });

        }
      }
    }
  </script>
</div>
```

Here's how loading with megabytes looks (blink and you'll miss it):

![](../images/120_progress_indicator_mb.gif)

## IntCYOAEnhancer script
The **IntCYOAEnhancer script** by [agregen] is a script hosted on Greasy Fork
which adds features on the client-side when playing CYOAs. It is available
[here][intcyoaenhancer]. Unlike the others on this list, this doesn't enhance
your ICYOAs as a creator, but as a player.

Some of the features of this script include:

* A download progress indicator (see [here](#progress-indicator) for adding
  that to your own CYOA, whether they have this script or not)
* Game state tracking, meaning if you reload on accident you can keep your
  choices
* An overview of selected choices and sections
* An option to enable the backpack (where you can export your choices for
  import again) if it's not already enabled
* A download option for any interactive's project.json file
* A cheat engine to change points
* And so much more

!!! question "Why should I bother to add the Progress Indicator if people could just use this script?"

    Many reasons: they might not know about it, they might not know how to
    install it, they might not be able to install it, the list goes on.

    It's simply a nice gesture to add the progress indicator, whether 

### Installing the Enhancer
To install this script, you first must install a relevant user script manager
addon. See [here](https://greasyfork.org/en) for a list of addons next to your
browser.

Next, navigate to the script page [here][intcyoaenhancer].

Simply press **Install this script** to add it to your script manager.

![](../images/121_installing_enhancer.gif)

After that, open up the IntCyoaEnhancer script and edit it, and look for a line
that looks like this:

```js
// @match        https://*.neocities.org/*
```

Under that line, copy and paste these lines:

```js
// @match        https://*.github.io/*
// @match        https://*.gitlab.io/*
```

Many CYOAs are hosted on GitHub ([Lt Ouroumov's Worm CYOA V6] and my CYOAs, for
example). Less people use GitLab, but *agregen*, the author of this script
does, so it's there just in case.

### Overview
Now when you load into any Interactive CYOA you should notice something in the
bottom right. This is the button that opens the **Overview** overlay, and it's
a sign that the installation is working as intended.

![](../images/122_enhancer_overview.png)

Pressing on that should yield the Overview menu. In this, you'll be able to
do three things:

1. See an outline of the entire CYOA (allowing for ease of copying your choices
to display on social media).
2. Navigate through the entire CYOA via Rows.
3. Roll a die/dice for RNG sections.

![](../images/123_enhancer_overview_2.png)

#### Activated
This is the list in the middle. You can hover over the bolded text that
represent your options in order to see their ID, descriptions, and Scores. It
also shows its Image if it has one.

#### Navigation
This is on the right-hand side. Press any of the Row Titles in order to jump to
there. A very conveninent tool.

#### Dice Roll
On the left side. This allows you to roll a dice for sections of the CYOA that
require you to roll a die or dice to get your result.

`NdM+K` means rolling an M-sided die N times and adding K to the total.

### Toolbar
You can access even more functions by pressing your script manager (mine being
Violentmonkey in this case) in your toolbar (if you have it pinned. if it's not
pinned, you should search for it by pressing the jigsaw puzzle piece.
considering pinning Violentmonkey if you're a big ICYOA fan).

![](../images/124_toolbar.png)

As you can see from that list, this tool is capable of quite a lot more.

#### Change webpage title
Many ICYOA creators do not know or do not care that you can change the title of
your websites in `index.html`. This can be frustrating when having many ICYOAs
open, and not being able to tell between them without switching to them.

This tool helps with that, in that it lets you change the title easily.

![](../images/125_e_title.gif)

#### Edit state
This lets you edit currently selected choices.

As an example, I will activate the ID `vllg`, which corresponds to the
`In One Ear...` choice:

![](../images/126_e_state.gif)

This can be useful in CYOAs that do not have a Backpack and Choice Import.

#### Toggle full scan mode
Full Scan mode is a togglable mode that changes the way that the Enhancer saves
data.

The Author says (paraphrased):
> It keeps track of all changes in app state; this overrides the default game
> state hash, including restoring the state on load and editing of the state
> string; this allows for storing state in apps where ids list import fails.
>
> This can be toggled on and off at any time, switching between IDs list and
> full scan snapshot.
>
> The state of both backpack and cheat add-ons is stored (and restored on load)
> as well.
>
> Implemented a multiline editor with JSON pretty-formatting (adjustable),
> highlighting and validation. (Also used for IDs list but without JSON
> features).

You can tell when it is in Full Scan mode by the colour of the bottom-right
Overview menu button. If it is dark, it is off. If it is light, it is on.

#### Downloading project data
This setting allows you to download a project's `project.json`, regardless of
how it is stored. For example, a few ICYOAs store their `project.json` data
inside of their `app.c533aa25.js`, and some store it in their `index.html`.
This option allows you to download the `project.json` in spite of that, which
is incredibly handy.

!!! warning

    This downloads the `project.json` in its current state.

    That means if you have selected some choices, when you load that
    `project.json` into the Creator, you'll have to deselect them if you wanted
    the project clean.

![](../images/127_e_download.gif)

#### Overview (Toolbar)
This just opens the [Overview](#overview) menu.

#### Cheat engine
This opens up the Cheat Engine. The Cheat Engine allows you to change any sort
of values.

!!! note

    Check out [launchcode01dl's Modded CYOAs] for a collection of Modded
    ICYOAs.

## Modded Viewer
!!! note

    Credit to [Om1cr0n](https://wormlewdmod.neocities.org/about) for this code.

In your project's `js` folder, replace `app.c533aa25.js` with the one from
==**[here](../static/fixed-app/app.c533aa25.js)**==. It's a fixed version that:

1. Doesn't sanitize `href`, `target`, and `rel` attributes in `<a>` tags in the
   HTML, enabling hyperlinking. See [here][a] for more.
2. Doesn't sanitize `<img>` tags in the HTML, allowing custom image insertion.
   See [here][img] for more.
3. Doesn't sanitize the `src` attribute in `<img>` tags.
4. Doesn't sanitize the `content` property in CSS, allowing arbitrary insertion
   of content via CSS. See [here][content] for more.

??? info "How it works"

    How does this work? Well, in the original `app.c533aa25.js` the author made
    it so that only specific html tags and attributes were allowed, and
    anything else would be "sanitized" (removed).

    We can take a deeper look if we run a `git diff` on the two files:

    ```diff
    diff --git a/pretty_app.js b/pretty_app.js
    index 6d6a7a6..1d8323a 100644
    --- a/pretty_app.js
    +++ b/pretty_app.js
    @@ -1008,8 +1008,10 @@
            data: function () {
            return {
                sanitizeArg: {
    -              allowedTags: ["address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre", "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"],
    +              allowedTags: ["img", "address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre", "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"],
                allowedAttributes: {
    +                a: ["href", "target", "rel"],
    +                img: ["src"],
                    p: ["style"],
                    b: ["style"],
                    span: ["style"],
    @@ -1018,6 +1020,7 @@
                allowedStyles: {
                    "*": {
                    color: [/^#(0x)?[0-9a-f]+$/i, /^[A-Za-z]+$/, /^rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)$/],
    +                  content: [/^.*$/],
                    "text-align": [/^left$/, /^right$/, /^center$/],
                    "font-size": [/^\d+(?:px|em|%)$/]
                    },
    @@ -1191,6 +1194,7 @@
                sanitizeArg: {
                allowedTags: ["address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre", "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"],
                allowedAttributes: {
    +                a: ["href", "target", "rel"],
                    p: ["style"],
                    b: ["style"],
                    span: ["style"],
    @@ -1756,6 +1760,7 @@
                sanitizeArg: {
                allowedTags: ["address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre", "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"],
                allowedAttributes: {
    +                a: ["href", "target", "rel"],
                    p: ["style"],
                    b: ["style"],
                    span: ["style"],
    @@ -2215,6 +2220,7 @@
                sanitizeArg: {
                allowedTags: ["address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre", "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"],
                allowedAttributes: {
    +                a: ["href", "target", "rel"],
                    p: ["style"],
                    b: ["style"],
                    span: ["style"],
    ```

    Here we can see that the new `app.c533aa25.js` file simply adds an
    exception for `<a>` tags and the `href` attribute, allowing for
    hyperlinking.

## Custom HTML, CSS, and JavaScript
You can truly supercharge your ICYOA by using HTML, CSS, and/or JavaScript.
Those three languages are the languages that every web browser runs on.

`HTML`

:   HyperText Markup Language. This language decides the general layout and
basic design of a web page.

`CSS`

:   Cascading Style Sheets. This language is what does the majority of the
styling. It's using this language that the most aethetically pleasing websites
you can think of achieve their look.

`JavaScript`

:   JavaScript is a scripting language. This language does the majority of the
logic and interactivity.

You can view some resources for learning HTML, CSS, and JavaScript over at
the [Resources](/appendix/resources/#programming-resources) section.

### Allowed HTML tags
!!! note

    **Remember:** Anything that is not allowed is only not allowed when
    it is inputted into the Creator itself, not if it is loaded separatedly
    in the `index.html`!

The following are the default allowed tags that are rendered with the Viewer:

<!-- Curiously, this list mentioned <main> twice -->

??? info

    | Tag                        | Explanation                                                                                         |
    | -------------------------- | --------------------------------------------------------------------------------------------------- |
    | [&lt;a&gt;]                | Defines a hyperlink[^1]                                                                             |
    | [&lt;abbr&gt;]             | Defines an abbreviation or an acronym                                                               |
    | [&lt;address&gt;]          | Defines contact information for the author/owner of a document                                      |
    | [&lt;article&gt;]          | Defines an article                                                                                  |
    | [&lt;aside&gt;]            | Defines content aside from the page content                                                         |
    | [&lt;b&gt;]                | Defines bold text                                                                                   |
    | [&lt;bdi&gt;]              | Isolates a part of text that might be formatted in a different direction from other text outside it |
    | [&lt;bdo&gt;]              | Overrides the current text direction                                                                |
    | [&lt;br&gt;]               | Defines a single line break                                                                         |
    | [&lt;blockquote&gt;]       | Defines a section that is quoted from another source                                                |
    | [&lt;caption&gt;]          | Defines a table caption                                                                             |
    | [&lt;cite&gt;]             | Defines the title of a work                                                                         |
    | [&lt;code&gt;]             | Defines a piece of computer code                                                                    |
    | [&lt;col&gt;]              | Specifies column properties for each column within a &lt;colgroup&gt; element                       |
    | [&lt;colgroup&gt;]         | Specifies a group of one or more columns in a table for formatting                                  |
    | [&lt;data&gt;]             | Adds a machine-readable translation of a given content                                              |
    | [&lt;dd&gt;]               | Defines a description/value of a term in a description list                                         |
    | [&lt;dfn&gt;]              | Specifies a term that is going to be defined within the content                                     |
    | [&lt;div&gt;]              | Defines a section in a document                                                                     |
    | [&lt;dl&gt;]               | Defines a description list                                                                          |
    | [&lt;dt&gt;]               | Defines a term/name in a description list                                                           |
    | [&lt;em&gt;]               | Defines emphasized text                                                                             |
    | [&lt;figcaption&gt;]       | Defines a caption for a &lt;figure&gt; element                                                      |
    | [&lt;figure&gt;]           | Specifies self-contained content                                                                    |
    | [&lt;footer&gt;]           | Defines a footer for a document or section                                                          |
    | [&lt;h1&gt; to &lt;h6&gt;] | Defines HTML headings                                                                               |
    | [&lt;header&gt;]           | Defines a header for a document or section                                                          |
    | [&lt;hgroup&gt;]           | Defines a heading and related content                                                               |
    | [&lt;hr&gt;]               | Defines a thematic change in the content                                                            |
    | [&lt;i&gt;]                | Defines a part of text in an alternate voice or mood                                                |
    | [&lt;kbd&gt;]              | Defines keyboard input                                                                              |
    | [&lt;li&gt;]               | Defines a list item                                                                                 |
    | [&lt;main&gt;]             | Specifies the main content of a document                                                            |
    | [&lt;mark&gt;]             | Defines marked/highlighted text                                                                     |
    | [&lt;nav&gt;]              | Defines navigation links                                                                            |
    | [&lt;ol&gt;]               | Defines an ordered list                                                                             |
    | [&lt;p&gt;]                | Defines a paragraph                                                                                 |
    | [&lt;pre&gt;]              | Defines preformatted text                                                                           |
    | [&lt;q&gt;]                | Defines a short quotation                                                                           |
    | [&lt;rb&gt;]               | Defines a ruby base element                                                                         |
    | [&lt;rp&gt;]               | Defines what to show in browsers that do not support ruby annotations                               |
    | [&lt;rt&gt;]               | Defines an explanation/pronunciation of characters (for East Asian typography)                      |
    | [&lt;rtc&gt;]              | Defines a Ruby Text Container                                                                       |
    | [&lt;ruby&gt;]             | Defines a ruby annotation (for East Asian typography)                                               |
    | [&lt;s&gt;]                | Defines text that is no longer correct                                                              |
    | [&lt;samp&gt;]             | Defines sample output from a computer program                                                       |
    | [&lt;section&gt;]          | Defines a section in a document                                                                     |
    | [&lt;small&gt;]            | Defines smaller text                                                                                |
    | [&lt;span&gt;]             | Defines a section in a document                                                                     |
    | [&lt;strong&gt;]           | Defines important text                                                                              |
    | [&lt;sub&gt;]              | Defines subscripted text                                                                            |
    | [&lt;sup&gt;]              | Defines superscripted text                                                                          |
    | [&lt;table&gt;]            | Defines a table                                                                                     |
    | [&lt;tbody&gt;]            | Groups the body content in a table                                                                  |
    | [&lt;td&gt;]               | Defines a cell in a table                                                                           |
    | [&lt;tfoot&gt;]            | Groups the footer content in a table                                                                |
    | [&lt;th&gt;]               | Defines a header cell in a table                                                                    |
    | [&lt;thead&gt;]            | Groups the header content in a table                                                                |
    | [&lt;time&gt;]             | Defines a specific time (or datetime)                                                               |
    | [&lt;tr&gt;]               | Defines a row in a table                                                                            |
    | [&lt;u&gt;]                | Defines some text that is unarticulated and styled differently from normal text                     |
    | [&lt;ul&gt;]               | Defines an unordered list                                                                           |
    | [&lt;var&gt;]              | Defines a variable                                                                                  |
    | [&lt;wbr&gt;]              | Defines a possible line-break                                                                       |

[^1]: The ICC sanitizes hyperlinks by default, use the
[modded Viewer](#modded-viewer) to enable it.

<!-- HTML tag URLs -->
[&lt;address&gt;]: https://www.w3schools.com/tags/tag_address.asp
[&lt;article&gt;]: https://www.w3schools.com/tags/tag_article.asp
[&lt;aside&gt;]: https://www.w3schools.com/tags/tag_aside.asp
[&lt;footer&gt;]: https://www.w3schools.com/tags/tag_footer.asp
[&lt;header&gt;]: https://www.w3schools.com/tags/tag_header.asp
[&lt;h1&gt; to &lt;h6&gt;]: https://www.w3schools.com/tags/tag_hn.asp
[&lt;hgroup&gt;]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup
[&lt;main&gt;]: https://www.w3schools.com/tags/tag_main.asp
[&lt;nav&gt;]: https://www.w3schools.com/tags/tag_nav.asp
[&lt;section&gt;]: https://www.w3schools.com/tags/tag_section.asp
[&lt;blockquote&gt;]: https://www.w3schools.com/tags/tag_blockquote.asp
[&lt;dd&gt;]: https://www.w3schools.com/tags/tag_dd.asp
[&lt;div&gt;]: https://www.w3schools.com/tags/tag_div.asp
[&lt;dl&gt;]: https://www.w3schools.com/tags/tag_dl.asp
[&lt;dt&gt;]: https://www.w3schools.com/tags/tag_dt.asp
[&lt;figcaption&gt;]: https://www.w3schools.com/tags/tag_figcaption.asp
[&lt;figure&gt;]: https://www.w3schools.com/tags/tag_figure.asp
[&lt;hr&gt;]: https://www.w3schools.com/tags/tag_hr.asp
[&lt;li&gt;]: https://www.w3schools.com/tags/tag_li.asp
[&lt;ol&gt;]: https://www.w3schools.com/tags/tag_ol.asp
[&lt;p&gt;]: https://www.w3schools.com/tags/tag_p.asp
[&lt;pre&gt;]: https://www.w3schools.com/tags/tag_pre.asp
[&lt;ul&gt;]: https://www.w3schools.com/tags/tag_ul.asp
[&lt;a&gt;]: https://www.w3schools.com/tags/tag_a.asp
[&lt;abbr&gt;]: https://www.w3schools.com/tags/tag_abbr.asp
[&lt;b&gt;]: https://www.w3schools.com/tags/tag_b.asp
[&lt;bdi&gt;]: https://www.w3schools.com/tags/tag_bdi.asp
[&lt;bdo&gt;]: https://www.w3schools.com/tags/tag_bdo.asp
[&lt;br&gt;]: https://www.w3schools.com/tags/tag_br.asp
[&lt;cite&gt;]: https://www.w3schools.com/tags/tag_cite.asp
[&lt;code&gt;]: https://www.w3schools.com/tags/tag_code.asp
[&lt;data&gt;]: https://www.w3schools.com/tags/tag_data.asp
[&lt;dfn&gt;]: https://www.w3schools.com/tags/tag_dfn.asp
[&lt;em&gt;]: https://www.w3schools.com/tags/tag_em.asp
[&lt;i&gt;]: https://www.w3schools.com/tags/tag_i.asp
[&lt;kbd&gt;]: https://www.w3schools.com/tags/tag_kbd.asp
[&lt;mark&gt;]: https://www.w3schools.com/tags/tag_mark.asp
[&lt;q&gt;]: https://www.w3schools.com/tags/tag_q.asp
[&lt;rb&gt;]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rb
[&lt;rp&gt;]: https://www.w3schools.com/tags/tag_rp.asp
[&lt;rt&gt;]: https://www.w3schools.com/tags/tag_rt.asp
[&lt;rtc&gt;]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rtc
[&lt;ruby&gt;]: https://www.w3schools.com/tags/tag_ruby.asp
[&lt;s&gt;]: https://www.w3schools.com/tags/tag_s.asp
[&lt;samp&gt;]: https://www.w3schools.com/tags/tag_samp.asp
[&lt;small&gt;]: https://www.w3schools.com/tags/tag_small.asp
[&lt;span&gt;]: https://www.w3schools.com/tags/tag_span.asp
[&lt;strong&gt;]: https://www.w3schools.com/tags/tag_strong.asp
[&lt;sub&gt;]: https://www.w3schools.com/tags/tag_sub.asp
[&lt;sup&gt;]: https://www.w3schools.com/tags/tag_sup.asp
[&lt;time&gt;]: https://www.w3schools.com/tags/tag_time.asp
[&lt;u&gt;]: https://www.w3schools.com/tags/tag_u.asp
[&lt;var&gt;]: https://www.w3schools.com/tags/tag_var.asp
[&lt;wbr&gt;]: https://www.w3schools.com/tags/tag_wbr.asp
[&lt;caption&gt;]: https://www.w3schools.com/tags/tag_caption.asp
[&lt;col&gt;]: https://www.w3schools.com/tags/tag_col.asp
[&lt;colgroup&gt;]: https://www.w3schools.com/tags/tag_colgroup.asp
[&lt;table&gt;]: https://www.w3schools.com/tags/tag_table.asp
[&lt;tbody&gt;]: https://www.w3schools.com/tags/tag_tbody.asp
[&lt;td&gt;]: https://www.w3schools.com/tags/tag_td.asp
[&lt;tfoot&gt;]: https://www.w3schools.com/tags/tag_tfoot.asp
[&lt;th&gt;]: https://www.w3schools.com/tags/tag_th.asp
[&lt;thead&gt;]: https://www.w3schools.com/tags/tag_thead.asp
[&lt;tr&gt;]: https://www.w3schools.com/tags/tag_tr.asp

### Allowed Attributes
Attributes provide additional information about HTML elements.

| HTML tag         | Explanation                     | Attribute(s) |
| ---------------- | ------------------------------- | ------------ |
| [&lt;b&gt;]      | Defines bold text               | [style]      |
| [&lt;p&gt;]      | Defines a paragraph             | [style]      |
| [&lt;span&gt;]   | Defines a section in a document | [style]      |
| [&lt;strong&gt;] | Defines important text          | [style]      |

<!-- Attributes list -->
[style]: https://www.w3schools.com/tags/att_style.asp

### Allowed Styles
| CSS Target | Property                               | Explanation                                                                                             |
| ---------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| *          | [color]<br>[text-align]<br>[font-size] | Sets the color of text<br>Specifies the horizontal alignment of text<br>Specifies the font size of text |
| p          | [font-size]                            | Specifies the font size of text                                                                         |

<!-- Styles list -->
[color]: https://www.w3schools.com/cssref/pr_text_color.php
[text-align]: https://www.w3schools.com/cssref/pr_text_text-align.php
[font-size]: https://www.w3schools.com/cssref/pr_font_font-size.php

<!-- URLs -->
[content]: https://www.w3schools.com/cssref/pr_gen_content.php
[img]: https://www.w3schools.com/tags/tag_img.asp
[a]: https://www.w3schools.com/tags/tag_a.asp
[agregen]: https://agregen.gitlab.io/
[Lt Ouroumov's Worm CYOA V6]: https://ltouroumov.github.io/worm-cyoa-v6-fork/viewer/
[intcyoaenhancer]: https://greasyfork.org/en/scripts/438947-intcyoaenhancer
[launchcode01dl's Modded CYOAs]: https://launchcode01dl.github.io/cyoa/

<!-- BUFFER -->