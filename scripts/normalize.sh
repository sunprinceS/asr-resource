#!/usr/bin/bash

cat $1 | tr -d ":" | tr -d "." | tr -d "," | tr -d "()" | tr -d '"' | tr -d "?" | gawk '{print tolower($0);}' 
