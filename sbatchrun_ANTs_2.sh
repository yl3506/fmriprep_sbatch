#!/bin/bash
dim=3 # image dimensionality
module add openmind/ants/2.1.0-3.8bed08
ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS=4 # controls multi-threading
export ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS
f="/mindhive/saxelab3/anzellotti/forrest/mask_tests/forrestFunctionalSpace_skullStrip.nii.gz"
m="/mindhive/saxelab3/anzellotti/forrest/mask_tests/kanparcelSpace_skullStrip.nii"
# fixed and moving image file names and fixed image mas, here the fixed image is the template
if [[ ${#f} -eq 0 ]] ; then #CLI feedback when parameters are not given correctly to the script
echo usage is
echo $0 fixed.nii.gz moving.nii.gz fixed_brain_mask.nii.gz
exit
fi
if [[ ! -s $f ]] ; then echo no fixed $f ; exit; fi
if [[ ! -s $m ]] ; then echo no moving $m ;exit; fi
reg=antsRegistration # path to antsRegistration
its=10000x1111x5 #iterations per scale for affine step
percentage=0.25 #percentage of voxels sampled for evaluating the metric
syn="20x20x0,0,5” #iterations per scale and stopping criterion
nm=BBM #naming prefix
imgs=" $f, $m ” #variable specifying the fixed and moving images
if [[ ! -s ${nm}0GenericAffine.mat ]] ; then #run if the .mat file does not exist
$reg -d $dim -r [ $imgs ,1] ¥ #initialize based on aligning centroids of voxel intensities
 -m mattes[ $imgs , 1 , 32, regular, 0.05 ] ¥ #metric
 -t translation[ 0.1 ] ¥ #transformation type
 -c [1000,1.e-8,20] ¥ #no. of iterations and stopping criteria
 -s 4vox ¥ #smoothing sigmas
 -f 6 -l 1 ¥ #scale factors 6= 1/6 original size + -l estimate learning rate
 -m mattes[ $imgs , 1 , 32, regular, 0.1 ] ¥
 -t rigid[ 0.1 ] ¥
 -c [1000x1000,1.e-8,20] ¥ #two scales used for rigid
 -s 4x2vox ¥
 -f 4x2 -l 1 ¥
 -m mattes[ $imgs , 1 , 32, regular, 0.1 ] ¥
 -t affine[ 0.1 ] ¥
 -c [$its,1.e-8,20] ¥ #three scales used for affine
 -s 4x2x1vox ¥
 -f 3x2x1 -l 1 ¥
 -m mattes[ $imgs , 1 , 32 ] ¥
 -t SyN[ .20, 3, 0 ] ¥
 -c [ $syn ] ¥
 -s 1x0.5x0vox ¥
 -f 4x2x1 -l 1 -u 1 -z 1 --float 1 ¥ #-u use histogram matching, -z combine output transforms (linear/nonlinear), -x use a mask during nonlinear step
 -o [${nm},${nm}_diff.nii.gz,${nm}_inv.nii.gz] #specify output prefix, forward and reverse file names
antsApplyTransforms -d $dim -i $m -r $f -n linear -t ${nm}1Warp.nii.gz -t
${nm}0GenericAffine.mat -o ${nm}_warped.nii.gz --float 1 #example of applying the calculated linear+nonlinear transforms to input data
fi
