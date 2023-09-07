import argparse
import re

def extract_and_save_uuids(file_path, output_file_path):
    uuids = []
    uuid_pattern = r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'
    
    # Read the file and extract UUIDs
    with open(file_path, 'r') as f:
        for line in f:
            line = line.replace('K', '')
            uuids += re.findall(uuid_pattern, line, re.IGNORECASE)
    
    # Save the extracted UUIDs to a new file, one per line
    with open(output_file_path, 'w') as f:
        for uuid in uuids:
            f.write(f"{uuid}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract and save UUIDs from a file.')
    parser.add_argument('-f', '--file', required=True, help='Path to the input file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output file')
    
    args = parser.parse_args()
    
    result = extract_and_save_uuids(args.file, args.output)
    print(f"UUIDs have been saved to {args.output}")
