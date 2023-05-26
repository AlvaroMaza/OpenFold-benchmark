import os
import glob

jar_path = "C:/Users/alvar/Desktop/PDB/qs-align_1.2-SNAPSHOT.jar"
cif_directory = "C:/Users/alvar/Desktop/PDB/data/output_directory_relaxed"
output_directory = "C:/Users/alvar/Desktop/PDB/OpenFold-benchmark/qsalign1"

# Get a list of all CIF files in the directory
cif_files = glob.glob(os.path.join(cif_directory, "*.cif"))

# Loop through each CIF file
for cif_file in cif_files:
    cif_filename = os.path.basename(cif_file)
    cif_name = cif_filename[:4]  # Extract the file name without extension
    output_file = f"{cif_filename.split('-', 1)[0]}.tsv"  # Output file name based on the CIF file name
    
    # Construct the command to execute
    command = f"java -jar {jar_path} -t {cif_name} -q {cif_file} -o {os.path.join(output_directory, output_file)}"
    
    # Execute the command
    os.system(command)

    print(f"Executed for CIF file: {cif_filename}.")

print("All CIF files processed.")