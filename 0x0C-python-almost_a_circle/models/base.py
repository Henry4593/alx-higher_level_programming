#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """
    Base class for various object representations in project 0x0C*.

    Attributes:
        id (int): Unique identifier assigned automatically or provided
        upon initialization.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base object.

        Args:
            id (int, optional): Unique identifier. Defaults to an
                auto-incremented value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serializes a list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Raises:
            TypeError: If any element in the list is not a dictionary.
            JSONDecodeError: If JSON serialization encounters issues.

        Returns:
            str: JSON-encoded string representing the list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list of objects as CSV file.
        Args:
            list_objs (list): List of inherited Base objects.

        Raises:
            Errors: For invalid objects, attributes, or file access.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a JSON string into a Python list.
        Args:
            json_string (str): JSON string representing a list of dictionaries.
        Returns:
            list: Python list containing the deserialized data,
            or empty list if input is invalid.
        Raises:
            JSONDecodeError: If the JSON string is malformed.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Creates an instance of the class from a dictionary.
        Args:
            **dictionary (dict): Attribute values for initialization.
        Returns:
            The created instance.
        Raises:
            TypeError: If the dictionary contains invalid attribute names.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Loads instances of the class from a JSON file.

        Returns:
            list: List of instantiated objects, or empty list if
            file not found.

        Raises:
            IOError: If the JSON file is invalid.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects inheriting from the Base class.
            Each object must have the following attributes:
               - 'id' (int): Unique identifier of the object.
               - 'x' (float): x-coordinate of the object's position.
               - 'y' (float): y-coordinate of the object's position.
               - 'width' (float, optional): Width of the object
                 (for rectangles).
               - 'height' (float, optional): Height of the object
                 (for rectangles).
               - 'size' (float, optional): Side length of the object
                 (for squares).
               - 'to_dictionary()' method: Returns a dictionary representation
                 of the object.

        Raises:
            TypeError: If any object in `list_objs` is not a subclass of
                Base or lacks the required attributes.
            AttributeError: If any object in `list_objs` is missing the
                 'to_dictionary()' method.

        Examples:
            >>> Rectangle.save_to_file_csv([Rectangle(1, 10, 20, 15, 25)])
        # Creates a CSV file named "Rectangle.csv" with one row representing
             the rectangle

            >>> Square.save_to_file_csv([Square(2, 50, 50, 30)])
        # Creates a CSV file named "Square.csv" with one row representing
             the square
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Loads a list of `cls` objects from a CSV file.

        This function reads data from a CSV file named `<cls.__name__>.csv`
        located in the same directory as the class definition. Each row in the
        CSV file represents a single object of the specified class.

        Args:
            cls (class): The class of objects to be loaded from the CSV file.

        Returns:
            list: A list of `cls` objects instantiated from the CSV data.
                - If the file does not exist, an empty list is returned.
                - Otherwise, the list contains instances created using the
                 `create` method of the class, with each instance's attributes
                    populated from the corresponding row in the CSV file.

        Raises:
            IOError: If the CSV file cannot be opened or read.

        Examples:
            >>> loaded_rectangles = Rectangle.load_from_file_csv()
            # Loads a list of Rectangle objects from "Rectangle.csv"

            >>> Square.load_from_file_csv()  # Raises IOError if "Square.csv"
                doesn't exist
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value
                              in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Visually display a collection of rectangles and squares.

        Args:
            list_rectangles(list): A list of `Rectangle` objects defining
                            position (x, y) and dimensions (width, height).
            list_squares(list): A list of `Square` objects defining position
                            (x, y) and side length.

        Each object is drawn using the turtle graphics library with a
        distinctive color. The function sets up the drawing environment,
        then iterates through each rectangle and square:
            1. Positions the turtle at the object's location.
            2. Draws the shape using forward and turn commands based on the
                object's dimensions.
            3. Optionally hides the turtle after drawing.

        Finally, the function waits for a mouse click before closing the window.

        Raises:
            TypeError: If either input list contains objects of an unexpected
            type.
        """
        turt_obj = turtle.Turtle()
        turt_obj.screen.bgcolor("#b7312c")
        turt_obj.pensize(3)
        turt_obj.shape("turtle")

        turt_obj.color("#ffffff")
        for rect in list_rectangles:
            turt_obj.showturtle()
            turt_obj.up()
            turt_obj.goto(rect.x, rect.y)
            turt_obj.down()
            for idx_i in range(2):
                turt_obj.forward(rect.width)
                turt_obj.left(90)
                turt_obj.forward(rect.height)
                turt_obj.left(90)
            turt_obj.hideturtle()

        turt_obj.color("#b5e3d8")
        for sq in list_squares:
            turt_obj.showturtle()
            turt_obj.up()
            turt_obj.goto(sq.x, sq.y)
            turt_obj.down()
            for idx_i in range(2):
                turt_obj.forward(sq.width)
                turt_obj.left(90)
                turt_obj.forward(sq.height)
                turt_obj.left(90)
            turt_obj.hideturtle()

        turtle.exitonclick()
