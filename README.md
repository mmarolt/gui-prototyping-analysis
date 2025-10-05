# A comparative analysis of methods for generating graphical user interfaces from user requirements

This repository contains code and resources for the comparative analysis of automatic methods to generate graphical user interfaces (GUIs) from user requirements, focusing on mobile applications. It provides a framework to transform textual or visual descriptions of user needs into working HTML prototypes and evaluates the quality of generated GUIs using quantitative metrics.

## Overview

The project implements and compares several prompt-driven and chain-based approaches for GUI prototyping. Given a description of a desired mobile app page (either as text or derived from an image), various methods translate the requirements step-by-step into UI elements, layout structures, and ultimately HTML/CSS code. The workflow is primarily implemented in Jupyter Notebooks and Python scripts.

### Key Features

- **Prompt-based GUI Generation:** Uses large language models (LLMs) and carefully designed prompts to convert requirements into code, including intermediate steps such as:
    - Extracting visible functionalities from descriptions.
    - Generating lists of UI elements.
    - Structuring the UI layout.
    - Producing HTML and inline CSS code optimized for mobile viewports.

- **Multiple Prototyping Chains:** Implements several strategies (e.g., "instruction", "pd_zs", "pd_fs", "ref_instruction") to analyze and refine requirements, providing alternative methods for GUI generation.

- **Dataset Creation:** Tools for creating datasets by describing mobile app screenshots and mapping them to requirements, summaries, or UI elements.

- **Evaluation Metrics:**
    - **Quantitative Metrics:**
        - **SSIM (Structural Similarity Index):** Measures visual similarity between reference images and generated GUIs.
        - **DOM Complexity:** Quantifies HTML DOM element count.
        - **Layout Area:** Sums bounding boxes of UI elements.
    - **Qualitative Metrics:**
        - **Online Questionnaire:** Includes code for an expert-driven evaluation questionnaire to assess compliance, appropriateness, intuitiveness, and simplicity of generated GUIs. The questionnaire is implemented in `index.html`, `script.js`, `style.css`, and Netlify configuration files.

## Repository Structure

- `prototyping.ipynb`: Main notebook for running GUI generation methods and chains.
- `prompts.py`: Contains prompt templates for each step of the prototyping process.
- `dataset_preprocesing.ipynb`: Scripts for dataset analysis and preprocessing.
- `dataset_creation.ipynb`: Scripts for creating description datasets of from images.
- `gui_evaluation.ipynb`: Notebook for evaluating generated GUIs using defined metrics.
- `index.html`, `script.js`, `style.css`, Netlify files: Implements the online questionnaire for expert evaluation of GUIs.
- Other supporting files for data processing and metric computation.

## Usage

1. **Prepare a dataset:**
    - Use `dataset_creation.ipynb` to generate requirement descriptions from mobile app screenshots.

2. **Run prototyping chains:**
    - Use `prototyping.ipynb` to apply different LLM-based chains for GUI generation from requirements.

3. **Evaluate GUIs (Quantitative):**
    - Use `gui_evaluation.ipynb` to compute metrics such as SSIM, DOM complexity, and layout area for each generated prototype.

4. **Evaluate GUIs (Qualitative):**
    - Deploy the questionnaire (using Netlify or similar) and invite experts to rate generated GUIs based on compliance, appropriateness of components, and usability.

5. **Compare and analyze:**
    - Summarize results and compare methods based on both quantitative and qualitative criteria.

## Technologies

- **Jupyter Notebook** (primary interface)
- **Python** (core logic and metric computation)
- **HTML/CSS/JavaScript** (prototype generation and questionnaire)
- **Netlify** (online deployment of the questionnaire)
- **Large Language Models** (prompt execution via LangChain)

## Example Evaluation Criteria

**Quantitative:**
- SSIM (visual similarity)
- DOM Complexity
- Layout Area

**Qualitative (via questionnaire):**
- Compliance with requirements
- Appropriateness of components
- Intuitiveness and simplicity of navigation and usage


## License

This project is intended for research and educational purposes.

## Acknowledgments

The repository leverages open-source tools and libraries for LLM interfacing, data processing, and image analysis.