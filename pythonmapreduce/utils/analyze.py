import os
import random
from pathlib import Path

import matplotlib.pyplot as plt


class Scatter:
    def __init__(self, relations=None):
        self.relations = dict()
        if relations is not None:
            self.relations = relations

    def append(self, name: str, data):
        self.relations[name] = data

    def plot(self, plot_title: str, x_axis: str, y_axis: str, fname: str):
        if not os.path.isdir(Path("data", "plots")):
            os.makedirs(Path("data", "plots"))
        for title, data in self.relations.items():
            r = lambda: random.randint(0, 255)
            x = data[0]
            y = data[1]
            plt.scatter(
                x,
                y,
                c="#%02X%02X%02X" % (r(), r(), r()),
                alpha=0.3,
                label=title,
                edgecolors="none",
            )
        plt.xlabel(x_axis)  # Add an x-label to the axes.
        plt.ylabel(y_axis)  # Add a y-label to the axes.
        plt.title(plot_title)  # Add a title to the axes.
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.75, 0.5), loc="center right")
        plt.savefig(
            fname=Path("data", "plots", f"{fname}.png"),
            dpi=300,
            format="png",
            bbox_inches="tight",
        )
        plt.savefig(
            fname=Path("data", "plots", f"{fname}.svg"),
            dpi=300,
            format="svg",
            bbox_inches="tight",
        )
        plt.close()
