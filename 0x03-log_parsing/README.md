# 0x03. Log Parsing

## Description
This project reads logs from standard input and computes metrics in real-time, including the total file size and the frequency of specific HTTP status codes.

## Requirements
- Ubuntu 20.04 LTS
- Python 3.4.3

## Usage
To run the script, pipe a log generator into it as follows:
```bash
./0-generator.py | ./0-stats.py

