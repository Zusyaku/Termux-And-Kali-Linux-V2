#!/usr/bin/env python

"""
$Id: $

Copyright (c) 2012-2013 Jan Seidl <jseidl@wroot.org> (http://wroot.org/)

LICENSE:
This software is distributed under the GNU General Public License version 3 (GPLv3)

LEGAL NOTICE:
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY 
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT. 
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.
"""

import getopt, sys
import string

####
# Program info
####
USERNAMER_VERSION="1.0-rc3"
BUILD_DATE="2018-11-11"
AVAILABLE_PLUGINS=[ 'normal', 'two_terms', 'one_term', 'normal_abbreviated', 'dotted_two_terms', 'starts_with', 'under_score']
AVAILABLE_FILTERS=[ 'sort', 'unique' ]

####
# Program Functions
####

def parse_file(filePath, plugins = [], filters = []):

    try:
        with open(filePath, 'r') as fileObject:
            for line in fileObject:
                parse_name(line, plugins, filters)
    except IOError:
        e = "Could not open the file: " + filePath
        error(e)

def parse_name(name, plugins = [], filters = []):

    name = name.strip() # Trim whitespaces
    nameTokens = name.split(' ') # Tokenize name and each surname
    numTokens = len(nameTokens)

    if numTokens < 2:
        error('Name and at least one Surname must be supplied')

    # Split First Name and Surnames
    firstName = nameTokens[0]
    nameTokens.pop(0)
    surnames = nameTokens

    results = []

    # Run Plugins
    run_plugins(firstName, surnames, results, plugins)

    # Run Filters
    run_filters(results, filters)
    
    for result in results:
        print result

def run_plugins(firstName, surnames, resultList, plugins = []):

    defaultPlugins = AVAILABLE_PLUGINS

    if len(plugins) == 0:
        plugins = defaultPlugins

    for pluginName in plugins:

        internalPluginName = "plugin_"+pluginName

        # Validate if plugin exists
        if not internalPluginName in globals():
            error("Invalid plugin: "+pluginName)

        pluginObject = globals()[internalPluginName]
        pluginObject(firstName, surnames, resultList)


def run_filters(resultList, filters = []):

    defaultFilters = AVAILABLE_FILTERS

    if len(filters) == 0:
        filters = defaultFilters

    for filterName in filters:

        internalFilterName = "filter_"+filterName

        # Validate if filter exists
        if not internalFilterName in globals():
            error("Invalid plugin: "+filterName)

        filterObject = globals()[internalFilterName]
        filterObject(resultList)

####
# Result Filters
####

# Unique Filter
#
# Removes duplicated entries

def filter_unique(resultList):

    uniqueResults = set(resultList)
    del resultList[:]
    for result in uniqueResults:
        resultList.append(result)

# Sort Filter
#
# Filter entries alphabetically
def filter_sort(resultList):

    resultList.sort()

# Lowercase Filter
#
# Transforms entries to lowercase

def filter_lowercase(resultList):

    for key, result in enumerate(resultList):
        resultList[key] = result.lower()

####
# Parsing Plugins
####

# Normal Plugin
#
# Generates usernames based on concatenation
# of first name with surnames in permutation
#
# Ex: JohnPaulJones, JohnJonesPaul
def plugin_normal(firstName, surnames, resultList):

    surnamePermutations = permutate_all(surnames)

    for permutations in surnamePermutations:
        resultList.append(firstName+string.join(permutations, ''))
        resultList.append(string.join(permutations, '')+firstName)
        
# Two Terms Plugin
#
# Generates usernames based on concatenation
# of first name with surnames in permutation
#
# Ex: JohnPaul, JohnJones, PaulJones
def plugin_two_terms(firstName, surnames, resultList):

    # Try each surname with 
    # first name and reversed
    for surname in surnames:
            resultList.append(firstName+surname)
            resultList.append(surname+firstName)

    # If more than one surname,
    # combine'em too
    if len(surnames) > 1:
        tokens = list(surnames)
        for surname in surnames:
            firstToken = tokens.pop(0)
            for token in tokens:
                resultList.append(firstToken+token)

# One Term Plugin
#
# Generates usernames based on permutation
# of first name and surnames generating one-word
# usernames
#
# Ex: John, Paul, Jones
def plugin_one_term(firstName, surnames, resultList):

    tokens = [ firstName ]
    tokens += surnames
    for name in tokens:
        resultList.append(name)

# Dotted Two Terms Plugin
#
# Generates usernames based on concatenation
# of first name with surnames in permutation
# with a dot in the middle
#
# Ex: John.Paul, John.Jones, Paul.Jones
def plugin_dotted_two_terms(firstName, surnames, resultList):

    # Try each surname with 
    # first name and reversed
    for surname in surnames:
            resultList.append(firstName+'.'+surname)
            resultList.append(surname+'.'+firstName)


