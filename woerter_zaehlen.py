def zaehle_woerter(text: str):
    woerter = text.split()

    woerter_dict = {}

    for wort in woerter:
        wort = wort.lower()
        if wort in woerter_dict.keys():
            woerter_dict[wort] += 1
        else:
            woerter_dict[wort] = 1

    return woerter_dict

text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
print(zaehle_woerter(text))