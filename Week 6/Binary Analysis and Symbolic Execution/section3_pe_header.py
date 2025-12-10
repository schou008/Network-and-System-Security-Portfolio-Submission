#section3_pe_header.py
#Library for reading PE structures
import pefile         
#Handles file paths safely      
from pathlib import Path     

#File to analyse
sample = r"C:\Windows\System32\notepad.exe"

def inspect_pe(path):
    """
    Load and inspect the PE file header.

    Parameters:
        path (str): Path to the executable file
    """

    #Load the PE file; pefile automatically parses the structure
    pe = pefile.PE(path)

    #Print the entry point address:
    #This is where execution begins when the file runs
    print("Entry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))

    #Image base is the preferred memory address where the PE is loaded
    print("Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))

    print("\nImported DLLs and first 5 functions:")

    #List imported DLLs and their functions
    #Attackers often hide malicious imports or use dynamic loading
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        #Print the name of the imported DLL
        print(" ", entry.dll.decode())

        #Print the first 5 imported functions from this DLL
        for imp in entry.imports[:5]:
            #Some imports may not have names (rare but possible)
            print("    -", imp.name.decode() if imp.name else "None")


if __name__ == "__main__":
    #Convert string path into a Path object for safety
    sample_path = Path(sample)

    #Validate that the file exists before attempting analysis
    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")
    else:
        #Run PE inspection
        inspect_pe(sample)