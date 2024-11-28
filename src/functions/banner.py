def banner_text(text: str = " ", width: int = 80) -> None:
    """
    Display a line of banner text. If text is '*' it displays '*' width times.

    :param text: any text with len is shorter then 80.
    :param width: `int` value - width of a line, default is 80.
    :return: None
    """
    asterix = "*"
    if width < 0 or width > 80:
        width = 80
    if len(text) > width - 4:
        raise ValueError("The text is too long. Len={0}".format(len(text)))
    else:
        if text == asterix:
            centered_text = asterix * width
        else:
            centered_text = text.center(width - 4)
            centered_text = (asterix + asterix + "{0}" + asterix + asterix).format(centered_text)
        print(centered_text)


width_gl = 60
banner_text("*", width_gl)
banner_text("*", width_gl)
banner_text(width=width_gl)
banner_text(width=width_gl)
banner_text("HELLO WORLD", width_gl)
banner_text(width=width_gl)
banner_text(width=width_gl)
banner_text("*", width_gl)
banner_text("*", width_gl)

print(banner_text.__doc__)
