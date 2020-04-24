from io import BytesIO

import matplotlib.pyplot as plt


def renderLatex(formula, fontsize=12, dpi=300, format='svg', file=None):
    """
    Renders LaTeX formula into image or prints to file.

    Parameters
    ----------
    formula
    fontsize
    dpi
    format
    file

    Returns
    -------

    """
    fig = plt.figure(figsize=(0.01, 0.01))
    text = fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)

    fig.savefig(BytesIO(), dpi=dpi)  # triggers rendering

    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.05
    fig.set_size_inches((width, height))

    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    output = BytesIO() if file is None else file
    fig.savefig(output, dpi=dpi, transparent=True, format=format,
                bbox_inches='tight', pad_inches=0.0)

    plt.close(fig)

    if file is None:
        output.seek(0)
        return output