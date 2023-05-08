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
        print("IDs table created")
        csvfile.write("ID,symmetry,seq_lenght\n")


def write_fasta(input, folder):
    
    if os.path.exists(folder) and os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder) 


    file = open(os.path.join(folder,input[0]+".fasta"), "w")
    string = ">" + input[0] + " | " + "Assembly ID: "+ input[1] +  " | " + "Author ID: "+ input[2] +  "\n" +input[3] + "\n"
    file.write(input[4]*string)
    file.close()