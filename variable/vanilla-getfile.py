# vanilla getfile example
# the vanilla module must be installed

from vanilla.dialogs import getFile

file_paths = getFile('Get a file from Drawbot:')
file_path = file_paths[0]

f = open(file_path, 'r')
print f.read()
