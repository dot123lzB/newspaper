#!/usr/bin/env bash
# Usage: bash bootstrap.sh /home/claude/newspaper   (run after placing assets/style.css and tools/*.py)
set -e
R="${1:-/home/claude/newspaper}"; mkdir -p "$R/assets/fonts" "$R/work" "$R/out"
T="$(mktemp -d)"; cd "$T"; npm init -y >/dev/null 2>&1
npm install @fontsource/unifrakturmaguntia @fontsource/source-serif-4 @fontsource/libre-franklin >/dev/null 2>&1
F="$T/node_modules/@fontsource"
cp $F/unifrakturmaguntia/files/unifrakturmaguntia-latin-400-normal.woff2 "$R/assets/fonts/"
for w in 400-normal 400-italic 600-normal 700-normal 700-italic 900-normal; do cp $F/source-serif-4/files/source-serif-4-latin-$w.woff2 "$R/assets/fonts/"; done
for w in 500 700 800; do cp $F/libre-franklin/files/libre-franklin-latin-$w-normal.woff2 "$R/assets/fonts/"; done
ls "$R/assets/fonts" | wc -l
