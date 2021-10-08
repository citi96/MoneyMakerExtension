from sqlalchemy import Column, String
from sqlalchemy.sql.expression import desc
from utilities import utilities


Base = utilities.get_base()


class Parameter:
    DEFAULT_RESOLUTION_X = "default_resolution_x"
    DEFAULT_RESOLUTION_Y = "default_resolution_y"
    TOP_COLUMN_DEFAULT_COORD_X = "top_column_default_coord_x"
    TOP_COLUMN_DEFAULT_COORD_Y = "top_column_default_coord_y"
    MIDDLE_COLUMN_DEFAULT_COORD_X = "middle_column_default_coord_x"
    MIDDLE_COLUMN_DEFAULT_COORD_Y = "middle_column_default_coord_y"
    BOTTOM_COLUMN_DEFAULT_COORD_X = "bottom_column_default_coord_x"
    BOTTOM_COLUMN_DEFAULT_COORD_Y = "bottom_column_default_coord_y"

    __tablename__ = "parameters"
    key = Column(String(20), primary_key=True)
    value = Column(String(50))
    description = Column(String(50))

    def __init__(self, key, value, description):
        self.key = key
        self.value = value
        self.description = description


Base.metadata.create_all()