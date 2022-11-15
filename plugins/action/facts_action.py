# Copyright (c) 2022 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        # This just overrides, the action plugin can also run a module/cmd/inspect
        # to determine whether to override pkg_mgr.
        return {
            'ansible_facts': {
                'pkg_mgr': 'jordan.package.mgr',
            }
        }
