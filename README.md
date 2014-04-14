# Perforce Plugin for Sublime Text 3

No, it's not a *real* plugin.  It's just a hack that copies the file path to the clipboard so I can check it out in Perforce without getting stuck in a loop (the loop's not a problem with ST3).

## Installation
1. In Sublime, go to Preferences > Browse Packages.
2. Create a directory called `JGreer`.
3. Put `JGreer.py` in the directory.
4. Restart Sublime (why not?).

## Usage
When saving a file, if the file is read-only, a message will appear telling you to "check it out."  At this point, the file path is in the clipboard.  Go to Perforce and check out the file.  Return to Sublime, hit OK, and carry on.