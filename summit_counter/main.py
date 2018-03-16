#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cliff import lister
from cliff import show

_SUMMITS = [
    ('Austin', 'Austin', 'https://wiki.openstack.org/wiki/Design_Summit/Austin'),
    ('Bexar', 'San Antonio', 'https://wiki.openstack.org/wiki/Design_Summit/Bexar'),
    ('Cactus', 'Santa Clara', ''),
    ('Diablo', '', ''),
    ('Essex', 'Boston', 'https://wiki.openstack.org/wiki/Design_Summit/Essex'),
    ('Folsom', 'San Francisco', 'https://wiki.openstack.org/wiki/Design_Summit/Folsom'),
    ('Grizzly', 'San Diego', 'https://wiki.openstack.org/wiki/Design_Summit/Grizzly'),
    ('Havana', 'Portland', 'https://wiki.openstack.org/wiki/Design_Summit/Havana'),
    ('Icehouse', 'Hong Kong', 'https://wiki.openstack.org/wiki/Design_Summit/Icehouse'),
    ('Juno', 'Atlanta', 'https://wiki.openstack.org/wiki/Design_Summit/Juno'),
    ('Kilo', 'Paris', 'https://wiki.openstack.org/wiki/Design_Summit/Kilo'),
    ('Liberty', 'Vancouver', 'https://wiki.openstack.org/wiki/Design_Summit/Liberty'),
    ('Mitaka', 'Tokyo', 'https://www.openstack.org/summit/tokyo-2015/'),
    ('Newton', 'Austin', 'https://wiki.openstack.org/wiki/Design_Summit/Newton'),
    ('Ocata', 'Barcelona', 'https://www.openstack.org/summit/barcelona-2016'),
    ('Pike', 'Boston', 'https://www.openstack.org/summit/boston-2017'),
    ('Queens', 'Sydney', 'https://www.openstack.org/summit/sydney-2017'),
    ('Rocky', 'Vancouver', 'https://www.openstack.org/summit/vancouver-2018'),
]


class SummitCount(show.ShowOne):

    # Set the command so that when we run through
    # python-openstackclient we do not require authentication.
    auth_required = False

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        choices = [s[0].lower() for s in _SUMMITS]
        parser.add_argument(
            'first',
            help='Your first summit',
            choices=choices,
        )
        parser.add_argument(
            'current',
            help='The current summit',
            choices=choices,
            nargs='?',
            default=choices[-1],
        )
        return parser

    def _name_to_num(self, name):
        return ord(name.lower()[0]) - ord('a') + 1

    def take_action(self, parsed_args):
        first = self._name_to_num(parsed_args.first)
        current = self._name_to_num(parsed_args.current)
        return (('Summits',), (current - first + 1,))


class SummitList(lister.Lister):

    # Set the command so that when we run through
    # python-openstackclient we do not require authentication.
    auth_required = False

    def take_action(self, parsed_args):
        columns = ('Number', 'Name', 'Location', 'URL')
        summits = []
        for i, s in enumerate(_SUMMITS, 1):
            summits.append((i,) + s)
        return (columns, summits)
