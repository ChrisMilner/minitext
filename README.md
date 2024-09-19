# MiniText.mtxt

MiniText sits at the unique intersection of a file encoding (which is entirely unsupported by any text editor), and compression algorithm (which isn't very good).

## Structure
A `mtxt` consists of two parts seperated by `0xff` byte:
* The **header** defines the list of characters used within the file
* The **content** encodes the text using the index of the character in the dictionary. Since we know how many characters the file uses, each character is represented using the minimum number of bits required.

The text `aaaa` will be encoded as `a|0xff|0xf0` (a space saving of one byte):
* Since there's only one character it can be represented in a single bit
* The first 4 bits in the content are set to 1s to represent the a's, the rest are 0 and should be ignored

## FAQ

> Does it work with Unicode?
I don't know, but probably not
