#! python3
# P01_mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe P01_mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe P01_mcb.pyw delete <keyword> - Deletes keyword from database.
#        py.exe P01_mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe P01_mcb.pyw list - Loads all keywords to clipboard.
#        py.exe P01_mcb.pyw delete - Deletes all keywords from database.
#
# Extend the multiclipboard program in this chapter so that it has a delete <keyword>
# command line argument that will delete a keyword from the shelf. Then add a delete
# command line argument that will delete all keywords.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# Delete clipboard content.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # List keywords, delete all keywords, and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
