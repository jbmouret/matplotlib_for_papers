Creating publication-quality with Python and Matplotlib
=======================================================

Author: Jean-Baptiste Mouret (mouret@isir.upmc.fr)

This repository contains the handout (and the source of the handout) for the tutorial "Creating publication-quality with Python and Matplotlib", give at the [Alife 2014 conference](http://blogs.cornell.edu/alife14nyc/).

Any contribution to make this tutorial better is welcomed: feel free to clone and send pull requests.

You can access to the handout [here]( http://htmlpreview.github.com/?https://github.com/jbmouret/matplotlib_for_papers/blob/master/matplotlib.html).

The main source is [here](matplotlib.rst) (github interprets the rst).

This is a [docutils](http://docutils.sourceforge.net/) document, written in [reStructuredText](http://docutils.sourceforge.net/rst.html). To generate a html version:

```
rst2html.py --syntax-highlight=short --stylesheet=dana.css,style.css matplotlib.rst > matplotlib.html
```

 