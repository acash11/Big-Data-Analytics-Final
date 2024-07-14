import numpy as np
import matplotlib.pyplot as plt

# Define a sample signal (e.g., a sine wave with added noise)
n = 128  # number of points
t = np.linspace(0, 1, n, endpoint=False)  # time vector
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(n)  # 5 Hz sine wave + noise

# Compute the n-point DFT
dft = np.fft.fft(signal)

# Number of coefficients to keep
k = 3

# Zero out all but the first k coefficients
dft_truncated = np.zeros_like(dft)
dft_truncated[:k] = dft[:k]
print(dft_truncated)

# Reconstruct the signal from the truncated DFT
reconstructed_signal = np.fft.ifft(dft_truncated)
print(reconstructed_signal)

# Plot the original and reconstructed signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Original Signal')
plt.title('Original Signal')
plt.subplot(2, 1, 2)
plt.plot(t, reconstructed_signal.real, label='Reconstructed Signal (first 10 coefficients)')
plt.title('Reconstructed Signal (first 10 coefficients)')
plt.tight_layout()
plt.show()