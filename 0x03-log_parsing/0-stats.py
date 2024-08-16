#!/usr/bin/python3
import sys

# Initialize total file size and a dictionary for status code counts
total_file_size = 0
status_code_count = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

def print_metrics():
    """Print the current metrics: total file size and status code counts."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Ensure the line has enough components and matches expected format
        if len(parts) > 6:
            try:
                # Extract status code and file size from the line
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code count if it's a valid code
                if status_code in

