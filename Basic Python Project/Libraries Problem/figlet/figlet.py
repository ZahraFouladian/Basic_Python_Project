def main():

    from sys import argv, exit
    from pyfiglet import Figlet
    import random


    fig_object = Figlet()
    font_ls = fig_object.getFonts()


    if len(argv) == 1:
        font_choice = random.choice(font_ls)
        fig_object.setFont(font=font_choice)
    elif len(argv) == 3:
        if argv[1] in ["-f", "--font"]:
            font_input = argv[2]
            fig_object.setFont(font=font_input) if font_input in font_ls else exit(
                "Invalid usage"
            )
        else:
            exit("Invalid usage")
    else:
        exit("Invalid usage")

        
    text = input("Input: ")
    print(fig_object.renderText(text))


if __name__ == "__main__":
    main()
