# uniscribe

This Docker image is a thin wrapper around <https://github.com/janlelis/uniscribe>.
It gives you a way to break down Unicode strings.
For example:

```console
$ uniscribe "Hello world"

   0048 ├─ H		├─ LATIN CAPITAL LETTER H
   0065 ├─ e		├─ LATIN SMALL LETTER E
   006C ├─ l		├─ LATIN SMALL LETTER L
   006C ├─ l		├─ LATIN SMALL LETTER L
   006F ├─ o		├─ LATIN SMALL LETTER O
   0020 ├─ ] [  ├─ SPACE
   0077 ├─ w		├─ LATIN SMALL LETTER W
   006F ├─ o		├─ LATIN SMALL LETTER O
   0072 ├─ r		├─ LATIN SMALL LETTER R
   006C ├─ l		├─ LATIN SMALL LETTER L
   0064 ├─ d		├─ LATIN SMALL LETTER D

```

h/t [@glasnt](https://twitter.com/glasnt/status/878119485697269760) for telling me about this utility.