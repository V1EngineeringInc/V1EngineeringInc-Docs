Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Download-URL: https://pypi.python.org/pypi/pyembed/
Description: PyEmbed
        =======
        
        .. image:: https://secure.travis-ci.org/pyembed/pyembed.png?branch=master
          :target: http://travis-ci.org/pyembed/pyembed
        .. image:: https://coveralls.io/repos/pyembed/pyembed/badge.png
          :target: https://coveralls.io/r/pyembed/pyembed
        .. image:: https://pypip.in/d/pyembed/badge.png
          :target: https://pypi.python.org/pypi/pyembed/
        .. image:: https://pypip.in/v/pyembed/badge.png
          :target: https://pypi.python.org/pypi/pyembed/
        .. image:: https://pypip.in/wheel/pyembed/badge.png
          :target: https://pypi.python.org/pypi/pyembed/
        .. image:: https://pypip.in/egg/pyembed/badge.png
          :target: https://pypi.python.org/pypi/pyembed/
        .. image:: https://pypip.in/license/pyembed/badge.png
          :target: https://pypi.python.org/pypi/pyembed/
        
        `OEmbed`_ consumer library for Python with automatic discovery of
        producers.
        
        PyEmbed allows you to easily embed content on your website from a wide
        variety of producers (including `Flickr`_, `Twitter`_ and `YouTube`_).
        Unlike many OEmbed consumers, you don't need to configure each producer
        that you want to use - PyEmbed discovers the configuration automatically.
        
        You just need to provide the URL, and PyEmbed will generate a block of
        HTML, ready for you to include in your page:
        
        ::
        
            >>> from pyembed.core import PyEmbed
            >>> html = PyEmbed().embed('http://www.youtube.com/watch?v=9bZkp7q19f0')
            <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>
        
        There are plugins for embedding content into `Markdown`_ and 
        `reStructuredText`_ documents, and for customizing embeddings with `Jinja2`_
        and `Mustache`_ templates.  For more information, see the `PyEmbed`_ website.
        
        Compatibility
        -------------
        
        PyEmbed has been tested with Python 2.7 and 3.3.
        
        Installation
        ------------
        
        PyEmbed can be installed using pip:
        
        ::
        
            pip install pyembed
        
        Contributing
        ------------
        
        To report an issue, request an enhancement, or contribute a patch, go to
        the PyEmbed `GitHub`_ page.
        
        License
        -------
        
        PyEmbed is distributed under the MIT license.
        
        ::
        
            Copyright (c) 2013 Matt Thomson
        
            Permission is hereby granted, free of charge, to any person obtaining
            a copy of this software and associated documentation files (the
            "Software"), to deal in the Software without restriction, including
            without limitation the rights to use, copy, modify, merge, publish,
            distribute, sublicense, and/or sell copies of the Software, and to
            permit persons to whom the Software is furnished to do so, subject to
            the following conditions:
        
            The above copyright notice and this permission notice shall be
            included in all copies or substantial portions of the Software.
        
            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
            EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
            MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
            NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
            LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
            OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
            WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        
        .. _OEmbed: http://oembed.com
        .. _Flickr: http://flickr.com
        .. _Twitter: http://twitter.com
        .. _YouTube: http://youtube.com
        .. _Markdown: https://pypi.python.org/pypi/pyembed-markdown
        .. _reStructuredText: https://pypi.python.org/pypi/pyembed-rst
        .. _Jinja2: https://pypi.python.org/pypi/pyembed-jinja2
        .. _Mustache: https://pypi.python.org/pypi/pyembed-mustache
        .. _PyEmbed: http://pyembed.github.io
        .. _GitHub: https://github.com/pyembed/pyembed
        
        .. :changelog:
        
        Changes
        =======
        
        v1.3.3, 2016-04-16
        ------------------
        
        Bug fixes:
        
        - #62: Add explicit scheme for YouTube.
        
        v1.3.1, 2015-11-19
        ------------------
        
        Bug fixes:
        
        - #61: Handle downtime of provider list.
        
        v1.3.0, 2015-09-05
        ------------------
        
        Enhancements:
        
        - #59: Reorder discovery.
        
        v1.2.3, 2015-08-27
        ------------------
        
        Bug fixes:
        
        - #53: Don't hit provider list until necessary.
        
        v1.2.2, 2015-08-15
        ------------------
        
        Bug fixes:
        
        - #51: Fix other Beautiful Soup warning
        
        v1.2.1, 2015-08-15
        ------------------
        
        Bug fixes:
        
        - #50: Specify Beautiful Soup parser
        
        v1.2.0, 2015-08-12
        ------------------
        
        Enhancements:
        
        - #48: Use official list of providers
        
        v1.1.2, 2015-01-03
        ------------------
        
        Enhancements:
        
        - #44: Allow overriding of default templates by subclassing.
        
        v1.1.1, 2014-09-02
        ------------------
        
        Bug fixes:
        
        - #42: Error embedding from SoundCloud.
        
        v1.1.0, 2014-08-02
        ------------------
        
        Enhancements:
        
        - #40: Add support for providers that do not have discovery enabled.
        
        v1.0.0, 2014-02-05
        ------------------
        
        Initial stable release
        
        v0.7.0, 2014-01-20
        ------------------
        
        Breaking changes:
        
        - The `pyembed.core.consumer.embed` method has been removed.  Instead, call
          `embed` on the `pyembed.core.PyEmbed` class.
        
        v0.6.1, 2014-01-11
        ------------------
        
        Bug fixes:
        
        - #36: Failure to handle relative OEmbed URLs
        
        v0.6.0, 2014-01-01
        ------------------
        
        Breaking changes:
        
        - The option to provide Mustache templates for rendering has been removed. It
          will be restored in a new pyembed-mustache module.
        
        Enhancements:
        
        - #33: Make rendering engines pluggable
        
        v0.5.0, 2014-01-01
        ------------------
        
        Breaking changes:
        
        - The ``rembed`` package has been renamed to ``pyembed``.
        
        Enhancements:
        
        - #30: Rename to PyEmbed
        
        v0.4.3, 2013-12-29
        ------------------
        
        Rebuilt due to error in deployment process.  No functional changes.
        
        v0.4.2, 2013-12-29
        ------------------
        
        Rebuilt due to error in deployment process.  No functional changes.
        
        v0.4.1, 2013-12-29
        ------------------
        
        Rebuilt due to error in deployment process.  No functional changes.
        
        v0.4.0, 2013-12-29
        ------------------
        
        Enhancements:
        
        - #5: More control over embedding format
        
        v0.3.0, 2013-08-03
        ------------------
        
        Breaking changes:
        
        - The ``rembed`` package has been renamed to ``rembed.core``.
        
        Enhancements:
        
        - #19: Make rembed into a namespace package
        
        v0.2.2, 2013-08-03
        ------------------
        
        Enhancements:
        
        - #20: Add code coverage to build
        - #21: Add static analysis to build
        
        v0.2.1, 2013-08-02
        ------------------
        
        Bug fixes:
        
        - #17: Classifiers not shown in PyPI
        
        v0.2.0, 2013-07-30
        ------------------
        
        Enhancements:
        
        - #3: Support Python 3
        - #4: Add maxheight and maxwidth parameters
        - #10: Improve PyPI package entry
        
        Bug fixes:
        
        - #9: Tidy up requirements duplication
        
        v0.1.1, 2013-07-29
        ------------------
        
        Bug fixes:
        
        - #6: Package fails to install
        
        v0.1.0, 2013-07-29
        ------------------
        
        Initial release
        
Platform: UNKNOWN
Classifier: Development Status :: 5 - Production/Stable
Classifier: Intended Audience :: Developers
Classifier: Natural Language :: English
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python
Classifier: Programming Language :: Python :: 2
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.3
Classifier: Topic :: Text Processing
Provides: pyembed.core
