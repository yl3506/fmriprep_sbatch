import os

# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids/'
os.chdir(main_directory)
# get all subject folders in main directory
all_folder_names = os.listdir(main_directory)
os.chdir(main_directory+'sub-01/ses-movie/anat')
os.rename(main_directory+'sub-01/ses-movie/anat/sub-01_ses-movie_ses-movie_ses-movie_ses-movie_ses-movie_ses-movie_ses-movie_ses-movie_T1w-defacemask.nii.gz', main_directory+'sub-01/ses-movie/anat/sub-01_ses-movie_T1w-defacemask.nii.gz')
# os.rename(main_directory+'sub-02/ses-localizer/anat/sub-02_T1w-defacemask.nii.gz', main_directory+'sub-02/ses-localizer/anat/sub-02_ses-localizer_T1w-defacemask.nii.gz')
# os.rename(main_directory+'sub-02/ses-movie/anat/sub-02_ses-movie_ses-movie_T1w-defacemask.nii.gz', main_directory+'sub-02/ses-movie/anat/sub-02_ses-movie_T1w-defacemask.nii.gz')
for sub in all_folder_names:
	if sub == '.DS_Store' or sub == 'dataset_description.json' or sub == 'sub-01':
		continue
	# enter current subject folder
	os.chdir(main_directory+sub+'/ses-movie/anat')
	list_of_anat = os.listdir('.')
	for anat_file in list_of_anat:
		if 'ses-movie_ses-movie_' in anat_file:
			os.rename(anat_file, main_directory+sub+'/ses-movie/anat/'+sub+'_ses-movie_T1w-defacemask.nii.gz')
			print("renamed: "+main_directory+sub+'/ses-movie/anat/'+anat_file)
	# enter current subject folder
	os.chdir(main_directory+sub+'/ses-localizer/anat')
	list_of_anat2 = os.listdir('.')
	for anat_file2 in list_of_anat2:
		if 'defacemask' in anat_file2:
			os.rename(anat_file2, main_directory+sub+'/ses-localizer/anat/'+sub+'_ses-localizer_T1w-defacemask.nii.gz')
			print("renamed: "+main_directory+sub+'/ses-localizer/anat/'+anat_file2)
		else:
			continue