#!/bin/bash
# Fix language switcher relative paths in compare pages
# Changes ../XX/compare/ to ../../XX/compare/ (except English which should be ../../compare/)

for file in */compare/index.html; do
    echo "Fixing: $file"
    # Fix language paths: ../XX/compare/ → ../../XX/compare/
    sed -i '' 's|value="\.\./\([a-z][a-z]\)/compare/"|value="../../\1/compare/"|g' "$file"
    # English path is already correct: ../../compare/
done

echo "Done! All compare pages fixed."
