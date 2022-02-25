#!/bin/sh

file_path="letters.txt"
pattern="veniam"
count=0

while read -r line; do
  if [[ $line =~ $pattern ]]; then
      count=$((count + 1))
  fi
done <$file_path

echo The pattern \"$pattern\" is found $count times in the file $file_path
