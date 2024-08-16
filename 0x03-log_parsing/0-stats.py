#!/usr/bin/python3
import sys

# Initialize global variables
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """Print the total file size and status code counts in ascending order."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

try:
    for line in sys.stdin:
        line = line.strip()  # Strip any extra whitespace
        parts = line.split()  # Split the line into parts

        # Check if the line has the correct format
        if len(parts) < 7:
            continue  # Skip if the line is malformed

        try:
            # Extract status code and file size
            status_code = int(parts[-2])  # Status code is the second-to-last element
            file_size = int(parts[-1])    # File size is the last element

            # Update total file size
            total_file_size += file_size

            # Update the count for the status code if it's valid
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines that don't have valid status code or file size
            continue

        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle CTRL + C by printing the metrics before exiting
    print_metrics()
    raise

# Print final metrics at the end of the input
print_metrics()

