import os
import re

# Define the patterns to search for (sample patterns for demonstration purposes)
malware_patterns = [
    r'\bexec\(base64',
    r'rm -rf /',
    r'\bxorstr\(0x[A-Fa-f0-9]+\)',
]

# Specify the directory to scan
directory_to_scan = '/path/to/directory'

# Scan the directory for malware patterns
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                for pattern in malware_patterns:
                    if re.search(pattern, content):
                        print("Malware pattern found in:", file_path)
                        break

# Start the scan
scan_directory(directory_to_scan)
