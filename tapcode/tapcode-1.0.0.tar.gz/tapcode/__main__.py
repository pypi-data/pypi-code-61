#!/usr/bin/env python
import argparse
from tapcode import tapcode

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="tapcode",description='Encipher or Decipher a tapcode message.')
    parser.add_argument("-s","--sentence",help="Sentence to cypher or decipher")
    parser.add_argument("-f","--file",help="file to cypher or decipher")
    parser.add_argument("-d", "--decode", action="store_true", help="decode tapcode sentence.")
    parser.add_argument("-e", "--encode", action="store_true", help="encode sentences to tapcode.")
    args = parser.parse_args()
    
    
    if args.sentence:
        if args.decode :
            print(tapcode.decipher(args.sentence," ","."))
    
        elif args.encode:
            print(tapcode.encipher(args.sentence," ","."))
        else:
            print("Please provide an option : Decode (-d) or Encode (-e) ?")
    
    elif args.file :
        if args.sentence: 
            print("Cannot process 'sentence option' and 'file option' at the same time. Please choose !")

        f = open(args.file)
        sentences = f.read()
        
        if args.decode :
            dec = tapcode.decipher(sentences," ",".")
            out = open('decoded', 'w')
            out.write(dec)
    
        elif args.encode:
            enc = tapcode.encipher(sentences," ",".")
            out = open('encoded', 'w')
            out.write(enc)
        out.close()
    
    else :
        print("Please provide a sentence to cypher or encipher !")
        exit()