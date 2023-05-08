from queries import *
from utils import *

max_seq = 1600


db_location = "D:/data/openfold/openproteinset/pdb/%s"
fasta_folder_output = 'C:/Users/alvar/Desktop/PDB/benchmark/get_ids/fasta_files'

if __name__ == "__main__":

    create_csv_file("ids_final.csv")
    for sym in [(2,'"C2"'),(3,'"C3"'),(4,'"C4"'),(5,'"C5"'),(6,'"C6"'),(4,'"D2"'),(6,'"D3"')]:
        print(sym[1])
        data = get_data_for_polymers(get_searchapi_data(search_query % sym))
                                     
        for poly in data:
            
            seq_length = len(poly['entity_poly']['pdbx_seq_one_letter_code_can'])*sym[0]
            if seq_length < max_seq:
                name = poly['rcsb_id'][:-1].lower()+poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0]

                if folder_exists(name,db_location):
                    write_csv_file("ids_final.csv",name,sym[1][1:-1], seq_length)
                    write_fasta([name,
                                 poly['rcsb_id'][-1],
                                 poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0],
                                 poly['entity_poly']['pdbx_seq_one_letter_code_can'],
                                 sym[0]],
                                 fasta_folder_output)

    

