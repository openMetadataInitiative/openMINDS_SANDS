import nibabel as nib
import numpy as np
# Load the NIfTI file
nifti_img = nib.load("/home/kiwitz1/Downloads/OASIS-TRT-20_jointfusion_DKT31_CMA_label_probabilities_in_MNI152_v2.nii" )

# Print basic information about the image
print('Image shape:', nifti_img.shape)
print('Image affine:\n', nifti_img.affine)
print('Image data type:', nifti_img.get_data_dtype())

# Get the data array from the image
data = nifti_img.get_fdata()

# Print basic statistics about the data
print('Data shape:', data.shape)
print('Data minimum:', data.min())
print('Data maximum:', data.max())
print('Data mean:', data.mean())

# Get the label probabilities and labels
label_probs = np.argmax(data, axis=-1)
labels = np.unique(label_probs)

# Print the label probabilities and their respective labels
for label in labels:
    label_prob = np.mean(data[label_probs == label])
    print(f'Label {label}: {label_prob:.4f}')