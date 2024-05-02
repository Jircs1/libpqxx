# -*- coding: utf-8 -*-
"""
libpqxx documentation build configuration file, created by
sphinx-quickstart on Sun Dec  3 00:43:33 2017.

This file is execfile()d with the current directory set to its containing dir.

All configuration values have a default; values that are commented out serve
to show the default.
"""

import os
from pathlib import Path
from subprocess import check_call
import sys


source_dir = Path(__file__).parents[1].absolute()
build_dir = Path.cwd().parent.absolute()


# Trying this as a way to get myst_parser extension working.
sys.path.append(Path.cwd().parent)


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, make it absolute, like shown here.
sys.path.insert(0, source_dir)


def recursive_dir(path, relative_to):
    """List all files in `path`, as relative paths from `relative_to`."""
    path = os.path.normpath(path)
    relative_to = os.path.normpath(relative_to)
    files = []
    for dirpath, _, filenames in os.walk(path):
        local = os.path.samefile(dirpath, relative_to)
        reldir = os.path.relpath(dirpath, relative_to)
        for filename in filenames:
            filename = os.path.normpath(filename)
            if not filename.startswith('.'):
                if local:
                    relative = filename
                else:
                    relative = os.path.join(reldir, filename)
                files.append(relative)
    return files


breathe_projects = {
    'libpqxx': (build_dir / 'doc'),
}
breathe_projects_source = {
    'libpqxx': (
        source_dir,
        (
            recursive_dir(source_dir / 'src', source_dir) +
	    recursive_dir(source_dir / 'include/pqxx', source_dir)
        )
    ),
}
breathe_default_project = 'libpqxx'


breathe_implementation_filename_extensions = ['.cxx']


if os.environ.get('READTHEDOCS') == 'True':
    # C++23: Upgrade C++ version.
    check_call(
        [source_dir / 'configure', 'CXXFLAGS=-std=c++20 -O0'], cwd=build_dir)
    check_call('doxygen', cwd=(build_dir / 'doc'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    'sphinx.ext.autodoc',
#    ]
extensions = ['breathe', 'myst_parser']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = '.rst'
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'libpqxx'
copyright = u'2000-2024, Jeroen T. Vermeulen'
author = u'Jeroen T. Vermeulen'


def read_version():
    """Return version number as specified in the VERSION file."""
    return (Path(__file__).parents[1] / 'VERSION').read_text().strip()


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = read_version()

# The short X.Y version.
version = '.'.join(release.split('.')[:2])

html_title = "libpqxx %s" % release
html_short_title = "libpqxx"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# Looks like the setup is that our build generates the HTML itself, and then
# has readthedocs copy the full generated HTML tree to the output directory.
#
# Problem is, that doesn't seem to be working now.  This needs debugging.
#html_extra_path = [
#    str(Path(os.environ.get("READTHEDOCS_OUTPUT", '.')) / "html")
#]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'libpqxxdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'libpqxx.tex',
        u'libpqxx Documentation',
        u'Jeroen T. Vermeulen',
        'manual',
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'libpqxx', u'libpqxx Documentation', [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'libpqxx', u'libpqxx Documentation',
     author, 'libpqxx', "C++ client API for PostgreSQL.",
     'Miscellaneous'),
]
