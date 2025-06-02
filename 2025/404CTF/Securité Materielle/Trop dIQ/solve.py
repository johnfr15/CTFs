import numpy as np
from scipy.io.wavfile import write

# ========== STEP1: Inverse FFT et sauvegarde ==========
# Charger les données : deux float64 par échantillon (I + Q)
chall_data = np.fromfile('./resources/chall.iq', dtype=np.float64)

# Convertir en tableau de complexes
iq_samples = chall_data[::2] + 1j * chall_data[1::2]

reconstructed = np.fft.ifft(iq_samples)

# Reconversion en float64 intercalés (I, Q, I, Q, ...)
original = np.empty(2 * len(reconstructed), dtype=np.float64)
original[0::2] = reconstructed.real
original[1::2] = reconstructed.imag

# Sauvezgarde dans un nouveau fichier
original.tofile('reconstructed.iq')
print("✅ Inverse FFT appliquée. Fichier sauvegardé sous 'reconstructed.iq'")




# ========== STEP2: Démodulation et sauvegarde en WAV ==========
# Paramètres
iq_file = "reconstructed.iq"
output_wav = "output.wav"
sample_rate = 44100  # Hz

# Normalisation
raw_data = np.fromfile(iq_file, dtype=np.complex128)
raw_data /= np.max(np.abs(raw_data))
audio_signal = (raw_data * 32767).astype(np.int16)

# Sauvegarde en WAV
write(output_wav, sample_rate, audio_signal)
print("Fichier WAV généré :", output_wav)