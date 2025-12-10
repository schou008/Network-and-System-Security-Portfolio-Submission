#section6_full_workflow.py
from section1_hashes import compute_hashes
from section2_strings import extract_strings
#Reads PE header + imports
from section3_pe_header import inspect_pe
#Extracts URLs & IP indicators   
from section4_iocs import extract_iocs
#Runs a YARA rule on the file        
from section5_yara import yara_scan    
#Computes MD5/SHA1/SHA256         
from section1_hashes import compute_hashes  
#Extracts readable ASCII strings    
from section2_strings import extract_strings    
from pathlib import Path

#Target file for analysis
sample = r"C:\Windows\System32\notepad.exe"


def full_analysis(path):
    """
    Runs a complete static triage analysis on the given file.
    This mirrors the workflow used by malware analysts.

    Steps included:
        1. Hash calculation (IOCs)
        2. String extraction
        3. PE header & import enumeration
        4. IOC extraction (URLs/IPs)
        5. YARA rule scanning
    """

    #Hash Analysis
    print("=== HASHES ===")
    hashes = compute_hashes(path)
    for k, v in hashes.items():
        print(f"{k.upper()}: {v}")

    #String Extraction
    print("\n=== STRINGS (first 20) ===")
    strings = extract_strings(path)
    #Print only the first 20 strings for readability
    for s in strings[:20]:  
        print(s.decode(errors="ignore"))

    #PE Header Inspection
    print("\n=== PE HEADER & IMPORTS ===")
    inspect_pe(path)

    #IOC Extraction (URLs / IPs)
    print("\n=== IOCs ===")
    urls, ips = extract_iocs(path)
    print("URLs:", urls)
    print("IPs:", ips)

    #YARA Scanning
    print("\n=== YARA MATCHES ===")
    matches = yara_scan(path)
    print(matches)

if __name__ == "__main__":
    sample_path = Path(sample)
    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")
    else:
        #Run the complete analysis workflow
        full_analysis(sample)