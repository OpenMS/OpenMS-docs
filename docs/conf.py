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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'OpenMS'
copyright = '2022, OpenMS Team'
author = 'OpenMS Team'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short major.minor.patch version.
version = '2.7.0'
# Short version for the latest supported KNIME
knime_version = '4.6.0'

# The full version, including alpha/beta/rc tags.
release = '2.7.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx_copybutton',
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'myst_parser',
  'notfound.extension',
  'sphinxcontrib.images',
  'sphinx_inline_tabs',
  'hoverxref.extension',
]

numfig = True

myst_enable_extensions = [
  "tasklist",
  "dollarmath",
  "amsmath",
  "colon_fence",
  "linkify",
  "replacements",
  "linkify_fuzzy_links",
  "html_admonition",
  "substitution",
]

autosummary_generate = True
autosummary_imported_members = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_favicon = 'assets/logo/OpenMS_transparent_background.png'
html_logo = '../assets/logo/OpenMS_transparent_background.png'
html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "font-stack--monospace": "Consolas, monospace",
        "font-size--small": "90%",
        "toc-font-size": "87.5%"
    },
}
pygments_style = 'sas'

pygments_dark_style = 'rrt'

# Configure tooltips
hoverxref_roles = ['term']

hoverxref_role_types = {'term':'tooltip'}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

html_css_files = [
    'css/custom.css',
]

root_doc = 'index'

variables_to_export = [
    "project",
    "version",
    "knime_version"
]
myst_substitutions = {}
for v in variables_to_export:
    myst_substitutions[v] = globals()[v]
frozen_locals = dict(locals())
# Makes variables_to_export available in the epilog
rst_epilog = '\n'.join(map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export))
del frozen_locals

