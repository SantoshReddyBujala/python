import argparse


def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }

    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Provide a person name to greetings"
    )

    parser.add_argument(
        "-n", "--name", metavar="Name", required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="Language", choices=["English", "Spanish", "German"], required=True, help="The language of the greeting"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
