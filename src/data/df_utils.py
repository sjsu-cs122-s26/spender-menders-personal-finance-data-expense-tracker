import pandas as pd


def orm_to_df(objects, model_class):
    """
    Convert a list of SQLAlchemy ORM objects to a pandas DataFrame.
    It prevents pandas error due to empty DataFrame.

    Args:
        objects (list): List of SQLAlchemy ORM objects.
        model_class: The SQLAlchemy model class corresponding to the objects.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the ORM objects.
    """

    columns = [column.name for column in model_class.__table__.columns]
    rows = [{c: getattr(o, c) for c in columns} for o in objects]

    df = pd.DataFrame(rows, columns=columns)
    return df

def convert_date_to_month(date):
    """
    Convert a date to a month string in the format 'YYYY-MM-DD'.

    Args:
        date (datetime): The date to convert.
    """
    return date.strftime('%B')
