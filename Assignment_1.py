from loguru import logger

file_path = "pg1497.txt"

with open(file_path, encoding="utf8") as input_file:
    logger.debug(f"Reading input data from {file_path}...")
    data = input_file.read()
    logger.debug(f"Done, {len(data)} character(s) found.")
