#!/bin/bash

# Simple one-line script to remove yaml frontmatter and print the remainder of a file
gsed '1 { /^---/ { :a N; /\n---/! ba; d} }' $1
