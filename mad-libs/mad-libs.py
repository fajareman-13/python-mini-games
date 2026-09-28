#write a story
def mad_libs():
    print("\nLet's create a story. Fill in the blanks.")
    noun = input("Noun: ")
    verb = input("Verb: ")
    Adjective = input("Adjective: ")
    place = input("Place: ")

    story = f"Once upon a time , a {Adjective} {noun} decided to {verb} to {place}. Everyone was surpised but it turned out to be the best idea ever."
    print("\n Here is your story.\n")
    print(story)

mad_libs()
