Viet Text Tools
===============

Functions for working with Vietnamese text

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install viet_text_tools

Usage
-----

normalize_diacritics()
~~~~~~~~~~~~~~~~~~~~~~

You can normalize diacritics for a Vietnamese word.  The return value is in composed (NFC) form

.. code-block:: python

    normalize_diacritics('nghìên') == 'nghiền'

Pass ``new_style=True`` to use new style tone placement

.. code-block:: python

    normalize_diacritics('thủy', new_style=True) == 'thuỷ'

Pass ``decomposed=True`` to return a string in decomposed (NFD) form

.. code-block:: python

    len(normalize_diacritics('thủy')) == 4
    len(normalize_diacritics('thủy', decomposed=True)) == 5

vietnamese_sort_key()
~~~~~~~~~~~~~~~~~~~~~

A key function for use with sorted() to sort Vietnamese text with the correct collation order

.. code-block:: python

    words = ['anh', 'ba', 'áo', 'cắt', 'cá', 'cả']
    sorted(words) == ['anh', 'ba', 'cá', 'cả', 'cắt', 'áo']
    sorted(words, key=vietnamese_sort_key) == ['anh', 'áo', 'ba', 'cả', 'cá', 'cắt']

vietnamese_case_insensitive_sort_key()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as `vietnamese_sort_key()` but case-insensitive.
