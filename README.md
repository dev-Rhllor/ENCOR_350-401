Repository for the ENCOR 350-401 Cisco Certification Exam.

## PART 1 Python Crash Course

0. [Optional] IDE Configuration. You can use this [link](https://developer.cisco.com/learning/lab/dev-win/step/1) to prepare your environment.
1. Read the [python first steps](https://realpython.com/python-first-steps/) and:
    - Solve the **python_first_steps_excercises.py**
    - Do all **loop_excercises.py**
2. Read the first 6 points of [Functions for beginners](https://towardsdatascience.com/python-for-beginners-functions-2e4534f0ae9d) and all [functions with a not-defined amount of arguments](https://www.geeksforgeeks.org/args-kwargs-python/) and:
    - Do all **input_print_functions_excercises.py**
3. Read the introductions of [imports and modules](https://www.programiz.com/python-programming/modules).
4. Understand the use of the [Main function](https://realpython.com/python-main-function/)

## PART 2 Paramiko vs Netmiko vs Napalm

1. Build the test environment using GNS3 and configure the devices with the initial configuration provided.
2. Download or copy the following files in the **Network Automation** device. 
    - paramiko_show.py
    - netmiko_show.py
    - napalm_show.py
    - inventory.py
3. Open the **paramiko_show.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
4. Open the **netmiko_show.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Run it against the junos_vsrx device.
    - Compare outputs. 
5. Open the **napalm_show.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Run it against the junos_vsrx device.
    - Compare outputs. 

## PART 3 Configuring devices using Paramiko/Netmiko/Napalm

1. Download or copy the following files in the **Network Automation** device. 
    - paramiko_config.py
    - netmiko_config.py
    - napalm_config.py
    - inventory.py
    - interface_config.py
    - cisco_verification.yaml
3. Open the **paramiko_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
4. Open the **netmiko_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
5. Open the **napalm_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Compare outputs.
6. Open the **napalm_verify.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Compare outputs.

## PART 4 XML, JSON and YAML

1. Download or copy the following files in the **Network Automation** device.
    - inventory.xml
    - inventory.json
    - inventory.yaml
    - data_import.py
2. Open the **inventory.xml** file and identify their building components:
    - XML declaration
    - root element
    - child elemments
    - attributes
    - tags
3. Open the **inventory.json** file and identify their building components:
    - Objects
    - Lists
    - Data Types: String, number, object, array, boolean, Null

4. Open the **inventory.yaml** file and identify their building components:
    - Objects
    - Lists
    - Data Types: String, number, object, array, boolean, Null

5. Open the **data_importer.py** script and:
    - Identify their building components.
    - Run it against the different inventory files types.
    - Compare outputs.

## PART 5 ANSIBLE

1. From the [Ansible Documentation](https://docs.ansible.com/ansible/latest/network/getting_started/index.html) read:
    - [Basic Concepts](https://docs.ansible.com/ansible/latest/network/getting_started/basic_concepts.html)
    - [Network differences](https://docs.ansible.com/ansible/latest/network/getting_started/network_differences.html)

3. Download or copy the following files in the **Network Automation** device. 
    - ansible_ios-xe.yaml
    - ansible.cfg
    - cisco_config.txt
    - inventory.yaml

4. Open the **inventory.yaml** file and identify their building componentes:
    - Hosts.
    - Variables.

5. Open the **ansible_ios-xe.yaml** playbook and identify their building componentes:
    - Plays.
    - Tasks.
    - Modules.
    - Tags.
    - Design Patterns.

4. Run the **ansible_ios-xe.yaml** with and without verbose options. Compare the output.