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

This markdown doesn't support size hints (that I could find). But you can put basic html into
markdown, so if you have an image and you need it to be a certain size, I found this works:

```html
<img src="../media/filename.png" width="400" height="320"/>
```

The `height` is optional, and if you omit it, it will keep the original aspect ratio.

The `src` might need a '../' if this isn't the main page.

<img src="../media/pic.png" width="400"/>

<img src="../media/pic.png" width="400" height="120"/>

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

    | Tables   |      Are      |  Cool |
    |----------|:-------------:|------:|
    | col 1 is |  left-aligned | $1600 |
    | col 2 is |    centered   |   $12 |
    | col 3 is | right-aligned |    $1 |

For some reason, the style is all messed up here.

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

### Favicon

TODO: https://www.mkdocs.org/#changing-the-favicon-icon

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs gh-deploy` - Deploy the docs to github pages.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
