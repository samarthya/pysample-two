"""Filer

    Raises:
        ValueError: When the value to be read is not found

    Returns:
        Filer: Filer class allows you to read a line in the file
    """
import logging


class Filer:
    """Filer
        Defines the read file function for reading content
    """
    logger = logging.getLogger(__name__)

    def __init__(self, file_path, level=20):
        self.file_path = file_path
        self.logger.setLevel(level)
        self.logger.info('Instance created')

    def __str__(self):
        return f"File({self.file_path})"

    def read_line(self, line_number: int) -> str:
        """dump_line

        Args:
            line_number (int): Line to read from the file

        Raises:
            ValueError: In case line is not present

        Returns:
            str: Line read
        """

        try:
            with open(self.file_path, encoding="utf-8") as file:
                lines = file.readlines()
                if len(lines) < line_number:
                    raise ValueError(
                        f"File {self.file_path} has less lines than"
                        f" the expected line number {line_number}")
                if self.logger:
                    self.logger.info(
                        "Reading line %d from file %s", line_number, self.file_path)
                self.logger.debug("Line read %s", lines[line_number - 1])
                return lines[line_number - 1]
        except FileNotFoundError as fnf:
            if self.logger:
                self.logger.error("File %s not found.", self.file_path)
            raise FilerException(f"File {self.file_path} not found.") from fnf
        except ValueError as ver:
            if self.logger:
                self.logger.error(ver)
            raise FilerException(f"Line {line_number} not found.") from ver


class FilerException(BaseException):
    """FilerException

    Args:
        BaseException (_type_): Raises Filer exceptions for file not found and line not found
    """

    def __init__(self, msg: str):
        self.message = msg
