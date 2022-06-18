# Scanner

The scanner is a simple module - it's the one that reads source code
files, and outputs what's known as "Segments".

Let's look at an example. Consider a file with the following content:
```
@start md
asd
@\end
```

``` python
segments = list(scan(text))

```


