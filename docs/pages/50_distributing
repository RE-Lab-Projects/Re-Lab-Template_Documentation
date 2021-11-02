Distributing via PyPI (pip)
===========================

This should be done once the project is ready to be installed and then again for every release.

Instructions
------------

Everytime you upload a new version to PyPi you have to increase the version number in the setup.py file beforehand! 

1. If you want to share the project with users you might want them to be able to easily install the software. Here are the necessary steps:
	The pip installation will automatically add all python-files and all files specified in package_data and data_files in setup() arguments in the setup.py, as well
	as the README and pyproject.toml. If you need to include other files create a new file 'MANIFEST.in' in the project root folder and refer to the `official guidelines <https://packaging.python.org/guides/using-manifest-in/#using-manifest-in>`_ 
	on how to add these files.

2. From the project root directory run:
	| (Linux)		python3 -m build
	| (Windows)	py -m build

	There should now be a 'dist' directory with two files in it.

3. Upload (you still need to be in the project root folder)
	| (Linux)		python3 -m twine upload dist/*
	| (Windows)	py -m twine upload dist/*
	Enter the credentials. There is a RE-Lab account for PyPI.

4. Done. 
	You can now install the package:
	pip install package-name

Further reading
===============

A more in-depth tutorial can be found on the `official documentation <https://packaging.python.org/tutorials/packaging-projects/>`_