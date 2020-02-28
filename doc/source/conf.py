# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import icepyx


# -- Project information -----------------------------------------------------

project = 'icepyx'
copyright = '2020, Jessica Scheick, Anthony Arendt, Lindsey Heagy, Fernando Perez, Amy Steiker, Raphael Hagen'
author = 'Jessica Scheick, Anthony Arendt, Lindsey Heagy, Fernando Perez, Amy Steiker, Raphael Hagen'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    'sphinx_gallery.gen_gallery',
    "numpydoc",
    "nbsphinx"
]


sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'gallery',  # path to where to save gallery generated output
     'download_all_examples': False,
}






# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']
templates_path = ['_templates']

# location of master document (by default sphinx looks for contents.rst)
master_doc = 'index'


# -- Configuration options ---------------------------------------------------
autosummary_generate = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': None,
    'navigation_depth': 4,
    'collapse_navigation': True
}
html_logo = '_static/icepyx_logo.png'
html_favicon = '_static/icepyx_favicon.png'
html_static_path = ['_static']

html_context = {
    'menu_links_name': 'Outside Resources',
    'menu_links': [
        ('<i class="fa fa-comments fa-fw"></i> Pangeo Discourse', 'https://discourse.pangeo.io/t/icepyx-python-tools-for-icesat-2-data/404/2'),
        ('<i class="fa fa-archive fa-fw"></i> NSIDC Icesat-II Documentation', 'https://nsidc.org/data/icesat-2'),
        ('<i class="fa fa-github fa-fw"></i> Project Source Code', 'https://github.com/icesat2py/icepyx'),
        ('<i class="fa fa-gavel fa-fw"></i> Code of Conduct', 'https://github.com/icesat2py/icepyx/blob/master/code_of_conduct.md')
    ]
}


# html_title = 'Icepyx'
# html_short_title = 'Icepyx'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
