#!/usr/bin/env python3
import sys

class NotFASTAError(Exception):
    pass

class InvalidSequenceError(Exception):
    pass

file = ''

try:

    file = sys.argv[1]

    print("User provided file name:", file)

    if not file.lower().endswith(('.fasta', '.fa', '.nt')):
        raise NotFASTAError("Not a FASTA file")

    FASTA = open(file, "r")

    sequence = ''

    for line in FASTA:

        print(line)

        if not line.startswith('>'):
            sequence += line.strip().upper()

    FASTA.close()

    if not any(char in sequence for char in 'ARGCN'):
        raise InvalidSequenceError("No valid character found")

except IndexError:

    print("Please provide a file name")

except NotFASTAError:

    print("File needs to end with .fasta, .fa or .nt")

except InvalidSequenceError:

    print("No ARGCN characters found in the sequence")

except IOError as ex:

    print("Can't find file:", file, ':', ex.strerror)
