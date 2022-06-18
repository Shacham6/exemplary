# @start md
# # Scanner
#
# The scanner is a simple module - it's the one that reads source code
# files, and outputs what's known as "Segments".
# @end


from exemplary.scanner import scan
from exemplary.segment import Segment


def simple_scan_example():
    # @start md
    # Let's look at an example. Consider a file with the following content:
    #
    # ```
    # # @@start md
    # # Content
    # # @@end
    # ```
    #
    # Those `@@start` and `@@end` annotate the start & end of **blocks**. The **md** that comes after
    # the `@@start` specify the processor that will handle the **block**. In this case it'll be the
    # raw `markdown` processor.
    #
    # Using the scanner on the aforementioned file will result in **Segments** being formed.
    # See here:
    # @end

    text = "# @start md\n# Content\n# @end"

    # @start py

    from exemplary.scanner import scan

    segments = list(scan(text))

    # @end

    # @start md
    # !!!note
    #
    #       Calling `list(...)` here since the `scan` method returns a generator.
    # @end

    # @start md
    # This specific text will yield only a single segment, which will be
    # the following:
    # @end

    assert len(segments) == 1
    assert segments == [
        # @start py
        Segment(
            processor="md",
            args={},
            document="# Content",
            comment_pat="#",
        )
        # @end
    ]


def automatic_comments_syntax():
    # @start md
    # ## Agnostic Comments Support
    #
    # Although in the previous example the annotations where inside a Python-like comment (`#`),
    # all comment-styles are natively supported.
    #
    # For example, here's a document with C-style comment:
    #
    # ``` text
    # // @@start md
    # // Content
    # // @@end
    # ```
    # @end
    text = "// @start md\n// Content\n// @end"

    # @start md
    # Scanning it will yield the same segment as in the previous example,
    # only with a different `comment_pat` field:
    # @end

    # @start py
    segments = list(scan(text))
    assert segments == [
        Segment(
            processor="md",
            args={},
            document="Content",
            comment_pat="//",
        )
    ]
    # @end
