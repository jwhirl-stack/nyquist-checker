# Nyquist & Sampling-Rate Checker

A light Python command-line utility that computes the Nyquist frequency for a given sampling rate and determines whether a target signal frequency will undergo aliasing.

## Features

- **Nyquist Calculation:** Determines $f_{Nyquist} = \frac{f_{s}}{2}$ from any user-defined sampling rate.
- **Boundary Handling:** Distinguishes between safe frequencies, signals right at the Nyquist limit, and frequencies that will alias.
- **Zero Dependencies:** Built entirely with native Python features.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Open your terminal and run:

python nyquist.py

---

## Example Output

```text
Sampling rate: 44100
Nyquist frequency: 22050.0 Hz

Target frequency: 28000
28000.0 Hz will ALIAS below Nyquist
```
