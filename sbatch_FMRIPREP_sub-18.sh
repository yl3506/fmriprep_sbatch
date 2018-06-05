#!/bin/bash
#SBATCH --job-name=fmriprep
#SBATCH --nodes=1 --cpus-per-task=16  --tasks-per-node=2
#SBATCH --mem=50GB
#SBATCH --time=5-00:00:00
#SBATCH --mail-user=yichenli@mit.edu --mail-type=ALL
#SBATCH --output=logs/sbatchlog_FMRIPREP_stdout_%j.txt
#SBATCH --error=logs/sbatchlog_FMRIPREP_stderr_%j.txt
#SBATCH --qos=saxelab
chmod +x sbatchrun_FMRIPREP_sub-18.sh
srun ./sbatchrun_FMRIPREP_sub-18.sh