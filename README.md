# ebook-tools
Tools for writing ebooks


Process
Write in markdown with IA writer (or Jupyer Notebook first).

Convert markdown to html with pandoc.

Convert html to epub and pdf with calibre. (see css for calibre)

Remove emoji with script for epub version that will become mobi for Kindle.

Convert emoji-free epub to mobi with kindlegen.

Upload mobi to Kindle preview.

Upload other versions to own site.

And this is just the ebook stuff :)

Almost too easy.


```
pandoc ../Dropbox/ds/books/memorable_docker/memorable_docker.md  --toc --template="default.html" --toc-depth=2 -so ../Dropbox/ds/books/memorable_docker/memorable_docker2.html --number-sections --top-level-division=chapter --filter=twohead.hs  --resource-path=../Dropbox/ds/books/memorable_docker --metadata pagetitle="Memorable Docker"
``` 
