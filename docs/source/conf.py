import numpy
import os
import sys
from importlib.metadata import version

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dyson Equalizer'
copyright = '2024, Boris Landa, Francesco Strino, Yuval Kluger'
author = 'Boris Landa, Francesco Strino, Yuval Kluger'

# scm version (https://pypi.org/project/setuptools-scm/7.0.5/)
release_scm = version('dyson-equalizer')
release = '.'.join(release_scm.split('.')[:3])
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
    'numpydoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'matplotlib.sphinxext.plot_directive',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_context = {
    "default_mode": "light",
    "github_user": "KlugerLab",
    "github_repo": "DysonEqualizer",
    "github_version": "main",
    "doc_path": "docs",
}

html_sidebars = {
    "examples": []
}

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/KlugerLab/DysonEqualizer",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
    ],
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
}

plot_include_source = True
