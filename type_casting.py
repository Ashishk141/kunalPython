Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = '1'
>>> type(a)
<class 'str'>
>>> b = int(a)
>>> b
1
>>> type(b)
<class 'int'>
>>> b = 'ashadf'
>>> type(b)
<class 'str'>
>>> c = int(b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c = int(b)
ValueError: invalid literal for int() with base 10: 'ashadf'
>>> c = 1.25
>>> c
1.25
>>> type(c)
<class 'float'>
>>> d = int(c)
>>> d
1
>>> type(d)
<class 'int'>
>>> c
1.25
>>> type(c)
<class 'float'>
