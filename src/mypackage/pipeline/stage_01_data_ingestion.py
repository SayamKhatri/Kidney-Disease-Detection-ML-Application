from mypackage.config.configuration import ConfigurationManager
from mypackage.components.data_ingestion import DataIngestion
from mypackage import logger

STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} started')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e