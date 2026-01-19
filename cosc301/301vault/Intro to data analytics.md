### Data representation

**What is data?** - data is information before it's been given any context, structure, and meaning

Raw data is produced by how users interact with computers as well as from systems and sensors

![[Pasted image 20260108111040.png]]
Answer is B

**What is Big Data?** - general term to describe the 'explosion' of data collected and the opportunities to transform this data into useful insights to benefit society

'Big' because there is so much that it challenges how the data is processed

five V's
- Volume
- Velocity
- Variety
- Value
- Veracity

Your phone is spying on you and the government targets individual people to affect the populous

Anyways,

Computers represent data digitally or discretely, while real world data is analog or continuous.

aside: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
- #### The Core Principle
To perfectly reconstruct a continuous (analog) signal from discrete samples, you must sample at **at least twice the highest frequency component** present in the signal:

---

## Integers

An integer is encoded in a computer using a fixed num of bits (32,64,other)

[Twos complement](https://en.wikipedia.org/wiki/Two%27s_complement)

### Doubles / Floats

A decimal num may either be stored as a double (8 bytes) or a float (4 bytes). Values are stored using a standard IEEE 754 format.

Mantissa m, exponent e, 2 - radix 

Scientific representation of N = m * 2^e

Not perfectly precise. 
[floating point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)

### Characters

A common encoding is **ASCII** (american standard code for information interchange), which uses 8 bits to represent characters.

![[Pasted image 20260108114029.png]]

**Unicode Standard** uses a pattern of 16-bits to represent the major symbols used in all languages.
first 256 characters are the same as ascii, max num of symbols is 65,536


### String
A string is a sequence of characters.
A string has a terminator to know when it ends:
• Null-terminated string - last byte value is 0 to indicate end of string.
• Byte-length string - length of string in bytes is specified (usually in the first few bytes before string starts).

### Date & Time
Integer representation - Julian Date, Time since epoch.
String representation - YYYYMMDD, YYYYDDD, HHMMSSFF

### Other
Encoding other data. The documents, music, and videos that we commonly use are much
more complex. However, the principle is exactly the same. We use
sequences of bits and interpret them based on the context to
represent information.

### Metadata
Data about data, names of files, column names in a spreadsheet, table and column names and types in a db

### Files
A file is a sequence of bytes. the Operating system manages how to store and retrieve the file bytes from the device. Program must know how to interpret bytes based on its information (metadata).

### File Encoding
Determined by the file extension  which allows the os to know how to process the file
##### Text 
csv, json, xml
data analytics will often involve processing text files
[wiki](https://en.wikipedia.org/wiki/Character_encoding)
##### Binary
Smaller, faster, not human readable

## Time vs Space tradeoff
Some application cases require you to encode efficiently both time wise and space wise

At all granularities (sizes) of data representation, we want to use as
little space (memory) as possible. However, saving space often makes
it harder to figure out what the data means (think of compression or
abbreviations). In computer terms, the data takes longer to process.

The time versus space tradeoff implies that we can often get a faster
execution time if we use more memory (space). Thus, we often must
strive for a balance between time and space.

