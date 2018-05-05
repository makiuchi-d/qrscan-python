#!/usr/bin/env python
import sys
import qrtools

def qrscan(filename):
    qr = qrtools.QR()
    if qr.decode(filename):
        return qr.data
    return None

def print_help():
    print "usage: python qrscan.py <image_file>"

def main():
    if len(sys.argv) < 2:
        print_help()
        return 0

    r = qrscan(sys.argv[1])
    if r == None:
        return 1

    print r
    return 0

if __name__ == '__main__':
    sys.exit(main())
