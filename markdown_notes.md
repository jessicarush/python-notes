# Markdown Notes

## Table of contents
- [links](#links)
- [headings](#headings)
- [code](#code)
- [blockquotes](#blockquotes)
- [line breaks](#line-breaks)
- [lists](#lists)
- [emphasis, strong, strikethrough](#emphasis,-strong,-strikethrough)
- [images](#images)
- [horizontal rules](#horizontal-rules)
- [backslash escapes](#backslash-escapes)

## links

This in an [example link](https://daringfireball.net/projects/markdown/syntax).

You can add the links title attribute like this:
[example link](https://github.com/ "Title goes here")

You can use link references as well:
Here's [Google][1], [Yahoo][2], [MSN][3]

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"

You can also create automatic links out of a url:
<https://github.com/>

You can link to any heading within your document using like this: (#lower-case-heading-replaces-spaces-with-dashes)



# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6


## code
```
pip3 install mylibrary
```
Here is some `inline code`.

You cal also specify syntax highlighting:

```python
print('Syntax highlighting')
```


## blockquotes

> This is a blockquote
> You can precede each line with > if you're using hard returns.  
> Or if you're soft wrapping you can just add > to the first line.


## line breaks

Two spaces at the end of a line ensure a new line.  
Here's my new line.


## lists

Unordered lists can be marked with -, +, or *

* list
* list
* list

Ordered lists can be marked with any number.

1. list
1. list
1. list

Task lists:
- [x] This is a complete item
- [ ] This is an incomplete item
- [ ] This is an incomplete item


## emphasis, strong, strikethrough

Surround text with single \* or \_ for
*emphasized text*

Surround text with double \*\* or \_\_ for
**strong text**

Surround text with triple \*\*\* for
***strong emphasized text***

Surround text with double \~\~ for
~~strikethrough text~~


## images

![Alt text](/data/cat.png)

![Alt text](/data/cat.png "Optional title")

You can also place images using the reference method as with links above.


## horizontal rules

Insert a horizontal rule by typing 3 * or - or _ on their own line:

***
___
---


## backslash escapes

Markdown provides backslash escapes for the following characters:

```
\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark
```
