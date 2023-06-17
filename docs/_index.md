---
comments: true
---

# Interactive CYOA Tutorial

This is a complete and comprehensive guide to using the [Interactive
CYOA Creator](Interactive_CYOA_Creator "wikilink") by
[MeanDelay](MeanDelay "wikilink").

## Introduction

### Useful links

#### Interactive CYOA Creator

-   [Online creator](https://intcyoacreator.onrender.com/)
-   [Offline creator at itch.io (one time purchase of at least 2.50
    USD)](https://meandelay.itch.io/interactive-cyoa-creator)

#### Subreddits

-   [r/InteractiveCYOA](https://www.reddit.com/r/InteractiveCYOA/) – If
    you make a CYOA, feel free to showcase it here!
-   [r/makeyourchoice](https://www.reddit.com/r/makeyourchoice/) (mainly
    static CYOAs, but interactive are accepted if you link the static)

#### Other Tutorials

-   [How to guide on making interactive CYOAs for a first time creator.
    (Reddit)](https://www.reddit.com/r/InteractiveCYOA/comments/nxrlvm/how_to_guide_on_making_interactive_cyoas_for_a/)
    – This guide shows you how to upload your finished [Interactive
    CYOAs](Interactive_CYOA "wikilink") to Neocities, which is also
    covered in this tutorial [here](#Uploading_Your_Project "wikilink")
    -   [Imgur](https://imgur.com/a/QV36Ix8)
    -   [Google
        Slides](https://docs.google.com/presentation/d/18wSgIooZxM_uA3I90KmZICl9guaQMeVIuqCpV-UffJA/edit)
-   [Tips and Pitfalls for Interactive CYOA Creators
    (Reddit)](https://www.reddit.com/r/InteractiveCYOA/comments/wrf0hl/tips_and_pitfalls_for_interactive_cyoa_creators/)

### Launching the creator

When you launch the creator, you will be greeted with this screen:

<div class="res-img">

<figure>
<img src="0a_start.png" title="0a_start.png" />
<figcaption>0a_start.png</figcaption>
</figure>

</div>

#### Open Image-CYOA Creator

This is where you go to create [Interactive
CYOAs](Interactive_CYOA "wikilink").

When you first open it, you will be greeted with a blank screen and a
minimized sidebar. To learn more about the sidebar, go to [#The
Sidebar](#The_Sidebar "wikilink").

<div class="res-img">

<figure>
<img src="0b_creator.png" title="0b_creator.png" />
<figcaption>0b_creator.png</figcaption>
</figure>

</div>

This is what a complete CYOA would look like in this menu:

<div class="res-img">

<figure>
<img src="0bb_full_creator.png" title="0bb_full_creator.png" />
<figcaption>0bb_full_creator.png</figcaption>
</figure>

</div>

#### Open Image-CYOA Viewer

This is where you can preview CYOAs before you upload them. You can play
them, but options selected in the viewer will persist in the editor, so
make sure you [reset the options](#Resetting_choices "wikilink").

</div>
<div class="res-img">

<figure>
<img src="0c_viewer.png" title="0c_viewer.png" />
<figcaption>0c_viewer.png</figcaption>
</figure>

</div>

#### Help and Instructions

A small tutorial made by the author themself. It should be redundant
with this tutorial, but you may wish to check it out anyway.

<div class="res-img">

<figure>
<img src="0d_help_and_instructions.gif"
title="0d_help_and_instructions.gif" />
<figcaption>0d_help_and_instructions.gif</figcaption>
</figure>

</div>

### The Sidebar

## Basics

### Rows

The basic building block of Interactive CYOAs made with this creator is
the Row. Rows are not only the sections that divide the CYOA up, but it
is only attached to a row where choices can exist.

#### Creating Rows

Create a row by opening up the sidebar and pressing **Create New Row**.

<div class="res-img">

<figure>
<img src="1_creating_a_row.gif" title="1_creating_a_row.gif" />
<figcaption>1_creating_a_row.gif</figcaption>
</figure>

</div>

#### Cloning Rows

To clone a row, press the
<img src="2_clone_button.png" title="2_clone_button.png" width="30"
alt="2_clone_button.png" /> button.

Cloning rows can be useful when you have [private
styling](#Private_Styling "wikilink") or a specific set of choices you
need to repeat.

<div class="res-img">

<figure>
<img src="4_clone_row.gif" title="4_clone_row.gif" />
<figcaption>4_clone_row.gif</figcaption>
</figure>

</div>

#### Deleting Rows

To delete a row, press the
<img src="3_delete_button.png" title="3_delete_button.png" width="30"
alt="3_delete_button.png" /> button and then **OK**.

<div class="res-img">

<figure>
<img src="5_delete_row.gif" title="5_delete_row.gif" />
<figcaption>5_delete_row.gif</figcaption>
</figure>

</div>

#### Editing a Row

To edit a row, press the wrench/spanner icon:
<img src="6_edit_row.png" title="6_edit_row.png" width="30"
alt="6_edit_row.png" />.

This will open the edit menu for the row.

<div class="res-img">

<figure>
<img src="7_edit_row.gif" title="7_edit_row.gif" />
<figcaption>7_edit_row.gif</figcaption>
</figure>

</div>

#### Row Title

By default, the row title will be **Row**.

As rows are generally sections (such as Powers, Perks, Drawbacks, etc),
you should name your row after what the choices represent.

To edit the row title, simply edit the text in the **Row Title**
section.

<div class="res-img">

<figure>
<img src="8_row_title.gif" title="8_row_title.gif" />
<figcaption>8_row_title.gif</figcaption>
</figure>

</div>

#### Row Text

Row Text can be used to provide a description of the section.

You can also use it to provide notes specific to the section in
particular, such as informing the players that they can select only 1
option.

To edit the row text, simply edit the text in the **Row Text section**.

<div class="res-img">

<figure>
<img src="9_row_text.gif" title="9_row_text.gif" />
<figcaption>9_row_text.gif</figcaption>
</figure>

</div>

#### Allowed Choices

The **Allowed Choices** options allows you to restrict the amount of
choices a player can pick in that row. It takes a positive integer (a
whole number, like 5 or 28).

If you want ANY number of options with no limits, simply put `0` into
the field.

This is used for sections where you might say "You may only take X
options".

There will be a way to dynamically change this amount, but we’ll come
back to that later (to skip ahead, see
[here](#Adds_or_takes_away_a_rows_Allowed_Choices "wikilink")).

<div class="res-img">

<figure>
<img src="10_allowed_choices.png" title="10_allowed_choices.png" />
<figcaption>10_allowed_choices.png</figcaption>
</figure>

</div>

------------------------------------------------------------------------

<div class="res-img">

<figure>
<img src="10b_allowed_choices.gif" title="10b_allowed_choices.gif" />
<figcaption>10b_allowed_choices.gif</figcaption>
</figure>

</div>

#### Selected Choices (Input)

The 'Selected Choices' will show how many choices are currently
selected, and should normally be 0.

**You should not change this value unless you know what you're doing.**

If it is something else and no choices are selected, then something has
gone wrong. You can fix this by changing the value to 0.

<div class="res-img">

<figure>
<img src="11_selected_choices.gif" title="11_selected_choices.gif" />
<figcaption>11_selected_choices.gif</figcaption>
</figure>

</div>

#### Objects Per Row

The **Objects Per Row** option allows you to determine how many choices
are present within a row.

<div class="res-img">

<figure>
<img src="12_objects_per_row.png" title="The option" />
<figcaption>The option</figcaption>
</figure>

</div>

**Preview:**

13_1_per_row.png\|link=\|1 per Row 14_3_per_row.png\|link=\|3 per Row
15_4_per_row.png\|link=\|4 per Row

##### 'Row' Objects per Row

Most Row Width (A Row's `Objects Per Row` number) options seem pretty
straightforward, but this one in particular might get confusing. It is
not used by a Row's Row Width (thought the option is bafflingly there),
it is instead used for individual Choice Widths (An Object/Choice's
`Object Width`).

Choices have an Object Width of `Row` by default, and that means that
their width is equal to whatever is set by the Row Width. This is
convenient in that you don't need to go into each and every choice width
and update it, instead only updating the Row Width once.

If you have changed an individual Choice's width, then setting back to
Row resets it back to the default.

#### Non-Activatable?

For when you just want to supply information and don’t want those
information boxes (choices) to be selected.

From the official tutorial:

  
*The third button will make it impossible for a player to change any of
the choices, if one is selected then it will stay selected and vice
versa. Good to use when the user should be given information or story,
and not choices.*

<div class="res-img">

<figure>
<img src="16_non_activatable.gif" title="16_non_activatable.gif" />
<figcaption>16_non_activatable.gif</figcaption>
</figure>

</div>

#### Selected Choices? (Switch)

The `Selected Choices?` switch enables a whole host of other options
that have to do with the choices in the row.

From the official tutorial:

  
<i>The middle button named 'Selected Choices?' can be used to make the
row show all choices that have been selected, good to use at the end of
the project to let the player see the choices they have made. A private
row design should be used to make filters invisible.</i>

<div class="res-img">

<figure>
<img src="image.gif" title="image.gif" />
<figcaption>image.gif</figcaption>
</figure>

</div>

##### Selected Choices from Group Id

##### Deselect choices when Row lacks requirements?

##### Choices will all be 'Template Top' and Row Width

This option will force all images to display above choices (instead of,
say, to the side or below), as well as have all the choices take up the
same row width as is set in the Row settings (cancelling any custom Row
Widths for choices, forcing standardization).

##### Remove the text of the choices

This option removes the body text of all the choices within the row, but
keeps the title and images.

##### Show the title of the row in the choice.

#### Half of the Screen?

For when you want two rows side by side.

#### Row List (Side Menu)

This can be useful when moving rows over a lot of other rows.

#### Sort The Choices In The Row (Row Settings)

This can be useful.

### Choices / Objects

Choices (also called Objects by the creator) are individual options that
can be selected by the player.

#### Creating Choices

#### Cloning and Deleting Choices

Same as with rows.

#### Resetting choices

If you've accidentally activated choices, you can reset them using the
following methods:

#### Object Width

For sizing your section.

#### Functions

##### Selecting this choice will deselect other choices

very dangerous but useful

##### This choice can be selected multiple times

Use simply variable instead of a point type in almost all situations

##### Selecting this choice will be impossible

Kind of like the Row Non-Activatable option, but instead for individual
choices. In my experience, has been known to be buggy

##### Forces another choice active

Program Explanation: Works badly if multiple of these have the same ID,
or if the target has requirements attached. You can use commas to
activate multiple (ID,ID,ID).

##### Will make another choice unselected

The opposite of forcing one active, this forcibly deactivates it

##### Adds or takes away a rows Allowed Choices

Can be used to dynamically change what a rows Allowed Choices are.

Little trick: Having a choice affect the Allowed Choices of the row that
it is in allows it to be selected without affecting the number of
allowed choices.

#### Clean Selected Choices (Side Menu)

### IDs & Requirements

#### IDs – Unique Identifiers

What are IDs? IDs are unique identifiers that allow the creator to
directly access any object, whether that be rows, choices, points, or
groups.

They are particularly useful in situations where you have lots of
choices that have requirements, meaning if you assign IDs according to
regular, predictable rules, you don't need to check what the IDs are.

**It is strongly suggested that you change default IDs.**

#### Requirements

##### Selected choice

if x == true

##### Non-selected choice

if x != true

##### ‘One of these is selected’ requirement

OR

##### ‘None of these is selected’ requirement

XOR?

##### Doing multiple selected choices

AND

##### Doing multiple non-selected choices

NOR

#### Hiding Rows via Selected Choice

##### Nested Rows

Based on
[this](https://www.reddit.com/r/InteractiveCYOA/comments/wrf0hl/tips_and_pitfalls_for_interactive_cyoa_creators/).

  
*The third common pitfall is row nesting, specifically how NOT to do it.
Now nesting rows in and of itself isn't a bad thing. It prevents having
to scroll through hundreds of choices to find the section you want (one
of the few design flaws of the WoW ICYOA listed above). Instead, you
design the various rows to only show when the prerequisite choice is
active, basically showing up at the push of a button. Nesting rows
occurs when the button for a row is inside another row, which can be
inside another row, and so on. Overusing this can lead to your users
being confused and annoyed, having to search through nested row after
nested row to find the section they want. Not fun. Finding the right
balance between "ALL THE CHOICES" and "Where the hell is it!" is
important.  
  
Another problem with nested rows is avoiding orphaned rows. Orphaned
rows occur when attempting to close multiple levels of nested rows by
closing the top row leaves the lower rows still visible. This is an
annoying design flaw that forces your users to close nested rows in
order, every time.  
  
What's worse is if the button for a nested row is a choice you want to
keep, leaving you unable to close the orphan row without screwing up
your build. This is both aggravating and very unprofessional. To
counteract this, require all your nested rows to need all previous
levels active to appear. Thus, if you close an upper level, it will
close all lower levels. This does become slightly tedious to code the
deeper a nested row is, however.*

#### Disabled Choices via Selected Choice

Hiding choices using filters – almost always use private styling

#### Navigation with ID / Title list

ID / Title list as helpful way of navigating your way through a large
CYOA – showcase JRPG Traitor

#### Reusing IDs

Interesting fact: Setting multiple things to the same ID allows you to
activate one through the other

### Points & Scores

#### Creating Points

##### Names

##### Starting Sum

##### The Power of Hidden Point Types

**This score is not allowed to go under 0**

I find it particularly useful in hidden point types that determine how
much of a thing you’re allowed to select

##### +/- Score Signs

**Add a + or - in front of the scores**

##### Positive/Negative Colours

**Set colors for positive or negative**

##### Score Icon

##### Hide Point Types

ID needed to show

#### Scores

##### Adding Scores

##### Subtract Points

This is the default behaviour.

##### Add Points

##### Text Before

Change to something like “Gain:” or “Gives:” when adding points, but
keep it at "Cost:" when subtracting points.

##### Show Score?

This can be used to hide mechanics, or if the image shows the points
already.

##### Requirements and Discounts

Discounts can be made using requirements.

### Images

It is advisable that you do not upload images until the core mechanics
of the CYOA are complete. The vast majority of space that an Interactive
CYOA takes up is due to images, and a huge amount of images will slow
down lower end PCs. CYOAs over 300 MB are known to have caused issues.

#### Local vs External Images

There are pros and cons to using both local and external images for
choices.

<table>
<caption>Local vs External Images</caption>
<thead>
<tr class="header">
<th><p>Image type</p></th>
<th><p>Pros</p></th>
<th><p>Cons</p></th>
<th><p>Use case</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Local images</strong></p></td>
<td><p>+ Faster<br />
+ More reliable</p></td>
<td><p>- Takes up space (too much space can crash the creator, and most
free website hosts limit how much space you can use)</p></td>
<td><p>Smaller projects (&lt;300 MB)</p></td>
</tr>
<tr class="even">
<td><p><strong>External images</strong></p></td>
<td><p>+ You keep the size of your project.json down</p></td>
<td><p>- Slower<br />
- You have to trust the servers won't delete the image</p></td>
<td><p>Larger projects (&gt;300 MB)</p></td>
</tr>
</tbody>
</table>

Local vs External Images

#### Local Images

#### External Images

##### Image host sites

Keep in mind that your images should follow a host's terms and
conditions in order to not have the image removed. **Public**

-   [Imgur](https://imgur.com/)

**Private**

-   Discord (open image preview → **Open in Browser** to get the link)

#### Cropping

##### Aspect Ratios

These are useful for consistent image sizes between choices.

#### Templates/Image Position

Templates change the placement and position of an accompanying image to
a row or choice. The default behaviour is "Image Top", which places the
image above the row or choice. The other two options are:

-   **Image Left** – Places image to the left
-   **Image Right** – Places image to the right

There is a third option, **Image Bottom**, but curiously it is only
available for Row Templates, and Choice Templates do not have that
option.

#### Image Compression

### Backpack & Choice Import

### Changing Defaults

### Uploading Your Project

## Advanced Mechanics

### Addons

### Copying

### Words

### Buttons & Variables

### Groups

## Styling

### Important Advice

**BEFORE** styling your CYOA, make your that the core functionality
(text, scoring, logic, and images) of it is finished.

The reason is twofold:

1.  Because as you make your CYOA you might be tempted to make private
    styling choices, which is not advisable (the reasons of which are
    below)
2.  Excessive styling may slow down the preview slightly, meaning it
    will be that much harder to edit your CYOA.

**BEFORE** using private styling, make sure that you have styled all of
the CYOA using the global options. This is because once private styling
is turned on, the styling cannot be overridden by the global options.

So if, for example, you decide you like a different font in CYOA, but
you have a dozen private stylized sections, you would need to either

1.  Go to each of those sections for each change you make, and change
    the private styling, or
2.  Turn off private styling to reset the styling, then reapplying the
    private style options for each section.

### Style Templates

### Colour Palettes

### Backgrounds

#### Static Background

See [#Making a Static
Background](#Making_a_Static_Background "wikilink") for more.

### Text

### Filters

### Private Styling

## Extending your CYOA

Congratulations, you have learnt the core mechanics of the Interactive
CYOA Creator! However, this does not mean you are finished yet. There
are more things to add and modify using external tools and code. This
section deals with all that, and more.

### Making a Table of Contents (Tabs Menu)

### Progress Indicator

By default, Interactive CYOAs load with a blank white screen. This is
fine for smaller CYOAs, but when it gets larger then depending on their
internet speed, players can become unsure if it will ever load at all.

### IntCYOAEnhancer script

The **IntCYOAEnhancer** script by [agregen](https://agregen.gitlab.io/)
is a script hosted on Greasy Fork which adds features on the client-side
when playing CYOAs. It is available
[here](https://greasyfork.org/en/scripts/438947-intcyoaenhancer).

Some of the features of this script include:

-   A download progress indicator (see
    [here](#Progress_Indicator "wikilink") for adding that to your own
    CYOA, whether they have this script or not)
-   Game state tracking, meaning if you reload on accident you can keep
    your choices
-   An overview of selected choices and sections
-   An option to enable the backpack (where you can export your choices
    for import again) if it's not already enabled
-   A download option for any interactive's `project.json` file
-   A cheat engine to change points

#### Installation

To install this script, you first must install a relevant user script
manager addon. See [here](https://greasyfork.org/en) for a list of
addons next to your browser under **Step 1**.

Here is a mirrored list (warning: may not be up to date):

| Application        | Desktop                                                                                                                                                                                                                                       | Mobile (Android)                                                                                                                                                                                                                              | Mobile (IOS)                                                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Chrome**         | [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) or [Violentmonkey](https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)                          |                                                                                                                                                                                                                                               |                                                                                                                                    |
| **Firefox**        | [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/), [Tampermonkey](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/), or [Violentmonkey](https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/) | [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/), [Tampermonkey](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/), or [Violentmonkey](https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/) |                                                                                                                                    |
| **Safari**         | [Tampermonkey](https://www.tampermonkey.net/index.php?browser=safari) or [Userscripts](https://apps.apple.com/app/userscripts/id1463298887)                                                                                                   |                                                                                                                                                                                                                                               | [Tampermonkey](https://www.tampermonkey.net/?browser=safari) or [Userscripts](https://apps.apple.com/app/userscripts/id1463298887) |
| **Microsoft Edge** | [Tampermonkey](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd) or [Violentmonkey](https://microsoftedge.microsoft.com/addons/detail/violentmonkey/eeagobfjdenkkddmbclomhiblgggliao)          |                                                                                                                                                                                                                                               |                                                                                                                                    |
| **Opera**          | [Tampermonkey](https://addons.opera.com/en/extensions/details/tampermonkey-beta/) or [Violentmonkey](https://violentmonkey.github.io/get-it/) (Violentmonkey points you to the Chrome Web Store)                                              |                                                                                                                                                                                                                                               |                                                                                                                                    |
| **Maxthon**        | [Violentmonkey](https://extension.maxthon.com/detail/index.php?view_id=1680)                                                                                                                                                                  | [Violentmonkey](https://extension.maxthon.com/detail/index.php?view_id=1680)                                                                                                                                                                  |                                                                                                                                    |
| **Adguard**        | (no additional software required)                                                                                                                                                                                                             | ←                                                                                                                                                                                                                                             | ←                                                                                                                                  |
| **Dolphin**        |                                                                                                                                                                                                                                               | [Tampermonkey Dolphin](https://play.google.com/store/apps/details?id=net.tampermonkey.dolphin)                                                                                                                                                |                                                                                                                                    |
| **UC**             |                                                                                                                                                                                                                                               | [Tampermonkey](https://www.tampermonkey.net/?browser=ucweb&ext=dhdg)                                                                                                                                                                          |                                                                                                                                    |
| **Kiwi**           |                                                                                                                                                                                                                                               | [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) or [Violentmonkey](https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)                          |                                                                                                                                    |
| **XBrowser**       |                                                                                                                                                                                                                                               | [XBrowser](https://www.xbext.com/) (no additional software required)                                                                                                                                                                          |                                                                                                                                    |
| **Gear**           |                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                               | [Gear](https://gear4.app/) (no additional software required)                                                                       |

User script managers by platform and application

#### GitHub and other sites compatibility

This script is on by default for all Neocities sites, however, many
[Interactive CYOAs](Interactive_CYOA "wikilink") are hosted on
[GitHub](https://github.com) (such as Lt Ouroumov's Worm CYOA V6 fork),
and as such the script needs to be edited for that (and for any other
website hosts) as well.

To edit this, after installing, open up the extension, and underneath
this:

    // @match        https://*.neocities.org/*

Add this line:

    // @match        https://*.github.io/*

The asterisk means "match anything that comes here".

### Making a Static Background

A static background, as opposed to a continuous or overlapping
background, is one that scrolls with the user, perfect for backgrounds
that do not repeat perfectly.

An example of a continuous background is the [Worm V3
Revised](https://upasadena.github.io/cyoas/worm/v3/) interactive. No
matter how far you scroll, the background stays in the exact same
position.

It was first used in the [Jedi - Guardian of the Republic
Interactive](https://www.reddit.com/r/InteractiveCYOA/comments/w5mick/jedi_guardian_of_the_republic_interactive/)
CYOA, where the background fixes are attributed to
[u/LOLLOL12344](https://www.reddit.com/user/LOLLOL12344).

<div class="res-img">

<figure>
<img src="NA_static_background.gif" title="NA_static_background.gif" />
<figcaption>NA_static_background.gif</figcaption>
</figure>

</div>

To achieve this, simply add the following code in your `index.html`,
above the <code>

``` html
<div id=app></div>
```

</code> line.

``` html
<div id="indicator"><script>{let _XHR = XMLHttpRequest;  XMLHttpRequest = class XHR extends _XHR {constructor () {
  super();
  this.addEventListener('loadend', () => {indicator.innerText = "",document.getElementsByClassName("pb-12")[0].style.cssText += "background-size: cover;background-position: center;background-attachment: fixed;"});
}}}</script></div>
```

This is the same code where the progress indicator is located, so if you
wanted both it would look like this:

``` html
<div id="indicator"><script>{let _XHR = XMLHttpRequest;  XMLHttpRequest = class XHR extends _XHR {constructor () {
  super();
  this.addEventListener('progress', e => {indicator.innerText = " Loading data: " + (!e.total ? `${(e.loaded/1024**2).toFixed(1)} MB` : `${(100 * e.loaded / e.total).toFixed(2)}%`)});
  this.addEventListener('loadend', () => {indicator.innerText = "",document.getElementsByClassName("pb-12")[0].style.cssText += "background-size: cover;background-position: center;background-attachment: fixed;"});
}}}</script></div>
```

### Saving Space

Saving space is a good idea for a myriad of reasons. It takes up less
personal space, less space on website hosts, and it means your project
loads faster for developers and for end users.

#### Compress Images

See [#Image Compression](#Image_Compression "wikilink").

#### Use URLs for Images

The defining reason Interactive CYOAs often take up so much space, is
because of the images. Whether they are simply large in size (See
[#Image Compression](#Image_Compression "wikilink")) or in number. A way
to counteract this, is to simply not host the images, and link to it
instead. This will also have the added benefit of not taking up space
from whatever host you're using.

See how to do this at [#External_Images](#External_Images "wikilink").

### Custom HTML, CSS, and JavaScript

If you learn HTML, CSS, and/or JavaScript, you can apply it to your
`index.html` file, further enhancing the appearance and behaviour of
your Interactive CYOA.

#### Formatting

To format text within the CYOA, use these HTML tags:

##### Headings

<table>
<thead>
<tr class="header">
<th><p>Example</p></th>
<th><p>HTML</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="display: block; font-size: 2em; margin-top: 0.67em; margin-bottom: 0.67em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
1</span></p></td>
<td><pre class="html"><code>&lt;h1&gt;Heading 1&lt;/h1&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p><span style="display: block; font-size: 1.5em; margin-top: 0.83em; margin-bottom: 0.83em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
2</span></p></td>
<td><pre class="html"><code>&lt;h2&gt;Heading 2&lt;/h2&gt;</code></pre></td>
</tr>
<tr class="odd">
<td><p><span style="display: block; font-size: 1.17em; margin-top: 1em; margin-bottom: 1em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
3</span></p></td>
<td><pre class="html"><code>&lt;h3&gt;Heading 3&lt;/h3&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p><span style="display: block; font-size: 1em; margin-top: 1.33em; margin-bottom: 1.33em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
4</span></p></td>
<td><pre class="html"><code>&lt;h4&gt;Heading 4&lt;/h4&gt;</code></pre></td>
</tr>
<tr class="odd">
<td><p><span style="display: block; font-size: .83em; margin-top: 1.67em; margin-bottom: 1.67em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
5</span></p></td>
<td><pre class="html"><code>&lt;h5&gt;Heading 5&lt;/h5&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p><span style="display: block; font-size: .67em; margin-top: 2.33em; margin-bottom: 2.33em; margin-left: 0; margin-right: 0; font-weight: bold;">Heading
6</span></p></td>
<td><pre class="html"><code>&lt;h6&gt;Heading 6&lt;/h6&gt;</code></pre></td>
</tr>
</tbody>
</table>

##### Text Formatting

<table>
<thead>
<tr class="header">
<th><p>Example</p></th>
<th><p>HTML</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>This is <strong>bold</strong> text</p></td>
<td><pre class="html"><code>&lt;b&gt;Bold&lt;/b&gt;</code></pre>
<p>or<br />
</p>
<pre class="html"><code>&lt;strong&gt;Strong&lt;/strong&gt;</code></pre></td>
<td><p>The HTML &lt;b&gt; is a physical tag used to simply make text
bold.<br />
<br />
The HTML &lt;strong&gt; tag is a semantic tag that is used to signify
that the text inside the tag is of higher importance. This is shown by
making the text bold.</p></td>
</tr>
<tr class="odd">
<td><p>This is <em>italicized</em> text</p></td>
<td><pre class="html"><code>&lt;i&gt;Italics&lt;/i&gt;</code></pre>
<p>or<br />
</p>
<pre class="html"><code>&lt;em&gt;Emphasis&lt;/em&gt;</code></pre></td>
<td><p>The HTML &lt;i&gt; tag is a physical tag used to make the text
italic. It is used to indicate foreign text, scientific nomenclature,
thoughts, etc.<br />
<br />
The HTML &lt;em&gt; tag is a semantic tag that is used to signify that
the text inside the tag is being emphasized. It is a semantic tag as
opposed to &lt;i&gt; which doesn't hold any semantic meaning.</p></td>
</tr>
<tr class="even">
<td><p>This is <strong><em>bold and italicized</em></strong>
text</p></td>
<td><pre class="html"><code>&lt;b&gt;&lt;i&gt;bold and italicized&lt;i/&gt;&lt;/b&gt;</code></pre>
<p><br />
<br />
or<br />
<br />
</p>
<pre class="html"><code>&lt;i&gt;&lt;b&gt;bold and italicized&lt;b/&gt;&lt;/i&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>This is <sup>superscript</sup> text</p></td>
<td><pre class="html"><code>&lt;sup&gt;superscript&lt;/sup&gt;</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td><p>This is <sub>subscript</sub> text</p></td>
<td><pre class="html"><code>&lt;sub&gt;subscript&lt;/sub&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>This is <big>big</big> text</p></td>
<td><pre class="html"><code>&lt;big&gt;big&lt;/big&gt;</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td><p>This is <small>small</small> text</p></td>
<td><pre class="html"><code>&lt;small&gt;small&lt;/small&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>This is <u>underlined</u> text</p></td>
<td><pre class="html"><code>&lt;u&gt;underlined&lt;/u&gt;</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td><p>This is <mark>highlighted</mark> text</p></td>
<td><pre class="html"><code>&lt;mark&gt;highlighted&lt;/mark&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>This is <del>deleted</del> text</p></td>
<td><pre class="html"><code>&lt;del&gt;deleted&lt;/del&gt;</code></pre></td>
<td><p>The HTML &lt;del&gt; tag is a semantic tag used to represent that
the text is deleted or changed.</p></td>
</tr>
<tr class="even">
<td><p>This is <del>insreted</del><ins>inserted</ins> text</p></td>
<td><pre class="html"><code>&lt;ins&gt;inserted&lt;/ins&gt;</code></pre></td>
<td><p>The HTML &lt;ins&gt; tag is a semantic tag used to represent that
the text has been inserted in the document. The &lt;ins&gt; tag
generally follows some deleted text.</p></td>
</tr>
</tbody>
</table>

##### Lists

#### Learning Resources

There are a plethora of free and paid resources for learning HTML and
CSS on the internet, in a variety of formats. Depending on how you
learn, you may prefer hard documentation, or maybe a video to guide you
along the process.

Here are some free resources you can try:

**HTML:**

-   [Programiz](https://www.programiz.com/html) (Easy to understand)
-   [W3Schools](https://www.w3schools.com/html/default.asp)

**CSS:**

-   [W3Schools](https://www.w3schools.com/css/default.asp)

**JavaScript:**

-   [freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)
    (Interactive)
-   [W3Schools](https://www.w3schools.com/js/default.asp)

**Multiple**:

-   [Mozilla
    docs](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)
    (HTML, CSS, and JavaScript. Comprehensive, but can be hard to follow
    for beginners)
-   [freeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
    (Interactive) (HTML and CSS only)

## The End

You're finished! B