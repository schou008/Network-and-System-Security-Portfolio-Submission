#section5_yara.py
#YARA Python library for rule matching
import yara    
#Used for safe file path handling           
from pathlib import Path    

#Path to the file we want to analyse
sample = r"C:\Users\Saqib\Downloads\test.txt"


def yara_scan(path):
    """
    Compile and apply a simple YARA rule to a file.

    Parameters:
        path (str): Path to the target file

    Returns:
        List of YARA matches (empty list if no rules matched)
    """

    #YARA rule definition written directly as a Python string
    rule_source = """
    rule ContainsHTTP {
        strings:
            $s = "http"     // Search for the literal string "http"
        condition:
            $s              // Rule matches if $s appears anywhere
    }
    """

    #Compile the rule so YARA can use it
    rules = yara.compile(source=rule_source)

    #Run the rule against the specified file
    return rules.match(path)


if __name__ == "__main__":
    #Convert to Path object and verify the file exists
    sample_path = Path(sample)

    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")

    else:
        #Apply the YARA scan
        matches = yara_scan(sample)

        #Print results
        print("=== YARA MATCHES ===")
        #Lists all rules that matched the file
        print(matches)     