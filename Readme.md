# Deep search

## Introduction

Search through multiple files for a search term

Files supported : ``` all plain text files (.txt, .html, .php, .js) ```
> Note : PDF not supported ( need PDF parser support )

### How to use?

- Save 'search keyword' on ```deep_scan_keyword.ini``` file.
- Run the below command in terminal

``` bash
python app.py
```

- Result will be shown in the terminal as well as ```result.txt``` file

### Warnings

- ```result.txt``` will be replaced by the program for storing search result
- ```deep_scan_keyword.ini``` will be generated if not found
- if ```deep_scan_keyword.ini``` is empty or not found ```keyword``` should be given on command line
