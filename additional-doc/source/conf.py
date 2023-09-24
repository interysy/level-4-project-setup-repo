# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'String Search Algorithm Visualiser'
copyright = '2023, Michal Wozniak'
author = 'Michal Wozniak'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_js"]

templates_path = ['_templates']
exclude_patterns = []
 
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
} 
 
js_language = 'typescript' 
js_source_path = '../../src/myApp' 
primary_domain = 'js' 
entryPointStrategy =  "expand"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_static_path = ['_static' , 'dissertation']
