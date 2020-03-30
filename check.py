import lzma

f= lzma.open("cli_file_recv.xz","rb")
bindata = f.read()

print(bindata)


# f= lzma.open("ser_file_sent.xz","rb")
# bindata = f.read()

# print(bindata)