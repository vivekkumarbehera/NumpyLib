import zlib #Zlip is a library for the compressiom and decompression of data.
str=b"hello world,my name is vicky"
compressed=zlib.compress(str)
decompressed=zlib.decompress(compressed)
print("Original string:",str)
print("Compressed string:",compressed)
print("Decompressed string:",decompressed)

import gzip #gzip is a library for the compression and decompression of files and data using the gzip format.
with gzip.open('compressed_file.gz', 'wt') as f:
    f.write("hello world,my name is vicky0")
    f.close()
    
with gzip.open('compressed_file.gz', 'rt') as f:
    print(f.read())
    f.close()
    #comparssion between zlib and gzip 
    #zlib is a general-purpose compression library that provides a simple interface for compressing and decompressing data in memory. It is often used for compressing data in applications where speed is important, such as in network communication or file storage. gzip, on the other hand, is a file format and a software application used for file compression and decompression. It uses the DEFLATE algorithm, which is based on zlib, to compress files. gzip is commonly used for compressing files on disk and is widely supported across different platforms and applications.
    #In summary, zlib is a library for in-memory compression and decompression, while gzip is a file format and application for compressing and decompressing files using the DEFLATE algorithm.

import zipfile
with zipfile.ZipFile('compressed_file.zip', 'w') as zipf:
    zipf.write('compressed_file.gz')
with zipfile.ZipFile('compressed_file.zip', 'r') as zipf:
    print(zipf.namelist())
#new ZipFile Create add a file to it
with zipfile.ZipFile('compresse_file.zip', 'a') as zipf:
    zipf.write('compressed_file.gz')
with zipfile.ZipFile('compresse_file.zip', 'r') as zipf:
    print(zipf.namelist())  
