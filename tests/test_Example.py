"""
Test class. Run pytest from project root folder.
Take a look at the `example <https://github.com/RE-Lab-Projects/Re-Lab-Template_Documentation/tree/main/tests>`_ in our github repository.
"""

from src import example as e


def test_exponentiate():
	assert e.exponentiate(1,1) == 1
	assert e.exponentiate(1,2) == 1
	assert e.exponentiate(2,2) == 4
	assert e.exponentiate(3,3) == 27
	assert e.exponentiate(10,10) == 10000000000
	assert e.exponentiate(1,0) == 1
	assert e.exponentiate(2,0) == 1
