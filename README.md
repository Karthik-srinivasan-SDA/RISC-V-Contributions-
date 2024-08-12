**Opcode Definition Validator**


**Overview**:
 This Python script reads a YAML file containing opcode definitions and performs several consistency checks on the metadata. The primary purpose of the script is to ensure the correctness and validity of the opcode definitions used in assembly or machine code generation.

**Features**:

1.Bit Range Validation: Ensures that there are no overlapping bit ranges within the opcode definitions.

2.Value Representation Check: Validates that the values assigned to bit ranges are representable within their specified width.

3.Argument Mapping Verification: Confirms that all arguments used in the instructions have corresponding mappings in the provided argument lookup table.

**Prerequisites**
Python 3.x: Ensure that Python is installed on your system.

**YAML Library:** 
The script uses the PyYAML library to parse YAML files. Install it using:

pip install pyyaml

**Details of Repo:**

1.Script.py : contains script to configure the yaml file
2.config.yml: contains the opcode structures and defenitions

**Reference:**

https://docs.google.com/document/d/1H8WBROpBzEZMqiyjLmNyH6nZ8tqmYWq9GKQFUKRmmdw/edit

Repository URL:
https://github.com/riscv/riscv-opcodes

