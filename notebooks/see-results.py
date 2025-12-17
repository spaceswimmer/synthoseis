import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def plot_3d_slices(array_3d, seismic):
    """
    Interactive plot to cycle through slices of a 3D array along axis=1
    """
    fig, axs = plt.subplots(1,2)
    plt.subplots_adjust(bottom=0.2)
    
    # Initial slice
    initial_slice = 0
    im1 = axs[0].imshow(array_3d[:, initial_slice, :], cmap='viridis', aspect='auto')
    axs[0].set_title(f'Slice {initial_slice}')
    im2 = axs[1].imshow(seismic[:, initial_slice, :], cmap='seismic', aspect='auto')
    axs[1].set_title(f'Slice {initial_slice}')

    
    # Slider
    ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
    slider = Slider(ax_slider, 'Slice', 0, array_3d.shape[1] - 1, valinit=0, valfmt='%d')
    
    def update(val):
        slice_num = int(slider.val)
        im1.set_array(array_3d[:, slice_num, :])
        axs[0].set_title(f'Slice {slice_num}')
        im2.set_array(seismic[:, slice_num, :])
        axs[1].set_title(f'Slice {slice_num}')
        fig.canvas.draw()
    
    slider.on_changed(update)
    plt.show()


non_zero = np.load('../../data/non_zero.npy')
ind = 28
print(non_zero[12])
temp = np.load(f"..\scratch\synthoseis_example_test_mode_\seismic__2025.76439254_1\{non_zero[ind]}")
seismic = np.load(f"..\scratch\synthoseis_example_test_mode_\seismic__2025.76439254_1\{non_zero[54]}")
plot_3d_slices(temp.T, seismic.T)
# for i in range(len(non_zero)):
#     print(f'{i} - {non_zero[i]}')