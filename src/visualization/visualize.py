import os
import matplotlib.pyplot as plt
import config

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(config.basedir, "reports/figures", fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)