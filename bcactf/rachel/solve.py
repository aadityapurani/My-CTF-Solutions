# Found from OCR automation using image-magick and tesseract
flag = 820921601166721424573282546345206805820898697321521913920196691573868657577500743744203737234698
print(int_to_hex(flag))

def int_to_hex(inp):
    hexed = hex(inp)
    return bytearray.fromhex(hexed[2:]).decode()
    
#bcactf{0p71c4lly_r3c0gn1z3d_ch4r4c73rs}
