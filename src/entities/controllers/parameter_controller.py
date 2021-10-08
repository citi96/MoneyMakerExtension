from sqlalchemy.sql.expression import false
from entities.models.parameter import Parameter
from utilities import utilities


class ParameterController:
    @staticmethod
    def save(parameter: Parameter):
        with utilities.get_session() as session, session.begin():            
            session.add(parameter)

    @staticmethod
    def update(parameter: Parameter, props):
        with utilities.get_session() as session, session.begin():
            for key, value in props.items():
                setattr(parameter, key, value)

    @staticmethod
    def get(key):
        param = None
        with utilities.get_session() as session, session.begin():
             param = session.query(Parameter).get(key)
        
        return param