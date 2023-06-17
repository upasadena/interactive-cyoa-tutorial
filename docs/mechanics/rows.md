# Rows
The basic building block of Interactive CYOAs made with this creator is the 
Row. Rows are not only the sections that divide the CYOA up, but it is only 
attached to a Row where Objects can exist. 

## Creating Rows
Create a Row by opening up the sidebar and pressing _Create New Row_.

![](../images/1_creating_a_row.gif)

## Cloning Rows
!!! note ""

    ![](../images/2_clone_button.png){ align=left }
    To clone or copy a Row, press this button.

    Cloning rows can be useful when you have [private styling] or a specific
    set of choices you need to repeat. 

![](../images/3_clone_row.gif)

## Deleting Rows
!!! note ""

    ![](../images/4_delete_button.png){ align=left }

    To delete a Row, press this button, and then _OK_.

![](../images/5_delete_row.gif)

## Editing a Row
!!! note ""

    ![](../images/6_edit_row.png){ align=left }
    To edit a row, press the wrench/spanner icon.

    This will open the edit menu for the row. 

![](../images/7_edit_row.gif)

## Row Title
By default, the row title will be **Row**.

As Rows are generally sections (such as Powers, Perks, Drawbacks, etc), you 
should name your Row after what the Objects represent.

To edit the Row Title, simply edit the text in the **Row Title** section.

![](../images/8_row_title.gif)

## Row Text
Row Text can be used to provide a description of the section.

You can also use it to provide notes specific to the section in particular,
such as informing the players that they can select only 1 option.

To edit the row text, simply edit the text in the **Row Text** section.

![](../images/9_row_text.gif)

## Allowed Choices
The _Allowed Choices_ options allows you to restrict the amount of choices a 
player can pick in that row. It takes a non-negative integer (anything above
zero).

If you want ANY number of options with no limits, simply put 0 into the field.

This is used for sections where you might say "You may only take X options".

There will be a way to dynamically change this amount, but we’ll come back to 
that later (to skip ahead, see [here][dynamic_allowed_choices]).

![](../images/10a_allowed_choices.png)

---

![](../images/10b_allowed_choices.gif)

## Selected Choices (Input)
The _Selected Choices_ field will show how many choices are currently selected, and 
should normally be 0. An exception would be choices that are selected by
default.

!!! danger

    **You should not change this value unless you know what you're doing.**

If it is something else and no choices are selected, then something has gone wrong. You can fix this by changing the value to 0.

![](../images/11_selected_choices.gif)

## Objects Per Row
The _Objects Per Row_ option allows you to determine how many Objects are
present within an Object row.

=== "1 per Row"

    ![](../images/13a_1_per_row.png)

=== "3 per Row"

    ![](../images/13b_3_per_row.png)

=== "4 per Row"

    ![](../images/13c_4_per_row.png)

### 'Row' Objects per Row
!!! note

    This section may get confusing for beginners, so feel free to skip ahead
    if you don't understand it.

    _Objects per Row_ – This is set within a Row's options

    _Object Width_ – This is set within an Object's options

Most **Objects per Row** options seem pretty straightforward, but this one in 
particular might get confusing. It is in fact not used by a Row (though
the option is bafflingly there), but is instead used for individual Objects'
**Object Width**.

To give context, individual Objects of a specific Object row (not referring to
the Row object, but an actual row—as opposed to column—of Objects) can set a 
custom **Object Width**, allowing further customization and deviance from a 
Row's **Object per Row** setting.

* For example, you can have one row have two Objects take up an entire row by
setting both of their **Object Widths** to **2 per Row**, and the next row
could have five Objects take up the entire row by setting their
**Object Widths** to **5 per Row**.

Objects have an **Object Width** of **Row** by default, and that means that 
their width is equal to whatever is set by the **Objects per Row**. This is 
convenient in that you don't need to go into each and every choice width and 
update it, instead only updating the **Objects per Row** once.

If you have changed an individual Object's **Object Width**, then setting back 
to **Row** resets it back to the default. 

## Non-Activatable?
This option can be used when you just want to supply information using Objects 
and don’t want those Objects to be selectable.

Objects are great for this because they allow you to split information into 
chunks, each with an image being able to be attatched.

!!! quote "Help and Instructions"

    The third button will make it impossible for a player to change any of the 
    choices, if one is selected then it will stay selected and vice versa. Good 
    to use when the user should be given information or story, and not choices.

![](../images/14_non_activatable.gif)

## Selected Choices? (Switch)
The **Selected Choices?** switch enables a whole host of other options that 
have to do with the Objects in the Row.

!!! quote "Help and Instructions"

    The middle button named 'Selected Choices?' can be used to make the row 
    show all choices that have been selected, good to use at the end of the 
    project to let the player see the choices they have made. A private row 
    design should be used to make filters invisible.

### Selected Choices from Group Id
### Deselect choices when Row lacks requirements?
### Choices will all be 'Template Top' and Row Width
### Remove the text of the choices
### Show the title of the row in the choice.

## Half of the Screen?

[private styling]: ../../styling/#private-styling
[dynamic_allowed_choices]: ../objects/adds-or-takes-away-a-rows-allowed-choices