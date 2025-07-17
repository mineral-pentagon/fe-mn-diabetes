# Fe/Mn Diabetes Research

## Overview

This repository contains Python code and analysis exploring the relationship between the iron-to-manganese ratio (Fe/Mn) and diabetes prevalence, based on NHANES datasets.

We propose a scientific hypothesis that an elevated Fe/Mn ratio combined with iron-dependent fungal microecology plays a causal role in the development of type 2 diabetes.

## Key Findings

- Analysis of NHANES 2017-2018 data shows a **positive exponential correlation** between Fe/Mn ratio and diabetes prevalence.
- Single mineral levels (iron or manganese alone) do not display simple correlations with diabetes.
  
## Hypothesis (Axiom)

**An elevated iron-to-manganese ratio (Fe/Mn), together with iron-dependent fungal microecology, causally drives type 2 diabetes onset and progression.**

This hypothesis is supported by statistical associations and biological plausibility, and it offers a simplified unifying framework connecting mineral metabolism, microecology, and metabolic disease.

## Potential Implications

- New biomarkers for diabetes risk stratification (e.g., blood or hair Fe/Mn ratio)
- Novel intervention strategies targeting mineral balance and fungal microbiota
- Integrative models combining mineralomics, mycology, and metabolism for diabetes prevention and treatment

## Repository Contents

- Data processing and analysis scripts using NHANES datasets
- Visualization notebooks showing diabetes prevalence vs mineral ratios
- Statistical modeling for multivariate diabetes risk surfaces

## How to Reproduce

1. Download NHANES datasets for 2017-2018 (FETIB_J, PBCD_J, GHB_J, etc.)
2. Install required Python packages:
   ```bash
   pip install pyreadstat pandas matplotlib scikit-learn
