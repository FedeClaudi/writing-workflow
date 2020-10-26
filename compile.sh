python automation/compose_figures.py

cd paper
rm paper.md


echo "generating .md"
pandoc *.md -o paper.md -t markdown --bibliography=bib.bib --toc --strip-comments
echo "    ... done"
python ../automation/count_words.py paper.md


echo ""
echo "generating .html"
pandoc -f markdown -t html -s paper.md -o paper.html -c pandoc.css --metadata title="Brainrender" --filter pandoc-citeproc --bibliography=bib.bib
echo "    ... done"

    for MYFIELD in "$@"; do

        CHECKFIRST=`echo $MYFIELD | cut -c1`

        if [ "$CHECKFIRST" == "-" ]; then
            mode="flag"
        else
            mode="arg"
        fi

        if [ "$mode" == "flag" ]; then
            case $MYFIELD in
                -p)
                    echo ""
                    echo "generating .pdf"
                    pandoc --filter pandoc-citeproc --bibliography=bib.bib --variable classoption=twocolumn --variable papersize=a4paper -s paper.md -o paper.pdf
                    echo "    ... done"
                    ;;
                -w)
                    echo ""
                    echo "generating .word"
                    pandoc  -s paper.html -f html+smart -o paper.docx
                    echo "    ... done"
                    ;;
                -s)
                    open -a firefox paper.html
                    ;;
            esac
        fi
    done

cd ../



