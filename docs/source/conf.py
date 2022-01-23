import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# -- Project information -----------------------------------------------------

project = 'django-easy-error'
copyright = '2022, FamilyTreeCollab'
author = 'FamilyTreeCollab'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_autodoc_typehints'
]

source_suffix = '.rst'
master_doc = 'index'
pygments_style = None

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = []
