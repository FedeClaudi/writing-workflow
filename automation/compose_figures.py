from fcutils.file_io.io import load_yaml
from fcutils.plotting.utils import save_figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from rich import print
from pyinspect._colors import mocassin, orange

print(f'[{mocassin}]Generating [{orange}]figures[/{orange}][{mocassin}]...\n')


metadata = load_yaml('figures/composed_figures.yml')
figs_folder = Path('figures')

for figname, figs in metadata.items():
    if len(figs) < 2:
        ncols, nros = 1, 1
    elif len(figs) < 3:
        ncols, nrows = 2, 1
    elif len(figs) < 5:
        ncols, nrows = 2, 2
    elif len(figs) < 7:
        ncols, nrows = 3, 2

    f, axarr = plt.subplots(ncols=ncols, nrows=nrows, figsize=(18, 13))
    f.suptitle(figname)
    for ax in axarr.flatten():
        ax.axis('off')

    for ax, (title, fig) in zip(axarr.flatten(), figs):
        ax.imshow(mpimg.imread(figs_folder / fig))
        ax.set(title=title)

    f.tight_layout()
    save_figure(f, figs_folder / figname, verbose=False)
    