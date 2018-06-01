#!/bin/bash
participant="sub-17"
echo "participant: $participant"
exp_path="/mindhive/saxelab3/anzellotti/forrest"
sourcedir="${exp_path}/forrest_bids"
outdir="${exp_path}/derivatives"
workdir="${exp_path}/work"
module add openmind/singularity/2.4.5
cwd=/mindhive/saxelab3/anzellotti/software/preproc_fmriprep
DOW="Fri"
# SINGSCRATCH="/om/scratch//anzellot/fmriprep"
SINGSCRATCH="${exp_path}/scratch_singularity/fmriprep"
if [ ! -d "$SINGSCRATCH" ]; then
	mkdir -p "${SINGSCRATCH}"
fi
export SINGULARITY_CACHEDIR="${SINGSCRATCH}"
echo "FMRIPREP - Participant: ${participant}"
echo "experiment path:        ${exp_path}"
cd "${exp_path}" || exit
echo "output path:            ${outdir}"
cd "${outdir}" || exit
echo "source path:            ${sourcedir}"
cd "${sourcedir}" || exit
echo "work path:              ${workdir}"
cd "${cwd}" || exit
echo "Launching SingCon in:   ${cwd}"
echo ''
# echo 'COMMAND BEING RUN: '

singularity exec -B /mindhive/saxelab3/anzellotti:/mindhive/saxelab3/anzellotti docker://poldracklab/fmriprep:1.0.11 bash -c \
"ldconfig && \
fmriprep \
--participant_label ${participant} \
--nthreads 16 \
--omp-nthreads 16 \
--mem_mb 200000 \
--ignore slicetiming \
--bold2t1w-dof 9 \
--output-space T1w template fsnative fsaverage \
--template MNI152NLin2009cAsym \
--fs-no-reconall \
--fs-license-file /mindhive/saxelab3/anzellotti/software/preproc_fmriprep \
--write-graph \
${workdir} \
${sourcedir} \
${outdir} \
participant"
echo ''
echo 'sbatchrun FINISHED. exiting.'
exit
