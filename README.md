# Fall 2026 Quantum Physics I Notebooks

This repository contains Jupyter notebooks for an undergraduate Quantum Physics I course for physics majors. The notebooks combine analytic work, short explanations, numerical experiments, and Python visualizations.

## Notebook Index

| Notebook | Topic |
| --- | --- |
| `NB01.ipynb` | Normalization, probability, expectation values, probability current, Ehrenfest's theorem |
| `NB02.ipynb` | Infinite square well and time-dependent states |
| `NB03.ipynb` | Quantum harmonic oscillator, ladder operators, wavefunctions, variational principle |
| `NB04.ipynb` | Bound states, finite wells, delta-function potentials, numerical root finding |

## Ways to View the Notebooks

You have several options. If you only want to read a notebook, the first two are usually easiest. If you need to edit, run, or submit work, use one of the local options.

### Option 1: View on GitHub

Click any `.ipynb` file in the repository. GitHub will render the notebook in the browser.

This is convenient for reading, but it is not interactive. You cannot run code cells or save your own answers this way.

### Option 2: View with nbviewer

If GitHub has trouble rendering a notebook, paste the notebook URL into:

<https://nbviewer.org/>

nbviewer is also read-only.

### Option 3: Open in Google Colab

Google Colab runs notebooks in the browser without installing Python locally:

<https://colab.research.google.com/>

In Colab, choose **File > Open notebook > GitHub**, then paste the repository URL. Colab is a good fallback if your local Python installation is not working, but file paths and package versions may differ slightly from a local setup.

### Option 4: Run Locally with JupyterLab

This is the recommended option for regular course work.

## Installing Python

Use Python 3.11 or newer. If you already have a working Python installation, you can skip to the setup instructions below.

### Recommended: Miniforge

Miniforge is a lightweight Python distribution that includes Conda-style environment management:

<https://conda-forge.org/download/>

After installing Miniforge, open a new terminal so that `conda` or `mamba` is available.

### Alternative: python.org

You can also install Python directly from:

<https://www.python.org/downloads/>

This works well with the `venv` instructions below.

### Alternative: Anaconda

Anaconda is a larger scientific Python distribution:

<https://www.anaconda.com/download>

It is fine to use if you already have it installed.

## Local Setup with venv

From the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name quantum-fall2026 --display-name "Quantum Fall 2026"
```

Then start JupyterLab:

```bash
jupyter lab
```

When the browser opens, select the kernel named **Quantum Fall 2026**.

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Local Setup with Conda or Mamba

From the repository folder:

```bash
conda env create -f environment.yml
conda activate quantum-fall2026
jupyter lab
```

If you use Mamba:

```bash
mamba env create -f environment.yml
mamba activate quantum-fall2026
jupyter lab
```

## Updating an Existing Environment

If the package list changes later in the semester:

```bash
python -m pip install -r requirements.txt --upgrade
```

or, for Conda/Mamba:

```bash
conda env update -f environment.yml --prune
```

## Working with Notebooks

Recommended workflow:

1. Pull or download the latest version of the repository.
2. Open the assigned notebook in JupyterLab, VS Code, or Colab.
3. Run cells from top to bottom.
4. Save your work frequently.
5. Export to PDF or HTML if requested by the instructor.

In JupyterLab, export options are under **File > Save and Export Notebook As**. PDF export may require a local LaTeX installation, so HTML export is often the simpler option unless PDF is specifically required.

## Using VS Code

VS Code can open and run `.ipynb` notebooks directly.

Install:

- VS Code: <https://code.visualstudio.com/>
- Python extension
- Jupyter extension

Then open this repository folder in VS Code and select the **Quantum Fall 2026** kernel, or the Python interpreter from `.venv` or the Conda environment.

## Troubleshooting

If a notebook says a package is missing, make sure your environment is active and reinstall the requirements:

```bash
python -m pip install -r requirements.txt
```

If Jupyter opens but the wrong Python environment is selected, use the kernel menu in the upper-right corner of the notebook and choose **Quantum Fall 2026**.

If plots do not appear, restart the kernel and run the notebook again from the first cell.

If PDF export fails, try exporting to HTML first. PDF export often depends on additional system software.

## Repository Contents

- `NB*.ipynb`: Course notebooks.
- `requirements.txt`: Python packages for `pip` and `venv` users.
- `environment.yml`: Conda/Mamba environment file.
- `.gitignore`: Local files that should not be committed.

## Notes for Students

Do not edit the original notebook if your instructor asks you to preserve a clean copy. Instead, make your own copy with your name or initials in the filename.

Example:

```text
NB02_lastname_firstname.ipynb
```

Keep backups of submitted work. A notebook is both code and document, so rerun it before submitting to make sure the saved output matches your answers.
