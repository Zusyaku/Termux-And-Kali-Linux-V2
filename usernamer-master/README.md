usernamer
==========================================
usernamer is a penetration testing tool to generate a list of possible usernames/logins for determined name (ex: John Doe Doeson) for user enumeration or bruteforcing. 
This tool also supports text-files with one name per line as input.

Features
-----------------------------------------
usernamer has a plugin structure that enables a series of transformations:

* normal: Permutates given name with all surnames (if more than one) with name starting and ending (johndoedoeson,johndoesondoe,doedoesonjohn etc)
* two_terms: Permutates given name with all surnames (if more than one) with name starting and ending but it will output a two-termed login (johndoe, doejohn, johndoeson etc)
* one_term: Permutates all name tokens (first name and surnames) and generates single terms usernames (john, doe, doeson)
* dotted_two_terms: Permutates given name with all surnames (if more than one) with name starting and ending but it will output a two-termed login dot-separated (john.doe, doe.john, john.doeson etc)
* normal_abbreviated: Generates abbreviated versions of the 'normal' and 'two_terms' plugins (jdoe, johnd, jd etc)
* starts_with: Generates strings with a variable number of letters that the first and/or last names start with (jd, jod, johd, johnd, jdo, jdoe)
* under_score: Functions like starts_with, but inserts an underscore character '_' between the first and last names

Usage
-----------------------------------------

    usage: usernamer.py [ -f <file> ] [ -n <full name> ] [ -l ]
    
    flags:
        -n  supplies a single name
        -f  supplies name entries from text file
        -l  converts result to lowercase
        -p  manually specify plugins (comma-separated) [default: all]
            ['normal', 'two_terms', 'one_term', 'normal_abbreviated', 'dotted_two_terms', 'starts_with', 'under_score']


License
-----------------------------------------
This software is distributed under the GNU General Public License version 3 (GPLv3)

LEGAL NOTICE
-----------------------------------------
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY! IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT. BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.
