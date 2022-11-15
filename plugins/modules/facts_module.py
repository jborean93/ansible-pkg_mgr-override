#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: facts_module
short_description: Retrieves custom pkg_mgr to use with package
description:
- Tests out custom facts module overriding pkg_mgr for use with package
options: {}
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
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    module.exit_json(
        ansible_facts={'pkg_mgr': 'jordan.package.mgr'}
    )


if __name__ == '__main__':
    main()
