## Code Organisation 

-  main.py: The main entry point of the program. It reads the input from the input.txt file and prints the output to the console.
-  package_sorter.py: The package sorter class that contains the logic for sorting the packages.
-  test.py: The test file that contains the test cases for the package sorter class.
-  input.txt: The input file that contains the input for the program.
-  requirements.txt: The requirements file that contains the required packages for the program.
-  README.md: The README file that contains the instructions for the program.

## How to run the program

- Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

-  Run the program by running the following command:

```bash
python main.py
```

-  Run the tests by running the following command:

```bash
python -m pytest src/test.py
```

- Change inputs in input.txt to test different cases

- Testing from UI

```bash
streamlit run src/ui.py
```

