#section2_strings.py
#Used for regex pattern matching
import re
#Safer file path handling
from pathlib import Path 

#Path to the file we want to analyse
sample = r"C:\Windows\System32\notepad.exe"

def extract_strings(path, min_len=4):
    """
    Extract ASCII strings from a binary file.
    
    Parameters:
        path (str): File path
        min_len (int): Minimum string length to return
        
    Returns:
        list of byte strings containing readable text
    """

    #Open file in binary mode and read all bytes
    with open(path, "rb") as f:
        data = f.read()
    return re.findall(rb"[ -~]{%d,}" % min_len, data)


if __name__ == "__main__":
    #Convert path string to a Path object
    sample_path = Path(sample)

    #Validate file exists before trying to read it
    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")

    else:
        strings = extract_strings(sample)

        print("=== STRINGS (first 20) ===")

        #Display the first 20 extracted strings
        for s in strings[:20]:
            #Decode bytes to text, ignoring characters that can't convert
            print(s.decode(errors="ignore"))