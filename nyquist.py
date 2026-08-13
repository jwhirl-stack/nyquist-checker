# Program that takes a sampling rate and tells you the Nyquist Frequency, and warns if a signal frequency would alias.

def nyquist(sampling_frequency):
    return sampling_frequency * 0.5

samp_freq = float(input("Sampling rate: "))
nyquist_freq = nyquist(samp_freq)

print(f'Nyquist frequency: {nyquist_freq} Hz')

targ_freq = float(input("Target frequency: "))

if targ_freq < nyquist_freq:
  print(f'{targ_freq} Hz is SAFE (below Nyquist)')
elif targ_freq == nyquist_freq:
  print(f'{targ_freq} Hz is AT the Nyquist limit (critical boundary)')
else:
  print(f'{targ_freq} Hz will ALIAS below Nyquist')

