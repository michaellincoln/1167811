# Huntington's Disease Dataset Analysis

## Overview
Comprehensive data analysis of Huntington's Disease patient data including data preprocessing, exploratory data analysis, and identification of research opportunities.

## Key Features
- **48,536 patients** across all disease stages
- **13 clinical variables** including genetic, motor, cognitive, and molecular features
- Missing data analysis (25% cognitive assessments)
- Outlier detection using IQR and Z-score methods
- Comprehensive correlation analysis of clinical relationships

## Key Findings
- Strong correlation between HTT CAG repeat length and disease severity
- Age-related brain volume loss patterns identified  
- Genetic burden correlates with functional capacity decline
- Balanced patient representation across disease stages

## Files
- `Assignment2-Huntington_Disease_Analysis.ipynb` - Main analysis notebook
- `data/Huntington_Disease_Dataset.csv` - Patient dataset

## Setup

### Option 1: Use the existing venv
```bash

# Activate the existing virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies (if needed)
pip install -r requirement.txt

# Run analysis
jupyter lab Assignment2-Huntington_Disease_Analysis.ipynb

```

### Option 2: Create the new conda environment
```bash
# Create environment
conda create -n huntington-analysis python=3.11
conda activate huntington-analysis

# Install dependencies
pip install -r requirement.txt

# Run analysis
jupyter lab Assignment2-Huntington_Disease_Analysis.ipynb
```

## Environment Management
- `deactivate` - Exit current environment
- `jupyter lab` - Opens JupyterLab with file browser
- `jupyter notebook` - Opens classic Jupyter Notebook interface

## Research Questions Identified
- Genetic prediction models for disease onset timing
- Biomarker development for disease progression
- Clinical trial patient stratification approaches
- Personalized treatment planning optimization

## Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy
