# writing-workflow
Workflow for writing stuff: figures in .py, write in .md > convert to .html / .pdf / .docx

## Overview
The idea is to write a paper as a series of `.md` files and then use `pandoc` to convert these to other formats you might need.
You `.md` files should be put in **paper** and they should be named `00_xxx.md`, `01_xxx.md` etc.
If you need to include figures you can keep these in **figures**, the data and scripts used to generate figures can be kept in the **data** and **scripts** folders.

Once you're ready to convert your markdown to other format, run `compile.sh` and magic will happen (more details below)

## Folders
- **data**: include any data file you might need (e.g. to generate figures)
- **figures**: save your figures here
- **paper**: save your `.md` files with the paper content here
- **scripts**: save `.py` files used to generate figures here

## .md files
As stated above, these should be in **paper** and the names should start with a number indicating the order in which the individual `.md` files will be concatenated to produce a single output

## Producing output
To concatenate the individual `.md` files and produce a single output run:
```
bash compile.sh
```

This will
1. combine all `00_xxx.md` files into a single `paper.md` file with ALL the text.
2. convert this into a formatted `.html` which you can open in the browser

There's a few additional options you may pass to `bash compile.sh`
* `-s` opens hte `.html` file in the browser (firefox)
* `-w` saves a `paper.docx`  in **paper**
* `-p` saves a `paper.pdf`  in **paper**


## Citations
in **paper** you'll find a `bib.bib` file, add citations in Bibtex style there. 
Then, in your `.md` files add citations with things like:"[see @Claudi2020]" and they will be converted to proper citations in your output files!

## Figures
To include a figure, in the `.md` files use:
```
![fig1](../figures/fig1.png){ width=600px }
```