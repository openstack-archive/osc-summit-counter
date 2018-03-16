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

_PTGS = [
    ('Pike', 'Atlanta'),
    ('Queens', 'Denver'),
    ('Rocky', 'Dublin'),
]


class PtgCount(show.ShowOne):

    # Set the command so that when we run through
    # python-openstackclient we do not require authentication.
    auth_required = False

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        choices = [s[0].lower() for s in _PTGS]
        parser.add_argument(
            'first',
            help='Your first PTG',
            choices=choices,
        )
        parser.add_argument(
            'current',
            help='The current PTG',
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
        return (('PTGs',), (current - first + 1,))


class PtgList(lister.Lister):

    # Set the command so that when we run through
    # python-openstackclient we do not require authentication.
    auth_required = False

    def take_action(self, parsed_args):
        columns = ('Number', 'Name', 'Location')
        summits = []
        for i, s in enumerate(_PTGS, 1):
            summits.append((i,) + s)
        return (columns, summits)
