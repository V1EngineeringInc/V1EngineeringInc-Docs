# mkdocs Information

For full documentation visit [mkdocs.org](http://mkdocs.org).

A good markdown cheatsheet is available [here](https://www.markdownguide.org/cheat-sheet). The complete syntax is available
[here](https://daringfireball.net/projects/markdown/)

## Creating Links

Here's a link to the forums:

[V1Engineering Forum Link](https://www.v1engineering.com/forum/topic/community-documentation/)

Here's a link to another page in the documentation:

[About link](pg1.md)

Here's a link to a specific section in the documentation:

[About link subsection link](pg1.md#nautae-laeva)

## Images

!!! note
    It's preferable to use the syntax in [Image Resizing](#image-resizing) to this basic syntax for
    the v1 instructions.

If the image is on v1engineering.com, and it's the right size, then it can be placed here with
markdown like this:

```markdown
![Backup Text](imageLocation "Hover text")
```

![V1Engineering.com's logo](https://www.v1engineering.com/wp-content/uploads/2017/12/V1-Engineering-logo-260wide.png "This logo is linked from v1engineering.com")

If the image is something you want to share, and it's the right size, then it can be added to the
docs/media folder and linked like this:

```markdown
![Backup Text](media/filename.png "Hover text")
```

![images image](media/pic.png "This is linked here in this github")


### Image Resizing

In these instructions, it's helpful to allow a really big image to see detail. But also only show a
smaller version, to show the overview. To accomplish this, we want the images to be big in their
original format, and then smaller in the documentation. Then, when the user clicks the image, they
should get a bigger view.

Using these features is done like this:

```
![!Backup Text](imageLocation "Hover text"){: width="400" }
```

Notice the extra `!` in the `[]` brackets. That makes this a link to the image. Notice also the
`{: width="400" }`. That adds attributes to the image, and width limits the size, without changing
the aspect ratio. You can also add `height=""` and set the height.

![!Example Picture](media/pic.png){: width="400" }

![!Example Picture](media/pic.png){: width="400" height="100" }

## Organization

Documentation can be found at
[mkdocs.org](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation)

mkdocs 0.16.0 was too old for the nav tag. The 1.0 version works though.

The organization is in the `nav` section of [mkdocs.yml](https://github.com/V1EngineeringInc/V1EngineeringInc-Docs/blob/master/mkdocs.yml), 
and nesting more than two is funky. Also, top levels can't be pages, so it's really more like just two deep.

 - style/css/theme.

 - DONE. CC-BY-SA info in the pages.

## Bonus stuff

### Embed videos

Doesn't seem to work :(

[[embed url=http://www.youtube.com/watch?v=6YbBmqUnoQM]]

[!embed](https://www.youtube.com/watch?v=vq2jYFZVMDA)

Raw html works:

<iframe width="560" height="315" src="https://www.youtube.com/embed/xIGre_E2_og"
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

You can get this html by clicking the share button on a video, then clicking the `<>` symbol.

### Emojis?

:smile:

Nope. :(

### Tables

This helps a lot: [Table Generator](https://www.tablesgenerator.com/markdown_tables#)

    | Tables      |      Are      |  Cool |
    |-------------|:-------------:|------:|
    | col 1 is    |  left-aligned | $1600 |
    | col 2 is    |    centered   |   $12 |
    | column 3 is | right-aligned |    $1 |

| Tables      |      Are      |  Cool |
|-------------|:-------------:|------:|
| col 1 is    |  left-aligned | $1600 |
| col 2 is    |    centered   |   $12 |
| column 3 is | right-aligned |    $1 |

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs gh-deploy` - Deploy the docs to github pages.
* `mkdocs help` - Print this help message.

## Installing dependencies

Since this no longer only requires mkdocs as a dependency, there is a requirements.txt.

To make sure you have the requirements, and you're trying to build the docs on your computer, you
can do this:

    pip install -r requirements.txt

I recommend doing this in a virtualenv environment, which will let you easily remove the things
you've installed if you've made a mistake.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
