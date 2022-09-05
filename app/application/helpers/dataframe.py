from typing import List, TypedDict


class Dataframe(TypedDict):
    columns: List

class PandasDataFrame(TypedDict):
    dataframe: Dataframe