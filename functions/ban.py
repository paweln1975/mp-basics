def banner_text(text):
    screen_width = 80
    asterix = "*"
    if len(text) > screen_width - 4:
        raise ValueError("The text is too long. Len={0}".format(len(text)))
    else:
        if text == asterix:
            centered_text = asterix * screen_width
        else:
            centered_text = text.center(screen_width - 4)
            centered_text = (asterix + asterix + "{0}" + asterix + asterix).format(centered_text)
        print(centered_text)


banner_text("*")
banner_text("*")
banner_text("")
banner_text("")
banner_text("HELLO WORLD")
banner_text("")
banner_text("")
banner_text("*")
banner_text("*")