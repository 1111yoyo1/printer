import win32print
import win32api
import os


def Print(fileloc):
    oldDir = os.getcwd()
    curfolder = os.path.dirname(fileloc)
    filename = os.path.basename(fileloc)
    print "filename %s" % filename
    os.chdir(curfolder)
    currentprinter = win32print.GetDefaultPrinter()
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % currentprinter, ".", 0)
    os.chdir(oldDir)


curfolder = os.path.dirname(os.path.realpath(__file__))
curfileloc = os.path.realpath(__file__)
printedTxt = os.path.join(curfolder, "printed.txt")

skipFiles = []
with open(printedTxt, "r") as f:
    skipFiles = f.readlines()

skipFiles = map(lambda x: x.strip(), skipFiles)
#print skipFiles
#raise
allFiles = []
for root, subdir, files in os.walk(curfolder):
    #print root
    #print files
    for file in files:
        fileLoc = os.path.join(root, file)
        allFiles.append(fileLoc)

for tbdFile in allFiles:
    #for skipFile in skipFiles:
    if tbdFile in skipFiles or printedTxt == tbdFile or curfileloc == tbdFile:
        print "skip %s" % tbdFile
        continue
    else:
        print "print %s" % tbdFile
        Print(tbdFile)
        print "Write record for %s" % tbdFile
        with open(printedTxt, "a") as f:
            f.write("".join([tbdFile, "\n"]))
