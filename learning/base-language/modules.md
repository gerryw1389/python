
If you get the error `module $module has no $method attribute`, for example: `module csv has no reader attribute` when [it clearly does](https://docs.python.org/3/library/csv.html) then this is because I named my file `csv.py`. Once renamed to `monitorcsv.py`, everything worked. Had the same thing happen with `email.py`.
