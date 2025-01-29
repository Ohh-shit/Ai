import subprocess
import re

def get_wifi_profiles():
    """Retrieve all Wi-Fi profiles."""
    try:
        profiles_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8')
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_output)
        return profiles
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve Wi-Fi profiles.")
        return []

def get_wifi_details(profile):
    """Retrieve detailed information about a specific Wi-Fi profile."""
    try:
        profile_details = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', f'name={profile}', 'key=clear'], encoding='utf-8'
        )
        # Extract details
        password = re.search(r"Key Content\s*:\s*(.*)", profile_details)
        auth_type = re.search(r"Authentication\s*:\s*(.*)", profile_details)
        encryption_type = re.search(r"Cipher\s*:\s*(.*)", profile_details)
        connection_mode = re.search(r"Connection mode\s*:\s*(.*)", profile_details)
        network_type = re.search(r"Network type\s*:\s*(.*)", profile_details)
        radio_type = re.search(r"Radio type\s*:\s*(.*)", profile_details)
        vendor_info = re.search(r"Vendor extension\s*:\s*(.*)", profile_details)

        # Weak password detection
        is_weak_password = password and len(password.group(1)) < 8

        return {
            "Password": password.group(1) if password else "<No Password>",
            "Weak Password": is_weak_password,
            "Authentication Type": auth_type.group(1) if auth_type else "<Unknown>",
            "Encryption Type": encryption_type.group(1) if encryption_type else "<Unknown>",
            "Connection Mode": connection_mode.group(1) if connection_mode else "<Unknown>",
            "Network Type": network_type.group(1) if network_type else "<Unknown>",
            "Radio Type": radio_type.group(1) if radio_type else "<Unknown>",
            "Vendor Info": vendor_info.group(1) if vendor_info else "<Unknown>",
        }
    except subprocess.CalledProcessError:
        return {
            "Password": "<Error Retrieving Details>",
            "Weak Password": False,
            "Authentication Type": "<Error>",
            "Encryption Type": "<Error>",
            "Connection Mode": "<Error>",
            "Network Type": "<Error>",
            "Radio Type": "<Error>",
            "Vendor Info": "<Error>",
        }

def test_connection(profile):
    """Test connection to the Wi-Fi profile."""
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        return "Successful" if result.returncode == 0 else "Failed"
    except Exception:
        return "Error Testing Connection"

def get_signal_strength():
    """Retrieve signal strength for connected Wi-Fi."""
    try:
        wlan_output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], encoding='utf-8')
        signal_strength = re.search(r"Signal\s*:\s*(\d+)%", wlan_output)
        return signal_strength.group(1) + '%' if signal_strength else "<Unknown>"
    except subprocess.CalledProcessError:
        return "<Error Retrieving Signal Strength>"

def get_channel_info():
    """Retrieve channel information for connected Wi-Fi."""
    try:
        wlan_output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], encoding='utf-8')
        channel = re.search(r"Channel\s*:\s*(\d+)", wlan_output)
        return channel.group(1) if channel else "<Unknown>"
    except subprocess.CalledProcessError:
        return "<Error Retrieving Channel Information>"

def show_wifi_profiles_with_details():
    """Display all Wi-Fi profiles with their details."""
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    print("\nWi-Fi Profiles and Details:")
    print("------------------------------------------------------------")
    for index, profile in enumerate(profiles, start=1):
        details = get_wifi_details(profile)
        connection_status = test_connection(profile)
        signal_strength = get_signal_strength()
        channel_info = get_channel_info()

        print(f"\nProfile {index}:")
        print(f"   Name               : {profile}")
        print(f"   Password           : {details['Password']}")
        print(f"   Weak Password      : {'Yes' if details['Weak Password'] else 'No'}")
        print(f"   Authentication     : {details['Authentication Type']}")
        print(f"   Encryption         : {details['Encryption Type']}")
        print(f"   Connection Mode    : {details['Connection Mode']}")
        print(f"   Network Type       : {details['Network Type']}")
        print(f"   Radio Type         : {details['Radio Type']}")
        print(f"   Vendor Info        : {details['Vendor Info']}")
        print(f"   Connection Status  : {connection_status}")
        print(f"   Signal Strength    : {signal_strength}")
        print(f"   Channel            : {channel_info}")

if __name__ == "__main__":
    show_wifi_profiles_with_details()
