#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: mgr
short_description: Test out pkg_mgr injection from collection
description:
- Tests out custom module being used with package from core
options:
  name:
    description:
    type: str
    required: true
  state:
    description:
    type: str
    choices:
    - absent
    - present
    default: present
seealso:
- module: ansible.builtin.package
author:
- Jordan Borean (@jborean93)
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = dict(
        name=dict(type='str', required=True),
        state=dict(type='str', choices=['absent', 'present'], default='present'),
    )
    result = dict(
        changed=False,
        msg='from custom module',
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
