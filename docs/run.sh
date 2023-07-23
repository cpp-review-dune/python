#! /usr/bin/env bash

DATE=2022-11-06
ENGINE=lualatex
# DATE=$(date -u +"%Y-%m-%d")

if ! [ -e ieee.csl ]; then
  curl -O https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl
fi

pandoc $DATE/*.md \
  -t beamer \
  -V lang=es \
  --pdf-engine=$ENGINE \
  --pdf-engine-opt=-shell-escape \
  --bibliography biblio.bib \
  --citeproc \
  --csl=ieee.csl \
  -o $DATE.pdf
# --toc --toc-depth=2 --metadata date="$(date -u '+%Y-%m-%d')"

if [ -e /etc/debian_version ]; then
  okular $DATE.pdf &
elif [ -e /etc/arch-release ]; then
  zathura $DATE.pdf &
fi
