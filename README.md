# UniqueInt Project

## Overview
The `UniqueInt` project provides a utility for processing text files containing integer numbers. This utility reads the integers from an input file, removes duplicates, sorts them, and writes the sorted unique integers to an output file.

## Features
- **Leading and Trailing Whitespace Removal**: The utility can trim leading and trailing spaces, tabs, and newlines from strings.
- **String to Integer Conversion**: Converts string representations of integers to actual integer values, handling invalid inputs gracefully.
- **Integer to String Conversion**: Converts integer values back to their string representations.
- **Custom List Append**: Provides a custom method to append items to a list.
- **String Reversal**: Reverses a given string.
- **Custom Sorting**: Implements a custom quicksort algorithm to sort the integers.
- **File Processing**: Reads integers from a file, removes duplicates, sorts them, and writes the result to an output file.

## Usage

### Installation
No special installation is required for this project. Simply clone the repository and run the Python script.

### Running the Script
To use the `UniqueInt` utility, execute the script from the command line:

```sh
python UniqueInt.py
```

You will be prompted to enter the paths for the input and output files.

### Example
1. **Input File**: `input.txt`
    ```
    34
    12
    78
    12
    45
    34
    -23
    78
    ```
2. **Output File**: `output.txt`
    ```
    -23
    12
    34
    45
    78
    ```

### Methods

#### ltrim(s)
Removes leading spaces and tabs from the string `s`.

#### rtrim(s)
Removes trailing spaces, newlines, and tabs from the string `s`.

#### trim(s)
Removes both leading and trailing spaces, newlines, and tabs from the string `s`.

#### reverse_string(s)
Reverses the given string `s`.

#### str_to_int(s)
Converts the string `s` to an integer. Returns `False` if the string is not a valid integer or exceeds 1023.

#### int_to_str(i)
Converts the integer `i` to a string.

#### custom_append(lst, item)
Appends `item` to the list `lst` and returns the list.

#### custom_sort(array)
Sorts the list `array` using a custom quicksort implementation.

#### processFile(input_file, output_file)
Reads integers from `input_file`, processes them to remove duplicates, sorts them, and writes the sorted unique integers to `output_file`.

## Notes
- The input file should contain one integer per line.
- The integers must be in the range of -1023 to 1023.
- The script ignores lines that do not represent valid integers or satisfy those conditions above.
