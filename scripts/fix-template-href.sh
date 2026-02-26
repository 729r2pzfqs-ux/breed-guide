#!/bin/bash
# Fix template literal hrefs that Google crawls as literal strings
# Changes href="../breeds/${...}" to data-href="../breeds/${...}" href="#"
# This prevents Google from seeing broken URLs

echo "Fixing template literal hrefs in HTML files..."

find . -name "*.html" -type f | while read file; do
    # Check if file has the pattern
    if grep -q 'href="[^"]*\${' "$file" 2>/dev/null; then
        echo "Fixing: $file"
        # Replace href="...${..." with href="#" data-href="...${..."
        sed -i '' 's|href="\([^"]*\${\)|href="#" data-href="\1|g' "$file"
    fi
done

echo "Done! Don't forget to update JS to use data-href for navigation."
