<p align="center">
  <img src="https://github.com/serhatdog/colorhide/blob/main/colorhide_logo.png?raw=true" alt="ColorHide">
</p>

<p align="center"><b>Author: Serhat Dogan</b><p>
<p align="center"><b>Last update: 15.08.2022</b><p>
<p align="center"><b>Preparing...</b><p>
  
<h1 align="center">How The Function Works?</h1>

First of all, numbers are taken over keymap for your writing. Then it is converted to color codes (numpy array) with a simple encryption method for your texts. Then the picture is filled with all other color codes, except for your color code. At the end, your color codes are written line by line according to the keymap number.

For the reading process, your image is first converted to numpy array. Then the password you sent in the parameter is decoded and translated into color codes. If the color codes match, the string is returned back so that you can read the text.

<h1 align="center">Why We Have To Use Numba?</h1>

Numba translates Python functions to optimized machine code at runtime using the industry-standard LLVM compiler library. Numba-compiled numerical algorithms in Python can approach the speeds of C or FORTRAN.

You don't need to replace the Python interpreter, run a separate compilation step, or even have a C/C++ compiler installed. Just apply one of the Numba decorators to your Python function, and Numba does the rest.