# Normal Abbreviated Plugin
#
# Generates usernames based on concatenation
# of first name with surnames in permutation
# in abbreviated forms
#
# Ex: JohnPJones, JohnPaulJ, JohnJonesP JohnJPaul
def plugin_normal_abbreviated(firstName, surnames, resultList):

    permutatedSurnames = permutate_all(surnames)
    firstNameArr = [ firstName ] 

    # All Terms
    for entry in permutatedSurnames:

        nameFirst = list(firstNameArr+entry)
        nameLast = list(entry+firstNameArr)

        for name in abbreviate(nameFirst):
            resultList.append(name)

        for name in abbreviate(nameLast):
            resultList.append(name)

    # Two Words
    for surname in surnames:
        for name in abbreviate([ firstName, surname ]):
            resultList.append(name)
        for name in abbreviate([ surname, firstName]):
            resultList.append(name)

# Starts With Plugin
# contributed by Derek Callaway [decal (AT) sdf {D0T} org] https://decal.github.io
#
# X Letters First Name Starts With and/or
# Y Letters Last Name Starts With
#
# Generates usernames based on concatenation of
# first X letters in first name and/or
# first Y letters in last name
# 
# Such naming schemes are often found on legacy
# systems like AS/400 mainframes, DEC VMS/VAX, etc.
#
# Ex. dc dca dcal dcall dec deca decal decall derc derca dercal dercall 
def plugin_starts_with(firstName, surnames, resultList):
  for x in range(0, 1 + len(firstName) / 2):  
    for surname in surnames:
      resultList.append(firstName[0:x] + surname)
      for y in range(0, 1 + len(surname) / 2):
        resultList.append(firstName[0:x] + surname[0:y])
        resultList.append(firstName + surname[0:y])

def plugin_under_score(firstName, surnames, resultList):
  for x in range(0, 1 + len(firstName)):
    for surname in surnames:
      resultList.append(firstName[0:x] + "_" + surname)
      resultList.append(surname + "_" + firstName[0:x])
      for y in range(0, 1 + len(surname)):
        resultList.append(firstName[0:x] + "_" + surname[0:y])
        resultList.append(surname[0:y] + "_" + firstName[0:x])
        resultList.append(firstName + "_" + surname[0:y])
        resultList.append(surname[0:y] + "_" + firstName)
  
####
# Util functions
####
def permutate_all(tokens):
    if len(tokens) <=1:
        yield tokens
    else:
        for perm in permutate_all(tokens[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + tokens[0:1] + perm[i:]

def abbreviate(tokens):

    resultList = []

    tokenCount = len(tokens)
        
    # One abbreviated word
    for i in range(tokenCount):
        output = ''
        position = 0
        for j in tokens:
            if i == position:
                output += j[0]
            else:
                output += j
            position += 1;
        
        resultList.append(output)

    # Two abbreviated words
    for i in range(tokenCount):
        output = ''
        position = 0
        for j in tokens:
            if i == position or i == position+1:
                output += j[0]
            else:
                output += j
            position += 1;
        
        resultList.append(output)

    # All-but-one abbreviated words
    if tokenCount > 3:
        for i in range(tokenCount):
            output = ''
            position = 0
            for j in tokens:
                if i == position: 
                    output += j
                else:
                    output += j[0]
                position += 1;
        
        resultList.append(output)

    return resultList


####
# Main
####

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlp:f:n:", ["help", "lowercase", "plugins", "file=","name="])

        inputFile = None
        inputName = None

        defaultPlugins = AVAILABLE_PLUGINS
        defaultFilters = AVAILABLE_FILTERS

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-f", "--file"):
                inputFile = a
            elif o in ("-p", "--plugins"):

                pluginList = str(a).split(',')
                validPlugins = []

                for plugin in pluginList:
                    try:
                        pluginIndex = AVAILABLE_PLUGINS.index(plugin) # check plugin existance
                        validPlugins.append(plugin)
                    except ValueError:
                        error('Invalid plugin: "'+plugin+'"')

                defaultPlugins = validPlugins

            elif o in ("-n", "--name"):
                inputName = a
            elif o in ("-l", "--lowercase"):
                defaultFilters.append('lowercase')
            else:
                error("option '"+o+"' doesn't exists")

        if inputFile == None and inputName == None:
            error('Please specify an input file or name')

        if inputFile != None and inputName != None:
            error('Please specify only an input file or name, not both')

        # If name was supplied, 
        # process single entry and exit
        if inputName:
            parse_name(inputName, plugins = defaultPlugins, filters = defaultFilters)
            sys.exit(0)

        # If file was supplied,
        # process each line
        if inputFile:
            parse_file(inputFile, plugins = defaultPlugins, filters = defaultFilters)
            sys.exit(0)

    except getopt.GetoptError, err:
        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

def usage():

    print
    print "usage: " + sys.argv[0] + " [ -f <file> ] [ -n <full name> ] [ -l ]";
    print 
    print "flags:"
    print "\t-n\tsupplies a single name"
    print "\t-f\tsupplies name entries from text file"
    print "\t-l\tconverts result to lowercase"
    print "\t-p\tmanually specify plugins (comma-separated) [default: all]"
    print "\t\t"+str(AVAILABLE_PLUGINS)
    print ""

def error(errorMsg, fatal=True, showUsage=True):
    
    sys.stderr.write(errorMsg+"\n")
    if showUsage:
        usage()
    if fatal:
        sys.exit(2)
    
if __name__ == "__main__":
    main()

