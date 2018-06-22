#!/bin/bash
#SBATCH --job-name=fmriprep
#SBATCH --nodes=1 --cpus-per-task=16  --tasks-per-node=1
#SBATCH --mem=200GB
#SBATCH --time=5-00:00:00
#SBATCH --mail-user=yichenli@mit.edu --mail-type=ALL
#SBATCH --output=logs/sbatchlog_FMRIPREP_stdout_%j.txt
#SBATCH --error=logs/sbatchlog_FMRIPREP_stderr_%j.txt
#SBATCH --qos=saxelab
chmod +x sbatchrun_FMRIPREP_sub-16_sing.sh
srun ./sbatchrun_FMRIPREP_sub-16_sing.sh