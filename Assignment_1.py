from loguru import logger
import argparse
import string

file_path = "pg1497.txt"

def count_characters(file_path):
    counts = {char: 0 for char in string.ascii_lowercase}
    #Rough equivalent
    # counts = {}
    # for char in string_ascii_lowercase
    #   counts{char} = 0
    with open(file_path, encoding="utf8") as input_file:
        logger.debug(f"Reading input data from {file_path}...")
        data = input_file.read()
    logger.debug(f"Done, {len(data)} character(s) found.")
    logger.info("Counting characters")
    for char in data:
        if char in counts:   
            counts[char] += 1
    logger.info(f"Character counts: {counts}")
    num_characters = sum(counts.values())
    logger.info(f"Total nnumber of characters: {num_characters}")
    for key, value in counts.item():
        counts(key) == value / num_characters
    logger.info(f"Character frequencies: {counts}")

        

"""if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the characters in a text file")
    parser.add_argument("file")
    args = parser.parse_args()
    count_characters(args.file)"""
