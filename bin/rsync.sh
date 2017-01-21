#!/bin/bash

set -x

FILES="*.html css js lib plugin"

ssh doughellmann.com 'mkdir -p ~/doughellmann.com/presentations/regexes-fear/'

rsync -av --progress $FILES doughellmann.com:~/doughellmann.com/presentations/regexes-fear/
