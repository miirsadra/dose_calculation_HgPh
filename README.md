# Liquid Dosage Form Dose Calculation

Author: Mirsadra Molaei  

Date created: 2023-05-18  

Python version: 3.10.11  

Description: Dose calculation of liquid dosage forms based on the Hungarian Pharmacopoeia (Hg. Ph.). 

## Overview

This Python code calculates the dose of liquid dosage forms based on the Hungarian Pharmacopoeia (Hg. Ph.). 
It takes into account the amount of active agent, solvent, spoon size, and density of the active agent to calculate the ordered quantity in one spoon and one day. It also checks if the calculated dose exceeds the maximum single dose and maximum daily dose defined by Hg. Ph.

## Prerequisites

- Python 3.10.11: Make sure you have Python 3.10.11 installed on your machine. You can download Python from the official Python website (https://www.python.org/downloads/) and follow the installation instructions specific to your operating system.

## Usage

1. Clone the repository or download the `dose_calculation.py` file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `dose_calculation.py` file is located.

3. Run the following command to execute the script: `python dose_calculation.py`

4. Follow the prompts and enter the required information:
* **Amount of active agent weighted in grams**: Enter the amount of the active agent used in grams. This value should be a positive number.
* **Amount of solvent weighted in grams**: Enter the amount of the solvent used in grams. This value should be a positive number.
* **Spoon size**: Enter the spoon size as follows:
    1 for table spoon (15 grams)
    2 for child spoon (10 grams)
    3 for tea spoon (5 grams)
* **Density of the active agent**: Enter the density of the active agent as follows:
    1 for aqueous (density: 1)
    2 for syrup (density: 1.3)
* **Maximum single dose (mg)**: Enter the maximum single dose defined by Hg. Ph. in milligrams. This value should be a positive integer.
* **Maximum daily dose (mg)**: Enter the maximum daily dose defined by Hg. Ph. in milligrams. This value should be a positive integer.
* **Number of times the medicine needs to be taken per day**: Enter the number of times the medicine needs to be taken per day. This value should be a positive integer.

5. The script will calculate and display the ordered quantity in one spoon and one day based on the provided inputs. It will also check if the calculated dose exceeds the maximum single dose and maximum daily dose defined by Hg. Ph.

# Contributing

Contributions to this repository are welcome. If you want to add other calculations for different dosage forms or improve the existing code, you can fork this repository, make your changes in a new branch, and submit a pull request.

Please ensure that any changes or additions follow the relevant guidelines and coding standards.
