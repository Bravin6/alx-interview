#!/usr/bin/python3
import sys

# Initialize metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_code_count.keys())
line_count = 0

def print_metrics():
    """Print the total file size and status code count."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

try:
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespace
        line_count += 1
        
        # Split the line into parts
        parts = line.split()
        if len(parts) < 7:  # Check for minimum parts length
            continue

        try:
            # Extract the status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code count if valid
            if status_code in valid_status_codes:
                status_code_count[status_code] += 1

        except (ValueError, IndexError):
            # Skip the line if it has parsing errors
            continue

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Print metrics on keyboard interrupt (CTRL + C)
    print_metrics()
    raise

# Print final metrics after EOF
print_metrics()

