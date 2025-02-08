import scipy.io
import numpy as np
data = scipy.io.loadmat("dataset.mat")
segment_length = 6000 
def segment_signal(signal, segment_length):
    num_segments = len(signal) // segment_length 
    segments = [signal[i * segment_length:(i + 1) * segment_length] for i in range(num_segments)]
    return np.array(segments)
new_data = {}
for key in ['normal', 'inner', 'roller', 'outer']:
    original_signal = data[key].flatten()  
    segmented_signals = segment_signal(original_signal, segment_length)  
    new_data[key] = segmented_signals 
scipy.io.savemat("Newdataset.mat", new_data)

print("Dataset augmentation completed. New dataset saved as 'Newdataset.mat'.")
