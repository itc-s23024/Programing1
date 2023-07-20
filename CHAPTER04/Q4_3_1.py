def concat_words(*args, separator="."):
    return separator.join(args)


s = concat_words("a", "b", "c", "d", separator="_")
print(s)


e = concat_words("3_aja", "Naha", "Okinawa", "japan", separator=" ")
print(e)
