version: 2

sphinx:
  configuration: docs/source/conf.py

python:
  version: "3.8"
  install:
    - requirements: docs/requirements.txt

formats:
  - pdf
  - epub# Configuration file for the Sphinx documentation builder.

project = 'Git Commands Guide'
copyright = '2023, Your Name'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Add any additional configuration options here
