import sys

import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.exception import MyException
from src.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.yes:int = 0
        self.no:int = 1
    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))

class MyModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        :param preprocessing_object: Input Object of preprocesser
        :param trained_model_object: Input Object of trained model 
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, dataframe: pd.DataFrame) -> DataFrame:
        """
        Function accepts inputs in the original format (before transformation),
        applies the same transformations as training, then applies preprocessing and prediction.
        """
        try:
            logging.info("Starting prediction process.")
            logging.info(f"Input dataframe columns: {dataframe.columns.tolist()}")
            logging.info(f"Input dataframe shape: {dataframe.shape}")

            # Step 1: Apply the same transformations as during training
            df = dataframe.copy()
            
            # Drop id column first if it exists (must be done before Gender mapping)
            if 'id' in df.columns:
                logging.info("Dropping 'id' column")
                df = df.drop('id', axis=1)
            
            # Map Gender column to 0 for Female and 1 for Male
            if 'Gender' in df.columns:
                logging.info("Mapping 'Gender' column to binary values")
                df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1}).astype(int)
            
            # Handle the Vehicle_Age and Vehicle_Damage columns if they come as separate columns
            # (In case the input is not pre-processed)
            if 'Vehicle_Age' in df.columns or 'Vehicle_Damage' in df.columns:
                logging.info("Creating dummy variables for categorical features")
                df = pd.get_dummies(df, drop_first=True)
                logging.info("Dummy variables created")
            
            # Rename columns if needed
            rename_dict = {
                "Vehicle_Age_< 1 Year": "Vehicle_Age_lt_1_Year",
                "Vehicle_Age_> 2 Years": "Vehicle_Age_gt_2_Years"
            }
            df = df.rename(columns=rename_dict)
            
            # Ensure integer types for dummy columns
            for col in ["Vehicle_Age_lt_1_Year", "Vehicle_Age_gt_2_Years", "Vehicle_Damage_Yes"]:
                if col in df.columns:
                    df[col] = df[col].astype('int')
            
            logging.info(f"After transformation, columns: {df.columns.tolist()}")

            # Step 2: Apply scaling transformations using the pre-trained preprocessing object
            logging.info("Applying preprocessing (scaling) transformations")
            transformed_feature = self.preprocessing_object.transform(df)
            logging.info("Preprocessing transformations completed")

            # Step 3: Perform prediction using the trained model
            logging.info("Using the trained model to get predictions")
            predictions = self.trained_model_object.predict(transformed_feature)

            return predictions

        except Exception as e:
            logging.error("Error occurred in predict method", exc_info=True)
            raise MyException(e, sys) from e


    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"