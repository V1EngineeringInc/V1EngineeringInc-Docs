# Welcome to MkDocs

For full documentation visit [mkdocs.org](http://mkdocs.org).

 - DONE Pipeline figured out from .md files to webpage (github.io page).

 - DONE Some kind of images posted, and also images from v1engineering.com.

     ![V1Engineering.com's logo](https://www.v1engineering.com/wp-content/uploads/2017/12/V1-Engineering-logo-260wide.png
     "This logo is linked from v1engineering.com")

     ![images image](media/pic.png "This is linked here in this github")

 - DONE Image resizing.

     - I found there are some unofficial syntaxes to get images to resize, but they don't seem to
         work here. Maybe there's a python-markdown plugin? But that will bring it's own can of
         worms. Just using an img tag seems to work though. [More info](
         https://gist.github.com/uupaa/f77d2bcf4dc7a294d109 )

     <img src="media/pic.png" width="400" height="320"/>

     <img src="media/pic.png" width="400"/>

 - DONE Get links working in the documents to sections and pages and v1engineering.com

     [V1Engineering Forum Link](https://www.v1engineering.com/forum/topic/community-documentation/)

     [About link](about.md)

     [About link subsection link](about.md#nautae-laeva)

 - Menu organization, how deep.

   https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation

   This sort of works. I had to install a newer version of mkdocs (0.16 was too old).

   The organization is in mkdocs.yml, and nesting more than two is funky. Also, top levels can't be
   pages, so it's really more like just two deep. Maybe another theme would help?

 - style/css/theme.

 - DONE. CC-BY-SA info in the pages.

## Bonus stuff

 - Embed videos

     Doesn't seem to work :(

     [[embed url=http://www.youtube.com/watch?v=6YbBmqUnoQM]]

     [!embed](https://www.youtube.com/watch?v=vq2jYFZVMDA)

 - Emojis?

     :smile:

 - Tables

     This helps a lot: https://www.tablesgenerator.com/markdown_tables#

    | Tables   |      Are      |  Cool |
    |----------|:-------------:|------:|
    | col 1 is |  left-aligned | $1600 |
    | col 2 is |    centered   |   $12 |
    | col 3 is | right-aligned |    $1 |


 - Favicon: https://www.mkdocs.org/#changing-the-favicon-icon

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
