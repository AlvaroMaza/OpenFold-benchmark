#!/bin/bash
# Initial parameters taken from AlphaFold example expanse script
# Projects:
## Initial trial project for user jmduarte: "SDS154" (I took from my initial email)
## The "ACCESS Explore" project applied for benchmarking OpenFold on homomers: BIO230048 (ACCESS project name), TG-BIO230048 (ACCESS allocation id), SDS194 (Expanse project name)
#
# To find remaining credits use: expanse-client user jmduarte -p -r expanse_gpu
# To find Lustre project quota use: lfs quota -g sds194 -h /expanse/lustre/projects/sds194
#
# --partition set as gpu and not gpu-shared so that it is compatible with cuda:0 later
#
#SBATCH --job-name openfold
#SBATCH --output="openfold.%j.%N.log"
#SBATCH --error="openfold.%j.%N.log"
#SBATCH --account=SDS194
#SBATCH --time=12:00:00
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=gpu
#SBATCH --mem=40G
#SBATCH --constraint="lustre"



module load singularitypro/3.9

DATA_ROOT=/expanse/lustre/projects/sds194/jmduarte
OF_PARAMS=$DATA_ROOT/openfold_params
TEMPLATES_DIR=$DATA_ROOT/pdb_mmcif/mmcif_files
OF_SIF_FILE=$DATA_ROOT/singularity/openfold.sif

inDir=$1
alignments=/expanse/lustre/projects/sds194/amazamontesinos/alignments
outDir=/expanse/lustre/projects/sds194/amazamontesinos/output_models/$(basename $inDir)

echo "Start: $(date)"
# Note '--nv' is required so that singularity can use nvidia/cuda
singularity exec --nv \
--bind $TEMPLATES_DIR:/templates \
--bind $indDir:$inDir \
--bind $alignments:$alignments \
--bind $outDir:$outDir \
--bind $OF_PARAMS:/params \
$OF_SIF_FILE \
python3 /opt/openfold/run_pretrained_openfold.py \
    $inDir \
    /templates \
    --use_precomputed_alignments $alignments \
    --output_dir $outDir \
    --model_device "cuda:0" \
    --config_preset "model_1_ptm" \
    --save_outputs \
    --openfold_checkpoint_path /params/finetuning_ptm_2.pt \
    --cif_output

echo "Done:  $(date)"
python filter_pickle.py $outDir/predictions/
