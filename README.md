[![Supported Python Versions](https://img.shields.io/pypi/pyversions/python-examplary/0.0.1)](https://pypi.org/project/python-examplary/) [![PyPI version](https://badge.fury.io/py/python-exemplary.svg)](https://badge.fury.io/py/python-exemplary)
![Logo](https://github.com/shacham6/exemplary/raw/master/assets/Logo/For%20Web/svg/Color%20logo%20-%20no%20background.svg)

# Exemplary

A tool which provides extremely simple way to generate markdown documentation
from actual source code examples!

## Requirements

The requirements for using this package are:

- Python (>= 3.8).

## Installation Guide

Install the package as you would any other, using `pip`:

``` sh
> pip install python-exemplary
# or use `pipx` for virtual-env isolation
> pipx install python-exemplary
```

Check if it worked by running:

``` sh
> exemplary --help
```

## Usage Guide

Using `exemplary` is really easy. Upon installing the package, now a program called `exemplary` should be
available to run.

`exemplary` works by reading your source-code; finding what must be _comments_; and wrapping the documents by
the specified __processors__.

But why use words when examples do the trick?

Take for example the following Python script:

``` python
# myscript.py
def main():
    # @start md
    # # Exemplary Example!
    #
    # First when you want to add 1 to a number, you gotta start with a number.
    # Let's create a number-containing variable called "num"
    # @end

    # @start py
    num = 1
    # @end

    # @start md
    # And now let's just "+ 1" it, saving the result to "result".
    # @end

    # @start fence {"lang": "python"}
    result = num + 1
    # @end

    # @start md
    # Fantastic! Now let's print the result to see how we did
    # @end

    # @start py
    print(result)
    # @end


if __name__ == "__main__":
    main()
```

Let's break it down:

- `@start` - Those signify the start of a block to be processed. The `md`/`py` signify which processor will handle the text-segment.  There are currently 3 processors:
  - `md`/`markdown` - Strips the comment pattern (in this case `#`) and simply insert the block content as is.
  - `fence` - A classic markdown fence. The language is determined in the following arguments.
  - `py`/`python` - A shortcut for Python fence-blocks.
- `@end` signify the end of a block.
- ..And everything else in the middle, **is** the aforementioned blocks.

By running the command:

``` sh
> exemplary generate myscript.py
```

The output of the generated Markdown will be printed on screen:

    # Exemplary Example!

    First when you want to add 1 to a number, you gotta start with a number.
    Let's create a number-containing variable called "num"

    ``` python
    num = 1

    ```

    And now let's just "+ 1" it, saving the result to "result".

    ``` python
    result = num + 1

    ```

    Fantastic! Now let's print the result to see how we did

    ``` python
    print(result)

    ```

...And that's it. Nothing else to it. Have fun documenting!
