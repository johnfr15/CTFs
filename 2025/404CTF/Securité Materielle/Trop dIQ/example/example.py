import numpy as np
import matplotlib.pyplot as plt

# Load the IQ data: complex128 means each sample is two float64 values (I and Q)
iq_data = np.fromfile("./reconstructed.iq", dtype=np.complex128)

# Let's define a sampling rate (as you previously stated, it's 44100 Hz)
fs = 44100
t = np.arange(len(iq_data)) / fs  # Time vector

# Take a subset for visualization purposes (e.g., first 1000 samples)
subset = iq_data[:1000]
time_subset = t[:1000]

# Compute the Fourier Transform
fft_result = np.fft.fft(iq_data)
freqs = np.fft.fftfreq(len(iq_data), 1/fs)

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Time domain: real part of the signal
axs[0].plot(time_subset, subset.real)
axs[0].set_title("Signal (Time Domain - Real Part)")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Amplitude")
axs[0].grid(True)

# Frequency domain: magnitude spectrum
axs[1].plot(freqs[:len(freqs)//2], np.abs(fft_result[:len(freqs)//2]))
axs[1].set_title("Fourier Transform (Frequency Domain)")
axs[1].set_xlabel("Frequency (Hz)")
axs[1].set_ylabel("Magnitude")
axs[1].grid(True)

plt.tight_layout()
plt.show()
