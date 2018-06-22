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
-bash-4.2$ cat sbatchrun_FMRIPREP_sub-16_sing.sh
#!/bin/bash
exp_path="/mindhive/saxelab3/anzellotti/forrest"
DOW="Wed"
cd "/mindhive/saxelab3/anzellotti/software/preproc_fmriprep"
module add openmind/singularity/2.4.5
SINGSCRATCH="${exp_path}/scratch_singularity/fmriprep"
if [ ! -d "$SINGSCRATCH" ]; then
        mkdir -p "${SINGSCRATCH}"
fi
echo 'before export'
export SINGULARITY_CACHEDIR="${SINGSCRATCH}"
export SINGULARITY_LOCALCACHEDIR="${SINGSCRATCH}"

echo 'start all instances'
singularity instance.start -B /mindhive/saxelab3/anzellotti:/mindhive/saxelab3/anzellotti fmriprep1-1-1.simg web16

singularity exec instance://web16 bash -c \
"fmriprep \
--participant_label sub-16 \
--nthreads 16 \
--omp-nthreads 16 \
--mem_mb 200000 \
--ignore slicetiming \
--bold2t1w-dof 9 \
--output-space T1w template fsnative fsaverage \
--template MNI152NLin2009cAsym \
--fs-no-reconall \
--fs-license-file /mindhive/saxelab3/anzellotti/software/preproc_fmriprep/license.txt \
--write-graph \
-w /mindhive/saxelab3/anzellotti/forrest/work \
/mindhive/saxelab3/anzellotti/forrest/forrest_bids \
/mindhive/saxelab3/anzellotti/forrest/derivatives \
participant"
echo 'command entered'

singularity instance.stop web16
echo 'instance stopped'
echo 'finished and exit'
exit