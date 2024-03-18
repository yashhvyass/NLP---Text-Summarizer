# text summarizer is installed as a local package in setup.py
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise(e)