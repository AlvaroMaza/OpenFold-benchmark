import os
import shutil


def folder_exists(name,path):
    path = path % name
    return os.path.isdir(path)

def write_csv_file(file, data, sym,seq_length):
    with open(file, 'a') as the_file:
        the_file.write(data + "," + sym +  "," + str(seq_length) + "\n")
            

def create_csv_file(file):
    with open(file, 'w') as csvfile: 
        print("Data table created")
        csvfile.write("ID,symmetry,seq_length\n")


def write_csv_ids(file, data):
    with open(file, 'a') as the_file:
        the_file.write(data + "\n")
            

def create_csv_ids(file):
    with open(file, 'w') as csvfile: 
        print("IDs table created")
        csvfile.write("ID\n")

def write_fasta(input, folder):
    
    file = open(os.path.join(folder,input[0]+".fasta"), "w")
    string = ">" + input[0] + " | " + "Assembly ID: "+ input[1] +  " | " + "Author ID: "+ input[2] +  "\n" +input[3] + "\n"
    file.write(input[4]*string)
    file.close()