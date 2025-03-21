
#advanced python assignment.

import argparse
import logging

def setup_logging(level: str = "INFO"):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def process_message(message: str) -> str:
    """Gör om meddelandet till versaler (stora bokstäver)."""
    return message.upper()

def main():
    parser = argparse.ArgumentParser(description="Avancerat GitHub-uppdragsskript")
    parser.add_argument(
        "-m", "--message",
        type=str,
        default="Hello, GitHub assignment!",
        help="Meddelande att bearbeta"
    )
    parser.add_argument(
        "-l", "--log",
        type=str,
        default="INFO",
        help="Loggnivå (DEBUG, INFO, WARNING, ERROR)"
    )
    args = parser.parse_args()

    setup_logging(args.log)
    logging.info("Startar uppdragsskriptet.")

    result = process_message(args.message)
    logging.info(f"Bearbetat meddelande: {result}")
    print(result)

if __name__ == "__main__":
    main()
