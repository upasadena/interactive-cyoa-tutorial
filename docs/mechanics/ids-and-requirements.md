# IDs & Requirements

## IDs – Unique Identifiers
IDs are unique identifiers that allow the ICC to directly 
access any object, whether that be Rows, Objects, Points, or Groups.

They are particularly useful in situations where you have many choices that 
have requirements, meaning that if you assigned IDs according to regular, 
predictable rules, you would not need to contantly check for the IDs of those
Objects.

When you create any object, whether a Row, Choice, Point type, etc, they will 
be assigned a random 4-digit hex ID.

!!! warning

    It is **strongly** suggested that you change default IDs.

    If you do not, it makes it **incredibly difficult** to understand and 
    modify choice interactions.

    Start by making a sensible ID format that you can apply to **every** Row,
    Choice, Point, etc. This will make things **much** easier when the project
    starts getting large and convoluted, making the various interactions
    **much** easier to understand and track.[^1]

    An example of a format is:

    | Object type       | ID Format        | Example              |
    | ----------------- | ---------------- | -------------------- |
    | **Row**           | `row_{title}`    | `row_perks`          |
    | **Choice/Object** | `choice_{title}` | `choice_immortality` |
    | **Point type**    | `point_{title}`  | `point_companions`   |

## Requirements
Requirements are conditions that a Row must fulfil before it is shown and an
Object must fulfil before it can be selected.

### Adding Requirements
To add requirements to any object, press the icon that looks like a a key above
a plus sign. For Rows and Choices, you will have to enter their Edit menu
first.

=== "Rows"

    ![](../images/31a_add_row_requirement.gif)

=== "Choices"

    ![](../images/31b_add_choice_requirement.gif)

### Create Requirement Menu
The **Create Requirement** menu is the interface through which requirements are
added to objects.

![](../images/33_create_requirement.png)

#### Selected Choice
The _Selected choice_

#### Non-selected Choice
#### 'One of these is selected' requirement
#### 'None of these is selected' requirement
#### Doing multiple selected choices
#### Doing multiple non-selected choices

[^1]: [Tips and Pitfalls for Interactive CYOA Creators (Reddit)](https://www.reddit.com/r/InteractiveCYOA/comments/wrf0hl/tips_and_pitfalls_for_interactive_cyoa_creators/)