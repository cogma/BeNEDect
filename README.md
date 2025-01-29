# BeNEDect (Benchmark for Numerical Error Detection task)

## Introduction
This repository contains our BeNEDect dataset, a Benchmark for Numerical Error Detection task, which is introduced in the following research paper:

Development of Numerical Error Detection Tasks to Analyze the Numerical Capabilities of Language Models (Sakamoto et al., COLING 2025)


## Contents



## Data Overview



## Example



## Licence
BeNEDect is released under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).


## Citation
```
@inproceedings{sakamoto-etal-2025-development,
    title = "Development of Numerical Error Detection Tasks to Analyze the Numerical Capabilities of Language Models",
    author = "Sakamoto, Taku  and
      Sugawara, Saku  and
      Aizawa, Akiko",
    editor = "Rambow, Owen  and
      Wanner, Leo  and
      Apidianaki, Marianna  and
      Al-Khalifa, Hend  and
      Eugenio, Barbara Di  and
      Schockaert, Steven",
    booktitle = "Proceedings of the 31st International Conference on Computational Linguistics",
    month = jan,
    year = "2025",
    address = "Abu Dhabi, UAE",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.coling-main.666/",
    pages = "9957--9976",
    abstract = "Numbers are used to describe quantities in various scenarios in daily life; therefore, numerical errors can significantly affect the meaning of the entire sentence, and even a single-letter error can be fatal. Detecting numerical errors often requires a high level of commonsense and is difficult even with the recent large language models (LLMs). In this study, we create a benchmark dataset of numerical error detection that uses automatically generated numerical errors. In our analysis, we classify the numerical errors based on the properties of the errors and investigate the ability of the model from several perspectives, including the error class, error size, and passage domain. The experimental results indicate that GPT-3.5, GPT-4, and Llama-3-Instruct (8B) perform well in the numerical error detection task; however, they are not as accurate as humans. We find that the LLMs misidentified correct numbers as errors more frequently than the humans did. In particular, the analysis demonstrates that the current LLMs still need improvement for detecting numerical errors requiring calculations or extensive prior knowledge."
}
```
