#!/bin/sh

namespace=$(grep -w "namespace" galaxy.yml |  awk  '{print $2}')
name=$(grep -w "name" galaxy.yml |  awk  '{print $2}')
version=$(grep -w "version" galaxy.yml |  awk  '{print $2}')
collection_file="$namespace-$name-$version.tar.gz"
#echo "$collection_file"

rm -f /root/ansible_log.log
rm -rf /root/.ansible/collections/ansible_collections/dellemc/sfss
rm "$collection_file"
ansible-galaxy collection build

ansible-galaxy collection install "$collection_file" --force #-with-deps

#ansible-playbook -i playbooks/hosts playbooks/sfss_security_auth.yaml -vvv
#ansible-playbook -i playbooks/hosts playbooks/sfss_interface_ip_mgmt.yaml -vvv
#ansible-playbook -i playbooks/hosts playbooks/sfss_app_images.yaml -vvv
# ansible-playbook -i playbooks/hosts playbooks/sfss_app_image_upgrade.yaml -vvv
#ansible-playbook -i playbooks/hosts playbooks/sfss_endpoints.yaml -vv
#ansible-playbook -i tests/regression/hosts tests/regression/test.yaml -vv
# ansible-playbook -i playbooks/hosts playbooks/sfss_zones.yaml -vvv
#ansible-playbook -i playbooks/hosts playbooks/sfss_zone_groups.yaml -vvv
# ansible-playbook -i playbooks/hosts playbooks/sfss_zone_alias.yaml -vvv
#ansible-playbook -i playbooks/hosts playbooks/sfss_cdc_instances.yaml -vvv

