# Class Notes — 24 September 2026

PHYS 3316 Quantum Physics I class notes covering Hilbert-space vectors,
two-state Hamiltonians, Pauli matrices, basis rotations, coherent Rabi
oscillations, operator identities, unitary transformations, the
Schrieffer–Wolff construction, and continuous SU(2) operator rotations.

## Contents

- `ClassNotes_24_Sept_2026.tex` — LaTeX source for the handout
- `figures/rabi_oscillations.pdf` — generated Rabi-oscillation figure
- `code/make_rabi_figure.py` — reproducible figure-generation script
- `notes/Handwritten_2026-09-24_140801.pdf` — original scanned notes

## Build

Regenerate the figure from this directory with Python and ReportLab:

```bash
python3 code/make_rabi_figure.py
```

Then compile the handout with a standard LaTeX engine, for example:

```bash
pdflatex ClassNotes_24_Sept_2026.tex
```
