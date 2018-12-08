# Notes.py
# Hakuga
#
#
# This program is just a giant list of print functions to help me coorelate my
# notes. If you got this somehow, I hope you find it useful :)
#
#
#


def contents():
    return print("",
                 "general, loops, strings, lists, readwrite, boolean"
                 "",
                 sep = "\n", end = "\n################ END. ###################\n")

def general():
    return print("",
                 "print(<literally anything>, "", end="", sep="")",
                 'input("whatever you want")',
                 "round(<number>, <how many digits>)",
                 "ord(<string>) - converts letters to ASCII digits",
                 "chr(<string>) - converts digits to ASCII letters",
                 "",
                 sep = "\n", end = "\n################ END. ###################\n")
                 
def loops():
    return print("",
                 "For loops: ",
                 " ",
                 "For <var> in <sequence>():",
                 "    <BODY>",
                 " ",
                 " ",
                 "While Loops: ",
                 " ",
                 "While <condition>:",
                 "    <BODY>",
                 " ",
                 " ",
                 "Sentinel Loops: ",
                 " ",
                 "Get the first data item",
                 "while item is not the sentinel:",
                 "    process the item",
                 "    get the next data item",
                 "",
                 "",
                 sep = "\n", end = "\n################ END. ###################\n")
def strings():
    return print("",
                 "Strings and lists",
                 " ",
                 "+ - concatination",
                 "* - repetition",
                 "<string>[] - Indexing",
                 "<string[:] - Slicing",
                 "len(<var>) - length of the var",
                 "'Hello {0}, {1}, {1:1.3f}'.format('David', 3.4975) - Position 0 is David,",
                 "    position '1' is from '1':to'1', out to 3 decimals."                                        
                 " ",
                 " ",
                 "String methods: ",
                 "s.capitlize() - Copy of s with only the first character capitalized.",
                 "s.center(width) - Copy of s centered in a field of given width.",
                 "s.count(sub) - Count the number of occrences of sub in s.",
                 "s.find(sub) - Find the first position where sub occurs in s.",
                 "s.join(list) - Concatenate list in a string, using s as seperator.",
                 "s.ljust(width) - Like center, but s is left-justified.",
                 "s.lower() - Copy of s in all lowercase characters.",
                 "s.lstrip() - Copy of s with leading white space removed.",
                 "s.replace(oldsub, newsub) - Replace all occurences of oldsub in s with newsub.",
                 "s.rfind(sub) - Like find, but returns the rightmost position.",
                 "s.rjust(width) - Like center, but s is right-justified.",
                 "s.rstrip() - Copy of s with leading / trailing white space removed. ",
                 "    If () is specified,- remove that instead.",
                 "s.split() - Split s into a list of substrings (see text).",
                 "s.title() - Copy of s with first characer of each word capitalized",
                 "s.upper() - Copy of s with all characters converted to uppercase",
                 "",
                 sep = "\n", end = "\n################ END. ###################\n")
                 
                 

def lists():
    return print("",
                 "<somelist> = []",
                 "list.append(element) - Append an element to the end of your list",
                 "somelist[0] - whatever the value of the index of 0 is",
                 "",
                 sep = "\n", end = "\n################ END. ###################\n")

def readwrite():
    return print(
        "",
        '# Opening Files',
        '<variable> = open(<name>, <mode>) # Opens <variable>. Modes "r", "w"',
        ' ',
        '# Reading Files',
        '<variable> = <file>.read() # Returns the entire remaining contents of the file as a single',
        '              # string',
        '<variable> = <file>.readline() # Returns the next line of the file. All text up to + \n',
        '<variable> = <file>.readlines() # Returns a list of the remaining lines in the file,',
        '                   # each list item is a single line including the newline character',
        '                   # at the end',
        "",
        sep = "\n", end = "\n################ END. ###################\n")

def boolean():
    return print(
        "",
        '# boolean logic in Python higharchy',
        'x not y # If x is False, return True. Otherwise, return False.',
        'x and y # if x is False, return x. Otherwise, return y.',
        'x or y # if x is True, return x. Otherwise, return y.',
        ' ',
        '# if, else, elif',
        ' ',
        'if: #if <something>',
        '    <body> #Do this',
        ' ',
        'else: #when if does not satisfy that condition, do else:',
        '    <body> #Do this',
        ' ',
        'elif: #when if, else does not satisfy, elif:',
        '    <body> #Do this',
        ' ',
        '== # Equals exactly',
        '> # Greater Than',
        '< # Less Than',
        '>= # greater equal to',
        '<= # less or equal to',
        '!= # NOT equal to',
        "",
        sep = "\n", end = "\n################ END. ###################\n")
        

def notes():
    # Ask for a user input of the name of the notes you want to print

    module_select = ""
    
    while True:
        module_select = input("Input your selection: \n"
                              "\n"
                              "Type 'contents' without quotes, for contents.\n"
                              "Type 'exit' without quotes, to exit. \n"
                              "\n")
        if module_select == "exit":
            break
        elif module_select == "contents":
            contents()
        elif module_select == "general":
            general()
        elif module_select == "loops":
            loops()
        elif module_select == "strings":
            strings()
        elif module_select == "lists":
            lists()
        elif module_select == "readwrite":
            readwrite()
        elif module_select == "boolean":
            boolean()
        else:
            print("Invalid selection, please try again.")
notes()

