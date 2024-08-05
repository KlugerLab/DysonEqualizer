import numpy
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dyson Equalizer'
copyright = '2024, Boris Landa, Francesco Strino, Yuval Kluger'
author = 'Boris Landa, Francesco Strino, Yuval Kluger'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'numpydoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.graphviz',
    # 'sphinx.ext.ifconfig',
    # 'matplotlib.sphinxext.plot_directive',
    # 'IPython.sphinxext.ipython_console_highlighting',
    # 'IPython.sphinxext.ipython_directive',
    'sphinx.ext.imgmath',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_context = {
    "default_mode": "light",
}
