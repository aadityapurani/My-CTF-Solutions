# Check out this cool Filter (200 Points)

Category: Misc

_Writeup_:

An image was provided with quite evidently an filter applied. We investigate the image and find a repeated pattern in Blue channel (R,G,B) with a whole byte of size 0x33.

We recover this 
```
_Va`RP\x88aVYlW]RTlP\\Z]_R``V\\[lZR``R`ldVaUl_TOlcNYbR`\x8a
```

After thinking a bit, it was evident that the individual ASCII should be converted to decimal and substracted by 13 and again convert back to ASCII. The reason for that was we already know the pre-fix `RITSEC{` so I made analysis & concluded that

Solver script: solve_filter.py

##### Flag: RITSEC{TIL_JPEG_COMPRESSION_MESSES_WITH_RGB_VALUES}
