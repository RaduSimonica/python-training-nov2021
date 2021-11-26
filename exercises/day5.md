### Files exercises

1. Write a Python program that reads file content and displays the number of lines that were read.
1. Write a Python program to append text into a file and display the new content.
1. Write a function `grep` that receives `text` and `file` as parameters and returns a list with all the lines in the file containing `text`. 
1. Write another function `grepinto` that receives `text`, `infile` and `outfile` as parameters and writes to `outfile` the lines in `infile` that contain `text`. Open both files within one `with` statement. 

[!] `file`, `infile` and `outfile` are all file names - not file handlers.

### File system exercises

1. Write a Python program that creates a directory `outdir` at the current location and a directory `innerdir` inside `outdir`.
   Create an empty file inside `innerdir`. Use `os.walk()` to print the directory tree for `outdir`.
   Remove the directories and the file.
1. Write a generator function that yields all the file names with an extension from a directory.
   Give the path and the file extension as parameters. 

### Unittest exercises

1. Write a test case for `Employee.raise_salary()` method. Consider all representative cases.

