
# SAAF (System Analysis and Forensic Tool)

## Project Description

SAAF is a comprehensive forensic and system analysis tool designed for Windows environments. It provides multiple functionalities, such as gathering system information, forensic data dumping, IOC (Indicators of Compromise) searching, and special scanning for sensitive information. The tool is modular, allowing each functionality to be developed and expanded independently.

## Features

1. **System Information Gather**
   - Collects detailed system information, including hardware details, network configuration, CPU usage, memory usage, disk partitions, and more.
   - Outputs all collected information to a text file for easy reference and further analysis.

2. **Forensic Dumper (via txt)**
   - Designed to simulate a stealer's behavior by gathering specific files and information from the system.
   - Potentially gathers browser history, saved passwords, system logs, and other sensitive data that an attacker might target.
   - Dumps all collected data into text files for forensic analysis.

3. **IOC Search**
   - Allows integration with Threat Intelligence (TI) sources to search for known IOCs on the system.
   - Can be used to scan the system for indicators like malicious IP addresses, file hashes, or domain names.
   - Designed to be expandable with various TI sources, offering robust and customizable threat detection.

4. **Special Scanner**
   - Scans the entire system for specific sensitive information, such as Bitcoin wallets, financial documents, or any other user-defined targets.
   - Allows deep scanning of all directories to locate and identify critical files that may require further analysis or protection.

## Technologies Used
- Python 3
- `psutil` library (for system information gathering)
- `platform`, `cpuinfo`, `socket`, `uuid`, `re` libraries (for detailed system and network information)
- `argparse` (for handling command-line arguments in the hash tool)

## Installation Steps

1. **Install the required libraries:**
   - Install the necessary Python libraries by running:
     ```sh
     pip install psutil art py-cpuinfo filehash python-magic
     ```

2. **Running the Script:**
   - Start the SAAF tool by running:
     ```sh
     python main.py
     ```

   - The `main.py` script will present a menu to select the desired functionality.

3. **Using the Features:**
   - **System Information Gather:** Collects and saves comprehensive system data.
   - **Forensic Dumper:** (To be implemented) Gathers data typically targeted by stealers.
   - **IOC Search:** (To be implemented) Allows searching for IOCs using integrated TI sources.
   - **Special Scanner:** (To be implemented) Scans for sensitive information such as Bitcoin wallets or financial records.

## Potential Enhancements
- Implement the **Forensic Dumper** to collect specific sensitive information, simulating stealer behavior.
- Integrate with various TI sources for the **IOC Search** functionality.
- Develop the **Special Scanner** to thoroughly search the system for user-defined sensitive information.

## Support and Contact
If you have any questions or suggestions, feel free to contact the project maintainer at [kilicbartu@gmail.com](mailto:kilicbartu@gmail.com).
