#!/usr/bin/bash 

# the following script is for tundra-all
lang=$1
if [[ -d handmadeTest/txt ]];then
  cat handmadeTest/txt/*.txt | tr -d ":" | tr -d "." | tr -d "," | tr -d "()" | tr -d '"' | tr -d "?" | tr " " "\n" | sort | uniq > handmadeTest.wlist
fi

if [[ -d train/txt ]]; then
  cat train/txt/*.txt | tr -d ":" |  tr -d "." | tr -d "," |  tr -d "()" |  tr -d '"' | tr -d "?" | tr " " "\n" | sort | uniq > train.wlist
fi

if [[ -d test/txt ]]; then
  cat test/txt/*.txt |  tr -d ":" | tr -d "." | tr -d "," |  tr -d "()" |  tr -d '"' | tr -d "?" | tr " " "\n" | sort | uniq > test.wlist
fi

cat handmadeTest.wlist train.wlist test.wlist | gawk '{print tolower($0);}' | sort | uniq > $lang.wlist
