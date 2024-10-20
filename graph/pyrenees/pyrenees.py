from ridge_map import RidgeMap
import matplotlib.pyplot as plt
from pyfonts import load_font
from pypalettes import load_cmap

font = load_font(
    "https://github.com/googlefonts/imperial-script/blob/master/fonts/ttf/ImperialScript-Regular.ttf?raw=true"
)
cmap = load_cmap("Sunset2", cmap_type="continuous")
background_color = "#f6f6f6"

andorra_location = (1.574387, 42.558644)

location = (-1.476030, 41.697286, 2.973862, 43.746855)
rm = RidgeMap(location, font=font)
values = rm.get_elevation_data(num_lines=300)

ratio = (location[3] - location[1]) / (location[2] - location[0])
fig, ax = plt.subplots(dpi=300, figsize=(10, 10 * ratio))
fig.set_facecolor(background_color)
rm.plot_map(
    values=rm.preprocess(
        values=values, vertical_ratio=100, water_ntile=10, lake_flatness=1
    ),
    label="Pyrenees, France",
    label_y=0.1,
    label_x=0.1,
    label_size=40,
    linewidth=0.6,
    line_color=cmap,
    background_color=background_color,
    kind="elevation",
    ax=ax,
)

plt.savefig("graph/pyrenees/pyrenees.png", dpi=300, bbox_inches="tight")
