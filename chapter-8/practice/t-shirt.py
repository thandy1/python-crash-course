def make_shirt(size, text):
    print(
        f"The shirt size is \"{size}\".\n"
        f"The message on the shirt is \"{text}\"."
        )

make_shirt("Large", "Good Day") # Positional Argument
make_shirt(size="Large", text="Good Day") # Keyword argument