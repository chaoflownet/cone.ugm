cone.ugm
========

Manage Users and Groups in LDAP via Web Interface.


Getting started
===============

Installation
------------

Clone UGM repository::

    $ git clone git://github.com/chaoflownet/cone.ugm.git

    $ cd cone.ugm

Run bootstrap and buildout::

    cone.ugm$ python2.6 bootstrap.py -c anon.cfg

    cone.ugm$ ./bin/buildout -c anon.cfg

There are dependencies to compile openldap, in case of a debian-based
system: libsasl2-dev, libssl-dev and libdb-dev.

Start Test Application::

    cone.ugm$ ./bin/testldap start groupOfNames_100_100

    cone.ugm$ ./bin/paster serve ugm.ini

Point your browser to 127.0.0.1:8081 and log in with admin:admin.


Contributors
============

- Robert Niederreiter <rnix@squarewave.at>

- Florian Friesdorf <flo@chaoflow.net>
