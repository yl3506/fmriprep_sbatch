#!/bin/bash
thisfolder = /mindhive/saxelab3/anzellotti/forrest/mask_tests/
sub = sub-18
template = /mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz
t1brain = /mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii
DOW="Tue"
cd thisfolder
module add openmind/ants/2.1.0-3.8bed08

echo 'before export'

antsRegistration --dimensionality 3 --float 0 \
        --output [/mindhive/saxelab3/anzellotti/forrest/mask_tests/pennTemplate_to_sub-18_,/mindhive/saxelab3/anzellotti/forrest/mask_tests/pennTemplate_to_sub-18_Warped.nii.gz] \
        --interpolation Linear \
        --winsorize-image-intensities [0.005,0.995] \
        --use-histogram-matching 0 \
        --initial-moving-transform [/mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii,/mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz,1] \
        --transform Rigid[0.1] \
        --metric MI[/mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii,/mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz,1,32,Regular,0.25] \
        --convergence [1000x500x250x100,1e-6,10] \
        --shrink-factors 8x4x2x1 \
        --smoothing-sigmas 3x2x1x0vox \
        --transform Affine[0.1] \
        --metric MI[/mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii,/mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz,1,32,Regular,0.25] \
        --convergence [1000x500x250x100,1e-6,10] \
        --shrink-factors 8x4x2x1 \
        --smoothing-sigmas 3x2x1x0vox \
        --transform SyN[0.1,3,0] \
        --metric CC[/mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii,/mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz,1,4] \
        --convergence [100x70x50x20,1e-6,10] \
        --shrink-factors 8x4x2x1 \
        --smoothing-sigmas 3x2x1x0vox \
        --verbose 1

echo 'command entered'
echo 'finished and exit'
exit