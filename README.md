Wi-Fi Profile and Detail Viewer

This script retrieves and displays detailed information about all available Wi-Fi profiles on a Windows system.

Features
Retrieve Wi-Fi Profiles: Lists all Wi-Fi profiles available on the system.

Fetch Wi-Fi Details: Provides detailed information such as password, authentication type, encryption type, etc.

Test Connection: Tests the connection to the specified Wi-Fi profile.

Signal Strength & Channel Info: Retrieves the signal strength and channel information for connected Wi-Fi.

Collaborated with AI
This project includes AI-assisted code enhancements and optimizations.

Prerequisites
Python 3.6+: Ensure you have Python 3.6 or newer installed.

Usage
1. Clone the repository or download the script.

2. Navigate to the script directory in your terminal.

3. Run the script using Python:
python wifi_profile_viewer.py

4. Follow the on-screen instructions to see detailed information about your Wi-Fi profiles.

Example Output
Wi-Fi Profiles and Details:
------------------------------------------------------------

Profile 1:
   Name               : HomeWiFi
   Password           : <password>
   Weak Password      : No
   Authentication     : WPA2-Personal
   Encryption         : AES
   Connection Mode    : Auto-Connect
   Network Type       : Infrastructure
   Radio Type         : 802.11ac
   Vendor Info        : Acme Inc.
   Connection Status  : Successful
   Signal Strength    : 75%
   Channel            : 6
------------------------------------------------------------

Libraries Used
The script utilizes the subprocess and re libraries, both of which are part of Python's standard library. No additional installations via pip are required.


Contact:
For any questions or suggestions, please contact: reply4buck@gmail.com

