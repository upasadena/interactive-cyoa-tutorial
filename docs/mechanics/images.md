---
comments: true
---

# Images
Images are quite easy to add in this Creator, and we'll be going through how to
insert them.

!!! tip

    It is advisable that you do not upload images until the core mechanics of 
    the CYOA are complete. The vast majority of space that an Interactive CYOA 
    takes up is due to images, and a huge amount of images will slow down lower
    end PCs. CYOAs over 300 MB are known to have caused issues.

## Adding Images
To add an image to any compatible object, simply press the **Change Image**
button.

Don't worry about the Image Upload menu for now, we'll
[get into that later](#image-upload-menu).

The specifics for each compatible object and examples are detailed below.

### Adding to Rows
=== "Result (no styling)"

    ![](../images/76_added_row_image.png)

=== "Process"

    ![](../images/76_adding_row_image_process.gif)

### Adding to Choices
=== "Result (no styling)"

    ![](../images/77_added_choice_image.png)

=== "Process"

    ![](../images/77_adding_choice_image_process.gif)

### Adding to Addons
=== "Result (no styling)"

    ![](../images/78_added_addon_image.png)

=== "Process"

    ![](../images/78_adding_addon_image_process.gif)

### (TODO LINK) Adding to Backgrounds
Adding images to the Background, Row Backgrounds, and Object Backgrounds is
covered in the [Styling](../styling/) section.

## Removing Images
To remove images, simply press the **Remove Photo** button.

!!! warning

    The creator does not warn you when removing photos, so remain cautious
    around the button.

![](../images/83_remove_photo.png)

## The Image Menu
This is the Image menu. It is where you will upload your images and assign them
to Rows, Choices, Addons, and so on.

![](../images/79_upload_image_menu.png)

### Uploaded Image or External URL
This switch allows you to switch between uploading the image yourself (directly
into the .json file) or using one already on the internet.

Why you would want to use one or the other is covered later
[here](#local-vs-external-images).

=== "Uploaded Image"

    ![](../images/80_uploaded_image.png)

=== "External URL"

    ![](../images/80_external_url.png)

#### External Image URL
This only shows when the above switch is switched on. Put the URL of the
external image that you wanted to show here.

!!! note

    Unlike uploaded "local" images, external images cannot be altered. This
    means they cannot be cropped, compressed, nor have a tooltip.

### Tooltip That Shows When Hovering over it
This input field allows you to assign a
[tooltip](#tooltip-that-shows-when-hovering-over-it "like this!") on an image.

!!! tip

    If you wanted to give credit to artists' photos, here would be a great
    place to put it. That way, anyone wanting to know a specific image's artist
    would be able to tell the source of any image they hover over.

![](../images/81_tooltip.png "you hovered over me :3")

---

=== "Result"

    ![](../images/81_tooltip_result.png)

=== "Process"

    ![](../images/81_tooltip_process.gif)

### Cropper
The **Cropper** section allows you to crop your photos.

To crop an image, simply drag the borders around and press the **Crop Image**
button at the very top.

You can zoom in and out of the image by using the scroll wheel on your mouse.

When zoomed in, move the crop placement by dragging on the inside of the
borders. Move the image by dragging on the outside of the borders.

You cannot, however, rotate images.

![](../images/82_cropper_compressed.gif)

### Aspect Ratios
The **Width** and **Height Aspects** along with the **Change Aspect** button
allow you to change the Aspect Ratio of your images.

If you don't know what Aspect Ratios are, you can read about them
[here](https://en.wikipedia.org/wiki/Aspect_ratio_(image)).

These are useful for consistent image sizes between images used across the
CYOA.

!!! tip

    In order for a more uniform and orderly appearance, it is **highly**
    recommended you crop all of your images according to a specific
    aspect ratio and/or size.

    See the difference below:

    === "Cropped (1:1)"

        ![](../images/84_cropped.png)

    === "Full"

        ![](../images/84_uncropped.png)

You can change the Aspect Ratio by inputting the desired Aspect Ratio in the
**Width** and **Height** fields, before pressing **Change Aspect**. Afterward,
crop the image as usual.

![](../images/85_aspect_process.gif)

### Compress
Compressing images is very helpful if your CYOA is taking up too much space, as
the majority of space in the CYOA is taken up by local images.

You can switch to the Compress menu by pressing the **Compress** button up by
the **Cropper** button. These are tabs, and pressing one or the other allows
you to go back and forth.

![](../images/86_switch_to_compress.gif)

#### Compressing an Image

##### Image Scale

##### Image Quality

#### Compressing all Images
Compressing **all** images requires a different method, however. It is not
found in 

## Local vs External Images
There are pros and cons to using both local and external images. What you
choose should depend on your use case.

| Upload type  | Pros                                            | Cons                                                                                                                  | Use case                   |
| ------------ | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Local**    | + Faster<br>+ More reliable<br>+ Can be altered | - Takes up space (too much space can crash the creator, and most free website hosts limit how much space you can use) | Smaller projects (<300 MB) |
| **External** | + You keep the size of your project.json down   | - Slower<br>- You have to trust the servers won't delete the image<br>- Unable to be altered                          | Larger projects (>300 MB)  |

!!! tip

    You do not have to commit to one or the other. Sometimes, it's enough to
    just externally host large images and keep the rest locally.

## Local images
Local images are images they you have uploaded directly into the Creator.

## External images
External images are images they you have provided the Creator a link for.
Whenever someone plays your CYOA, it will download it from that site from their
computer.

### Image host sites
Here are a list of sites that you can host your external images on. Feel free
to provide suggestions in the comments below.

!!! warning 

    Keep in mind that your images should follow a host's terms and conditions
    in order to not have the image removed.

    This means be extra cautious when uploading NSFW images. If you can, prefer
    to keep them local. If you absolutely cannot, pick a host that allows
    NSFW images.

Public:

* [Imgur](https://imgur.com)

Private:

* [Discord](https://discord.com) (open image preview → Open in Browser to get 
the link)

## (TODO) Templates/Image Position
See [a](b). 
<!-- Link other place -->

## Image Compression
