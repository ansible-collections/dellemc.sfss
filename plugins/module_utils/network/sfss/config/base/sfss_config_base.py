from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.facts.facts import Facts
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.utils import (
    get_diff,
    update_states,
    remove_empties_from_list,
    send_requests,
)
from ansible_collections.dellemc.sfss.plugins.module_utils.network.sfss.utils.debug import debug
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)


class StfsConfigBase(ConfigBase):

    def __init__(self, module):
        super(StfsConfigBase, self).__init__(module)

    def get_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        debug("get_facts facts", facts)
        facts_data = facts['ansible_network_resources'].get(self.resource_name)
        if not facts_data:
            return []
        return facts_data

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_facts = self.get_facts()
        self.orginate_nqns = self.get_orginate_nqns_data()
        commands, requests = self.set_config(existing_facts)
        debug("execute_module existing_facts", existing_facts)
        debug("execute_module commands", commands)
        debug("execute_module requests", requests)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                responses = send_requests(self, requests)
            result['changed'] = True
        result['commands'] = commands

        changed_facts = self.get_facts()

        result['before'] = existing_facts
        if result['changed']:
            result['after'] = changed_facts

        result['warnings'] = warnings

        return result

    def get_orginate_nqns_data(self):
        return None

    def set_config(self, existing_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_facts
        resp = self.set_state(want, have)
        debug("set_config: resp", resp)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        state = self._module.params['state']
        diff = get_diff(want, have, self.test_keys)
        debug("Diff", diff)
        debug("want", want)
        debug("have", have)
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        ret_commands = remove_empties_from_list(commands)

        debug("set_state: resp", requests)
        return ret_commands, requests

    # def _state_replaced(**kwargs):
    #     """ The command generator when state is replaced

    #     :rtype: A list
    #     :returns: the commands necessary to migrate the current configuration
    #               to the desired configuration
    #     """
    #     commands = []
    #     return commands

    # def _state_overridden(**kwargs):
    #     """ The command generator when state is overridden

    #     :rtype: A list
    #     :returns: the commands necessary to migrate the current configuration
    #               to the desired configuration
    #     """
    #     commands = []
    #     return commands

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        requests = []
        commands = []
        if not want:
            commands, requests = self.build_delete_all_requests(have)
        else:
            debug("delete commands", diff)
            commands = get_diff(want, diff, self.test_keys)
            commands, requests = self.build_delete_requests(commands, want, have, diff)

        debug("final commands", commands)
        debug("final requests", requests)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = update_states(diff, "merged")
        ret_requests = []
        ret_commands = []
        for command in commands:
            matched_have = self.matches(command, have)
            debug("matched_have1", matched_have)
            if not matched_have:
                reqs = self.build_create_request(have, command)
            else:
                reqs = self.build_update_requests(have, matched_have, command)

            if reqs:
                ret_requests.extend(reqs)
                ret_commands.append(command)

        debug("final commands", ret_commands)
        debug("final requests", ret_requests)
        return ret_commands, ret_requests

    def matches(self, want_ep, have):
        debug("into matches")
        ep_id = self.resource_id(want_ep)
        debug("ep_id", ep_id)
        matched_have = None
        if isinstance(have, list):
            for have_ep in have:
                have_ep_id = self.resource_id(have_ep)
                debug("have_ep_id", have_ep_id)
                if ep_id == have_ep_id:
                    matched_have = have_ep
                    break
        else:
            have_ep_id = self.resource_id(have)
            debug("have_ep_id", have_ep_id)
            if ep_id == have_ep_id:
                matched_have = have
        return matched_have
