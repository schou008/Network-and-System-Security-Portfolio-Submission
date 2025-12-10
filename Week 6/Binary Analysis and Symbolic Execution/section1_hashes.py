#section1_hashes.py
#Provides hashing algorithms
import hashlib            
#Safer file-path handling
from pathlib import Path 

#Path to the file to analyse
sample = r"C:\Users\Saqib\Downloads\test.txt"

def compute_hashes(path):
    """
    Compute multiple cryptographic hashes for a given file.
    Supported algorithms: MD5, SHA1, SHA256.
    Returns a dictionary of {algorithm : hash_value}.
    """
    #List of hash functions to compute
    algos = ["md5", "sha1", "sha256"]  
    #Store results
    output = {}                         

    for a in algos:
        #Create a hash object (e.g., MD5, SHA1, SHA256)
        h = hashlib.new(a)             

        #Open file in binary mode so hashing works correctly
        with open(path, "rb") as f:
            #Read entire file and update hash object
            h.update(f.read())          
        #Convert raw hash to readable hex
        output[a] = h.hexdigest()      

    return output                       


if __name__ == "__main__":
    #Convert file path string to a Path object
    sample_path = Path(sample)

    #Check if file exists before hashing
    if not sample_path.is_file():
        print(f"ERROR: File not found at {sample}")

    else:
        #Compute MD5, SHA1, SHA256
        hashes = compute_hashes(sample)  

        print("=== HASHES ===")
        # Print each hash nicely
        for k, v in hashes.items():
            print(f"{k.upper()}: {v}")
