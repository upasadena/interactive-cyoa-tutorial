# install pandoc if you haven't already
find . -iname "*.md" | xargs pandoc -f markdown-tex_math_dollars --strip-comments -t plain | wc -w