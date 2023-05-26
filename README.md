<h1 align="center">OpenFold benchmark</h1>

<h3>Steps to replicate the benchmarck</h3>

<b>1. Run get_data.py</b>

If you want different type of data (include all stoichiometries for example), change the queries in queries.py so that you get the desired outputs.

<code>get_data.py</code> will create:
  1. A csv with the only ids
  2. A csv with the ids, symmetry, and sequence length of each protein 
  3. A folder with all the fasta files
  
This file is limited by the parameter max_seq, that excludes proteins bigger than a given limit. At the moment, this is set as 1600. When we dealt with bigger proteins, the gpus seemed not being able to handle them, and they ran out of memory.

<b>2. Run select_alignments.py (Optional)</b>

In case you don't want to work with the whole OpenProteinSet, you can filter the alignments of the fasta files you have with this script

<b>3. Send the folders with the fasta files and the aligments to expanse/lustre/projects/... </b>

<b>4. Run create_folders.py inside EXPANSE to create batches with the desired amount of fasta fyles </b>

Select a batch size of 550 (for example) by running <code>python create_folders.py 550</code>. It is set as 20 by default.


<b>5. Run parallel.sh </b>

This will submit a number of jobs using <code>run_of_inference.sh</code>

The way it works is the following, it takes as input the number of the batch you want to start with, and the number of jobs you want to send:
For example, if you run <code>bash parallel.sh 10 5</code> It will send 5 jobs, for batches 10, 11, 12, 13 and 14
The number of jobs is 1 if you don't specify it.

<ul>
<li>You may see that the jobs are waiting in the queue for a considerable amount of time. This happens because the job partition chosen in <code>run_of_inference.sh</code> is gpu and not gpu-shared. We changed this since in the parameters of OpenFold we allocate the job in cuda:0, but if we share the gpu this was not always availiable.</li>

<li>To reduce the size of the output pickle, filter_pickle is executed at the end of this script. It excludes the parts of the pickle that weighted the most. Be sure to have <code>filter_pickle.py</code> downloaded, or comment that line if you want the whole pickle output.</li>
</ul>

<b>6. Run parse_logs.py to get the times of inference and relaxation of all predictions in a JSON format</b>


<b>7. Run merge_batches.py to merge all the data from the batches into two single directories: </b>
   <ul>
  <li> output_directory_pkl </li>
  <li> output_directory_relaxed</li>

  </ul>
  
<b>8. Run qsalign.py to get the tsv files with the tm-score</b>
  
<b>9. Run merge_data.py to merge all the data from: </b>
  <ul>
  <li> ids.csv: it has the symmetry and sequence length of each protein </li>
  <li> times.json: it has the inference and relaxation time of each protein</li>
  <li> The ouput pickles that have the pLT, pAE, pLDDT,... of each prediction</li>
  </ul>

in a single dataframe.
  
