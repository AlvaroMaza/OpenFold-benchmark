#!/bin/bash

start=$1
n=${2:-8}

for (( i=$start ; i<$start+$n ; i++ ))
do
	sbatch $(pwd)/run_of_inference_expanse.sh /expanse/lustre/projects/sds194/amazamontesinos/batches/batch"$i" 
done
exit
