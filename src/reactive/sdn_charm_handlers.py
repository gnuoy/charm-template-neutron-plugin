# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import charms_openstack.charm as charm
import charms.reactive as reactive

# This charm's library contains all of the handler code associated with
# sdn_charm
import charm.openstack.{{ charm_lib }} as {{ charm_lib }}  # noqa

charm.use_defaults(
    'charm.installed',
    'update-status')

@reactive.when('neutron-plugin.connected')
def configure_neutron_plugin(neutron_plugin):
    with charm.provide_charm_instance() as charm_class:
        neutron_plugin.configure_plugin(
            plugin='ovs',
            config={
                "nova-compute": {
                    "/etc/nova/nova.conf": {
                        "sections": {
                            'DEFAULT': [
                            ],
                        }
                    }
                }
            })
