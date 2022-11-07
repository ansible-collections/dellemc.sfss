### Overview
Dell EMC SFSS Ansible Modules unit test scripts are located under
 [unit](./tests/regression/roles) directory.

### Implementing the unit tests
Any contribution must have an associated unit test. This section covers the
 tests that need to be carried out. 
* The unit tests are required for each new resource, bug fix, or enhancement. They must cover what is being submitted.

### Prerequisites
* Dell EMC SFSS collections - to install run `ansible-galaxy collection install dellemc.sfss`

### Executing unit tests
You can execute them manually by running [test](https://github.com/ansible-collections/dellemc.sfss/blob/main/tests/regression/test.yaml).
