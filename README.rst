===========================
Loan Calculator Project
===========================

This document provides instructions for setting up the Python environment on a Linux system using Anaconda and Conda, and it outlines the steps for running a Python-based loan calculator that computes monthly payments and differentiated payments.

Environment Setup
-----------------

1. **Creating a New Conda Environment:**

   To create a new isolated environment for the project:

   .. code-block:: bash

      conda create --name loancalculator python=3.12

   This command creates a new environment named ``loancalculator`` with Python 3.12.

2. **Activating the Environment:**

   Activate the created environment with the following command:

   .. code-block:: bash

      conda activate loancalculator

   This ensures that any Python operations or package installations are confined to this environment.

3. **Installing Necessary Packages:**

   Install necessary packages required for running the loan calculator:

   .. code-block:: bash

      conda install argparse math

Project Execution
-----------------

The core of this project involves calculating loan payments based on the user-provided loan parameters. The loan calculator script, `loan_calculator.py`, supports both annuity and differentiated payment calculations.

1. **Running the Loan Calculator:**

   Navigate to the directory containing `loan_calculator.py` and run the script with the necessary arguments. For example, to calculate the annuity payment for a loan with a principal of 1,000,000 over 60 months at an interest rate of 10%:

   .. code-block:: bash

      python loan_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

   To calculate differentiated payments for a loan with a principal of 500,000 over 8 months at an interest rate of 7.8%:

   .. code-block:: bash

      python loan_calculator.py --type=diff --principal=500000 --periods=8 --interest=7.8

2. **Arguments:**

   - `--type`: The type of calculation (`annuity` or `diff`).
   - `--principal`: The loan principal amount (must be a positive number).
   - `--periods`: The total number of repayment periods (must be a positive number).
   - `--interest`: The annual interest rate without the percentage sign (must be a positive number).
   - `--payment`: The monthly payment amount (must be a positive number, used only for annuity calculations).

Example Usages
--------------

1. **Calculate Annuity Payment:**

   .. code-block:: bash

      python loan_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

   Output:
   Your monthly payment = 21248!
   Overpayment = 274880

2. **Calculate Differentiated Payments:**

   .. code-block:: bash

      python loan_calculator.py --type=diff --principal=500000 --periods=8 --interest=7.8

   Output:
   Month 1: payment is 65750
   Month 2: payment is 65344
   ...
   Overpayment = 14628

Contributing
------------

Contributions to this project are welcome. Please ensure to maintain the environment specifications and follow the coding standards used in this project.

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file for details.
