import yaml
import sys

def load_yaml(filename):
    try:
        with open(filename, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        sys.exit(1)
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        sys.exit(1)

def check_overlapping_bit_ranges(bit_ranges):
    sorted_ranges = sorted(bit_ranges, key=lambda x: x['start'])
    overlap_found = False
    for i in range(len(sorted_ranges) - 1):
        if sorted_ranges[i]['end'] >= sorted_ranges[i + 1]['start']:
            print(f"2. Overlapping Check Error: Overlapping bit ranges detected between {sorted_ranges[i]} and {sorted_ranges[i + 1]}.")
            overlap_found = True
    return not overlap_found

def check_value_within_bit_width(bit_ranges):
    value_issue_found = False
    for bit_range in bit_ranges:
        width = bit_range['end'] - bit_range['start'] + 1
        max_value = (1 << width) - 1
        if bit_range['value'] > max_value:
            print(f"4. Representation of Bits within specified range Error: Value {bit_range['value']} is too large for a {width}-bit range in {bit_range}.")
            value_issue_found = True
    return not value_issue_found

def check_arguments(opcode, arguments, argument_lookup):
    argument_issue_found = False
    for arg in arguments:
        if arg['name'] not in argument_lookup:
            print(f"3. Argument Missing case: Error: Argument '{arg['name']}' in opcode '{opcode}' is not found in the argument lookup table.")
            argument_issue_found = True
    return not argument_issue_found

def verify_opcode_consistency(opcodes, argument_lookup):
    all_valid = True
    for opcode in opcodes:
        print(f"\n1. Validation case: Checking opcode '{opcode['name']}'...")
        
        bit_ranges = opcode['bit_ranges']
        arguments = opcode['arguments']
        
        if not check_overlapping_bit_ranges(bit_ranges):
            all_valid = False
            
        if not check_value_within_bit_width(bit_ranges):
            all_valid = False
            
        if not check_arguments(opcode['name'], arguments, argument_lookup):
            all_valid = False
            
    if all_valid:
        print("All opcodes are consistent and valid.")
    else:
        print("Some opcodes have consistency issues. Please review the errors above.")

def main():
    # Replace with your actual YAML file path
    yaml_file = "config.yml"
    argument_lookup_table = {
        "rd": "register",
        "rs1": "register",
        "rs2": "register",
        "imm": "immediate",
        # Add more arguments as needed
    }

    yaml_data = load_yaml(yaml_file)
    opcodes = yaml_data.get('opcodes', [])

    if not opcodes:
        print("Error: No opcodes found in the YAML file.")
        sys.exit(1)

    verify_opcode_consistency(opcodes, argument_lookup_table)

if __name__ == "__main__":
    main()
