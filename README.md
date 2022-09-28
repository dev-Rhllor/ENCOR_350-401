Repository for ENCOR 350-401 Cisco Certification Exam.

## PART 1 Python Crash Course

0. [Optional] IDE Configuration. Use this [link](https://developer.cisco.com/learning/lab/dev-win/step/1) to prepare your environment.
1. Read the [python first steps](https://realpython.com/python-first-steps/) and:
    - Solve the **python_first_steps_excercises.py**
    - Do all **loop_excercises.py**
2. Read the first 6 points of [Functions for beginners](https://towardsdatascience.com/python-for-beginners-functions-2e4534f0ae9d) and all [functions with a not-defined amount of arguments](https://www.geeksforgeeks.org/args-kwargs-python/) and:
    - Do all **input_print_functions_excercises.py**
3. Read the introductions of [imports and modules](https://www.programiz.com/python-programming/modules).
4. Understand the use of the [Main function](https://realpython.com/python-main-function/)

## PART 2 Paramiko vs Netmiko vs Napalm

1. Build the test environment using GNS3. Configure the devices with the initial configuration provided in this repository.
2. Download or copy the following files into the **Network Automation** device. 
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

1. Download or copy the following files into the **Network Automation** device. 
    - paramiko_config.py
    - netmiko_config.py
    - napalm_config.py
    - inventory.py
    - interface_config.py
    - cisco_verification.yaml
2. Open the **paramiko_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
3. Open the **netmiko_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
4. Open the **napalm_config.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Compare outputs.
5. Open the **napalm_verify.py** script and:
    - Identify their building components.
    - Run it against the ios_router device.
    - Compare outputs.

## PART 4 XML, JSON and YAML

1. Download or copy the following files into the **Network Automation** device.
    - inventory.xml
    - inventory.json
    - inventory.yaml
    - data_import.py
2. Open the **inventory.xml** file and identify their building components:
    - XML declaration/prolog.
    - XML Elements and tags.
        - root element.
        - child element.
    - XML Attributes.
3. Open the **inventory.json** file and identify their building components:
    - Objects
    - Lists.
    - Data Types: String, number, object, array, boolean, Null.

4. Open the **inventory.yaml** file and identify their building components:
    - Objects.
    - Lists.
    - Data Types: String, number, object, array, boolean, Null.

5. Open the **data_importer.py** script and:
    - Identify their building components.
    - Run it against the different inventory file types.
    - Compare outputs.

## PART 5 ANSIBLE

1. From the [Ansible Documentation](https://docs.ansible.com/ansible/latest/network/getting_started/index.html) read:
    - [Basic Concepts](https://docs.ansible.com/ansible/latest/network/getting_started/basic_concepts.html)
    - [Network differences](https://docs.ansible.com/ansible/latest/network/getting_started/network_differences.html)

2. Read and compare the different automation tools from [here](https://ipcisco.com/lesson/ansible-vs-puppet-vs-chef/)

3. Download or copy the following files into the **Network Automation** device. 
    - ansible_ios-xe.yaml
    - ansible.cfg
    - cisco_config.txt
    - inventory.yaml

4. Open the **inventory.yaml** file and identify their building componentes:
    - Hosts.
    - Variables.

5. Open the **ansible_ios-xe.yaml** playbook and identify their building components:
    - Plays.
    - Tasks.
    - Modules.
    - Tags.
    - Design Patterns.

6. Run the **ansible_ios-xe.yaml** with and without verbose options. Compare the output.

## PART 6 APIs and DNAc.

1. Watch the APIs introduction from [DEVNET Fundamentals](https://www.youtube.com/watch?v=xHBnfmiMSF4)

2. Read and understand the release policies of APIs from [Redhat](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces)
    - Private
    - Public
    - Partner

3. Read REST API definition from [here](https://restfulapi.net/) and understand the *six guiding principles the RESTful architecture*:
    - Uniform interface
    - Client–server
    - Stateless
    - Cacheable
    - Layered system
    - Code on demand (optional)

4. Read HTTP Methods from [here](https://restfulapi.net/http-methods/) and understand the difference between: 
    - GET
    - POST
    - PUT
    - DELETE
    - PATCH

5. Read and undestand the HTTP Status Codes from [here](https://restfulapi.net/http-status-codes/)
    - 1xx: Informational
    - 2xx: Success
    - 3xx: Redirection
    - 4xx: Client Error
    - 5xx: Server Error

6. Learn about the Cisco DNA Center API Overview with this [DEVNET Learning LAB](https://developer.cisco.com/learning/labs/dne-dnac-api-overview/) and: 
    - Understand Cisco DNA Center Programmability in the context of DNA.
    - Understand the five Cisco DNA Center API Domains.
    - Explore the main starting points for the Cisco DNA Center APIs.

7. Use this [Postman collection](https://www.postman.com/team-rhllor/workspace/cisco-encor-350-401) and authenticate into the different following Cisco REST APIs
    - Cisco DNAc [Documentation](https://developer.cisco.com/docs/dna-center/#!authentication-and-authorization/basic-authentication)
    - Cisco SDWAN [Documentation](https://developer.cisco.com/docs/sdwan/#!authentication/how-to-authenticate) 
    - Cisco IOS-XE using RESTCONF [Documentation](https://developer.cisco.com/docs/ios-xe/#!enabling-restconf-on-ios-xe/authentication)

## PART 7 Model Driven Programability (RESTCONF, NETCONF and YANG)

1. Learn about Moder Driven Programability reading the introduction of this [Devnet Learning LAB: MDP - Introduction](https://developer.cisco.com/learning/modules/intro-device-level-interfaces/why-mdp/introduction/)

2. Explore the YANG data model using:
    - The Python module Pyang following the [Devnet Learning LAB: MDP - Introduction](https://developer.cisco.com/learning/modules/intro-device-level-interfaces/intro-yang/introduction/)
    - The [Yang Catalog](https://www.yangcatalog.org/home.html)

3. Download or copy the following files into the **Network Automation** device. 
    - netconf_get.py
    - restconf_get.py
    - netconf_edit-config.py
    - restconf_post.py
    - netconf_telemetry.py
    - inventory.py

4. Open the **netconf_get.py** script and:
    - Identify their building components.
    - Run it against the sandbox device.

5. Open the **restconf_get.py** script and:
    - Identify their building components.
    - Run it against the sandbox device.

6. Open the **netconf_edit-config.py** script and:
    - Identify their building components.
    - Run it against the sandbox device.

7. Open the **restconf_post.py** script and:
    - Identify their building components.
    - Run it against the sandbox device.

8. Open the **netconf_telemetry.py** script and:
    - Identify their building components.
    - Run it against the sandbox device.