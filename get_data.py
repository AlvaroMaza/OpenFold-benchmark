from queries import *
from utils import *

max_seq = 1600

if __name__ == "__main__":

    create_csv_file("ids.csv")
    for sym in [(2,'"C2"'),(3,'"C3"'),(4,'"C4"'),(5,'"C5"'),(6,'"C6"'),(4,'"D2"'),(6,'"D3"')]:
        print(sym[1])
        data = get_data_for_polymers(get_searchapi_data(search_query % sym))
                                     
        for poly in data:

          if len(poly['entity_poly']['pdbx_seq_one_letter_code_can'])*sym[0] < max_seq:
                name = poly['rcsb_id'][:-1].lower()+poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0]

                if folder_exists(name):
                    write_csv_file("ids.csv",name)
                    write_fasta([name,
                                 poly['rcsb_id'][-1],
                                 poly['rcsb_polymer_entity_container_identifiers']['auth_asym_ids'][0],
                                 poly['entity_poly']['pdbx_seq_one_letter_code_can'],
                                 sym[0]])

    

