#section4_iocs.py
#Used for pattern matching (regex)
import re
#Safe file path handling
from pathlib import Path    

#Path to the sample file being analysed
#In a malware investigation, this would be the suspicious binary
sample = r"C:\Users\Saqib\Downloads\test.txt"


def extract_iocs(path):
    """
    Extract URLs and IP addresses from a file.

    Parameters:
        path (str): File path
    
    Returns:
        urls (list): List of detected URLs
        ips (list): List of detected IPv4 addresses
    """

    #Read the file in binary mode to avoid decode errors
    with open(path, "rb") as f:
        #Decode bytes → text, ignoring unreadable characters
        #This is important because binaries contain random bytes
        data = f.read().decode(errors="ignore")

    #Regex for URLs:
    #Matches http:// or https:// followed by any non-space characters
    urls = re.findall(r"https?://[^\s\"']+", data)

    #Regex for IPv4 addresses:
    #Matches numbers in the 0–255 range separated by dots
    ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", data)

    return urls, ips


if __name__ == "__main__":
    #Convert string to Path object for validation
    sample_path = Path(sample)

    #Check whether the file actually exists
    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")

    else:
        # Extract indicators of compromise
        urls, ips = extract_iocs(sample)

        print("=== IOCs ===")
        #May show malicious C2 servers in real malware
        print("URLs:", urls)
        #May show attacker infrastructure   
        print("IPs:", ips)     