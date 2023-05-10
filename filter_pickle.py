import pickle
import os
import sys

dir = sys.argv[1]

for file in os.listdir(dir):
    if file.endswith(".pkl"):
        path = os.path.join(dir,file)
        data = pickle.load(open(path, "rb"))
        exclude_keys = {'aligned_confidence_probs','distogram_logits',
                        'msa','pair'}
        new_data = {k: data[k] for k in set(list(data.keys())) - exclude_keys}
        pickle.dump(new_data, open(path, "wb"))
