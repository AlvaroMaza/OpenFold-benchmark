from queries import *
from utils import *

min_seq = 20
max_seq = 1600


db_location = "D:/data/openfold/openproteinset/pdb/%s"
fasta_folder_output = 'C:/Users/alvar/Desktop/PDB/data/fasta_files_new'

if __name__ == "__main__":

    #create the two csv files
    create_csv_ids("ids.csv")
    create_csv_file("data.csv")

    for sym in [(2,'"C2"'),(3,'"C3"'),(4,'"C4"'),(5,'"C5"'),(6,'"C6"'),(4,'"D2"'),(6,'"D3"')]:
        print(sym[1])

        data = get_data_for_polymers(get_searchapi_data(search_query % sym))
                                     
        for poly in data:
            
            seq_length = len(poly['entity_poly']['pdbx_seq_one_letter_code'])*sym[0]

            feature_summary = poly['polymer_entity_instances'][0]['rcsb_polymer_instance_feature_summary']
            for feature in feature_summary:
                if feature["type"] == "UNOBSERVED_RESIDUE_XYZ":
                    coverage = feature["coverage"]

            #consider changing the parameter for min_seq so that it is only for the sequence length
            #do not change the way the max_seq is calculated, we did it that way because otherways openfold crashed because of the protein size
            #mult_seq_length = len(poly['entity_poly']['pdbx_seq_one_letter_code'])*sym[0]
            #seq_length = len(poly['entity_poly']['pdbx_seq_one_letter_code'])

            if (seq_length < max_seq and (seq_length > min_seq) and 
                ('X' not in poly['entity_poly']['pdbx_seq_one_letter_code']) and 
                ('(' not in poly['entity_poly']['pdbx_seq_one_letter_code']) and
                coverage<0.2):

                name = poly['rcsb_id'][:-1].lower()+poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0]

                if folder_exists(name,db_location):
                    write_csv_ids("ids.csv",name)
                    write_csv_file("data.csv",name,sym[1][1:-1], seq_length)
                    write_fasta([name,
                                 poly['rcsb_id'][-1],
                                 poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0],
                                 poly['entity_poly']['pdbx_seq_one_letter_code'],
                                 sym[0]],
                                 fasta_folder_output)

    

