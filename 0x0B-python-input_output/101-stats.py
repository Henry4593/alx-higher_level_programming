#!/usr/bin/python3
"""Processes input from standard input, calculating and reporting
    statistics.
"""


def print_stats(size: int, status_codes: dict) -> None:
    """Displays accumulated metrics, including total file size and status code
       counts.

    Args:
        size: The total size of processed files.
        status_codes: A dictionary containing the counts of encountered status
                      codes.
    """

    print("File size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    """Main execution block, handling input processing and metric reporting."""

    import sys

    size = 0
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            # Process every 10 lines or upon keyboard interruption
            if count == 10 or count == 1:
                print_stats(size, status_codes)
                count = 1

            # Extract file size and status code from parsed line
            line_parts = line.split()
            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    status_codes[line_parts[-2]] = (status_codes.
                                                    get(line_parts[-2], 0) + 1)
            except IndexError:
                pass

        # Print final statistics
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
