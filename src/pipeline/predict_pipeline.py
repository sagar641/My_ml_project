import sys
import pandas as pd
from src.exception import CustomException
from src.utils import loadobject


class PredictPipeline:
    def __init__(self) -> None:
        pass

class CustomData:
    def __init__(self,
        gender: str,
        race_ethinicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender
        self.race_ethinicity = race_ethinicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch= lunch
        self.test_preparation_course= test_preparation_course
        self.reading_score= reading_score
        self.writing_score=writing_score