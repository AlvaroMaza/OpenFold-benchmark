import os
import shutil


def folder_exists(name,path = "D:/data/openfold/openproteinset/pdb/%s"):
    path = path % name
    return os.path.isdir(path)

def write_csv_file(file, data):
    with open(file, 'a') as the_file:
        the_file.write(data+ "\n")
            

def create_csv_file(file):
    with open(file, 'w') as csvfile: 
        print("IDs table created")
        csvfile.write("ID\n")


def write_fasta(input, folder = 'C:/Users/alvar/Desktop/PDB/benchmark/get_ids/fasta_files'):
    
    if os.path.exists(folder) and os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder) 


    file = open(os.path.join(folder,input[0]+".fasta"), "w")
    string = ">" + input[0] + " | " + "Assembly ID: "+ input[1] +  " | " + "Author ID: "+ input[2] +  "\n" +input[3] + "\n"
    file.write(input[4]*string)
    file.close()