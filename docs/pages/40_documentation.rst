Generating documentation
========================

Manual documentation
--------------------

Folders and files
^^^^^^^^^^^^^^^^^

Navigate to the docs/pages directory. This folder should contain all the rst-files you create. You can freely create as many as you want and they will be added to the documentation automatically.
The files will appear in the left-hand table ordered alphabetically by their filename. Note that the filename of the rst-file is not the title shown in the documentation, but the title in the first line of the files is.
This means you can name your files like "1_introduction.rst", "2_example.rst" and "3_final_thoughts.rst" for forcing a sensible order.

Syntax
^^^^^^

To learn the syntax take a look at the `official documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ or take a look at the example files provided.

Minimum requirements
^^^^^^^^^^^^^^^^^^^^

Projects released as a RE-Lab-project should at least have:

* An introduction page
* An example page showing how to run the program or how to make API calls
* The AutoDoc

AutoDoc
-------

AutoDoc uses the DocStrings from the py-files to generate class and function documentation.
Use propper DocStrings and the documentation is done automatically.

A DocString should at least have a description of what it does and what it returns. Take a look at our `example <https://github.com/RE-Lab-Projects/Re-Lab-Template_Documentation/tree/main/tests>`_ .

More information about `DocString <https://www.python.org/dev/peps/pep-0257/>`_

Makefile
--------

Use the makefile (Linux) or make.bat (Windows) to start documentation generation. Just start it.

You can now open docs/_build/html/index.html to verify everything is in order.

Uploading to readthedocs
------------------------
Make sure you pushed your changes to the repository. Log in to readthedocs.org and go to 'my projects'. Hit the refresh icon if the right repository is not in the list. Select the repository and follow the instrcutions.