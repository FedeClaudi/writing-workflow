# writing-workflow
Workflow for writing stuff: figures in .py, write in .md > convert to .html / .pdf / .docx

## Overview
The idea is to write a paper as a series of `.md` files and then use `pandoc` to convert these to other formats you might need.
You `.md` files should be put in **paper** and they should be named `00_xxx.md`, `01_xxx.md` etc.
If you need to include figures you can keep these in **figures**, the data and scripts used to generate figures can be kept in the **data** and **scripts** folders.

Once you're ready to convert your markdown to other format, run `compile.sh` and magic will happen (more details below)

## Folders
- **automation**: scripts used in the manuscript generation process
- **data**: include any data file you might need (e.g. to generate figures)
- **figures**: save your figures here
- **paper**: save your `.md` files with the paper content here
- **scripts**: save `.py` files used to generate figures here

## .md files
As stated above, these should be in **paper** and the names should start with a number indicating the order in which the individual `.md` files will be concatenated to produce a single output

## Figures
You can use scripts in **scripts** to generate the figures you need.
If you need to combine multiple figures into a larger figure, you can use `automation/compose_figures.py` (this happens by itself when you run `compile.sh`).
All you need to do is to specify in  `figures/composed_figures.yml` how figures should be combined.
Entries in the `yml` file should have the structure:

```yaml
FigTile:
 - [subplot_title, path/to/sub1.png]
 - [subplot_title, path/to/sub2.png]
 ...
```

This information will be used to combine the various subplots and save a new figure in as `figures/FigTitle.png`.
To include figures in your paper, in your `.md` files add: `![](../figures/fig.png){ width=600px }`


## Automation
If you need to update all figures, the easiest way is tu run `bash run_all_scripts.sh`.
This will runn all `.py` scripts into **scripts** (which should generate all the figures you need).

> Remember, to combine individual figures into more complex one, use `automation/compose_figures.py`

The other important automation script is running `compile.sh`, but more about that in a sec.


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