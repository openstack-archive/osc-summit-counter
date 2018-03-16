========================
OpenStack Summit Counter
========================

The ``summit count`` plugin for python-openstackclient helps the user
determine the number of summits they have attended since the beginning
of their interaction with OpenStack.

Installing
==========

::

  $ pip install openstack-summit-counter

Using
=====

::

  $ openstack summit count $first [$current]

For example, if your first summit was for the "Folsom" series and the
next summit is for "Rocky"::

  $ openstack summit count folsom rocky

  +---------+-------+
  | Field   | Value |
  +---------+-------+
  | Summits | 13    |
  +---------+-------+
