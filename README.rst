.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/keitaroinc/ckanext-purge.svg?branch=master
    :target: https://travis-ci.org/keitaroinc/ckanext-purge

.. image:: https://coveralls.io/repos/keitaroinc/ckanext-purge/badge.svg
  :target: https://coveralls.io/r/keitaroinc/ckanext-purge

.. image:: https://pypip.in/download/ckanext-purge/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-purge/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-purge/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-purge/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-purge/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-purge/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-purge/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-purge/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-purge/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-purge/
    :alt: License

=============
ckanext-purge
=============

A simple CKAN extension for purging datasets that are marked as deleted. 


------------
Requirements
------------

Requires CKAN 2.5+


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-purge:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-purge Python package into your virtual environment::

     pip install ckanext-purge

3. Add ``purge`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Command line interface
---------------

The following operations can be run from the command line using the
``paster --plugin=ckanext-purge purger`` command::

      purger showdeleted
        - Displays the datasets marked as deleted

      purger purgeall 
        - Purges all of the deleted datasets

    The commands should be run from the ckanext-purge directory and expect
    a development.ini file to be present. Most of the time you will
    specify the config explicitly though::

        paster purger purgeall --config=../ckan/development.ini



------------------------
Development Installation
------------------------

To install ckanext-purge for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/keitaroinc/ckanext-purge.git
    cd ckanext-purge
    python setup.py develop


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.purge --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-purge on PyPI
---------------------------------

ckanext-purge should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-purge. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-purge
----------------------------------------

ckanext-purge is availabe on PyPI as https://pypi.python.org/pypi/ckanext-purge.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
