# this script is to rearrange data files in 
# forrest dataset to allign with BIDS format
import os, json

# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids/'
os.chdir(main_directory)

# write dataset description in json
data = {}
data['BIDSVersion'] = []
data['BIDSVersion'].append("1.0.0")
data['License'] = []
data['License'].append("https://www.nature.com/articles/sdata201692#abstract")
data['Name'] = []
data['Name'].append("A studyforrest extension, simultaneous fMRI and eye gaze recordings during prolonged natural stimulation")
data['ReferencesAndLinks'] = []
data['ReferencesAndLinks'].append({"http://dx.doi.org/10.1038/sdata.2016.92"})


# get all subject folders in main directory
all_sub_folder = os.listdir(main_directory)
# iterate through all subjects to arrange files
for sub_folder in all_sub_folder:
	# enter current subject folder
	# create new folders ses-localizer and ses-movie
	# create new subfolder ses-localizer/func, anat (TBD)
	# and ses-movie/func, anat (TBD)
	# enter sub/func folder
	# iterate through all files in func 
	# move correspond files to ses-loc/func
	# move correspond files to ses-movie/func

	# cd to previous level anat folder
	# check if exists T1w_defacemask file
	# if so, change name to T12-defacemask
	# change name to ses-loc/movie
	
	# cd to main directory
	# copy sub/anat to sub/ses-movie
	# move file sub/anat to sub/ses-loc
	# cd to sub/ses-movie
	# change name of all files to ses-movie