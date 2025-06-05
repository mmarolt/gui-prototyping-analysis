[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13686834.svg)](https://doi.org/10.5281/zenodo.13686834)

# Effective GUI generation: Leveraging LLMs for Automated GUI Prototyping

The supplementary material of our submission to the HICSS-58 is structured as follows:
- **gui_generation**
  - **prototyping.ipynb:** Notebook that was used to generate the GUI prototypes
  - **prompts.py:** All 5 different prompts, that were evaluated in the study
  - **dataset_creation.ipynb:** Notebook that was used to generate the dataset of GUI descriptions
  - **annotations.csv:** contains all annotations that where made for the evaluation of our generated GUI prototypes
    - the columns for the annotated scores have the following format: {UI number of the Text summary, the GUI is based on}/{Metric}/{Prompting approach}
  - **dataset.csv:** contains the generated dataset of GUI descriptions
  - **generated_guis:** contains all GUIs that have been generated for the evaluation
  - **rico_gui:** contains the sampled rico GUIs, that were used as a base for our dataset

<img width="1321" alt="GUI Generation Approaches v4" src="https://github.com/user-attachments/assets/4b079d4d-0775-4495-bd71-3631685214fb">
