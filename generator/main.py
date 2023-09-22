# Imports
import json
import concurrent.futures

from time import perf_counter
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classes.data_generator import DataGenerator


def process_generated_data(first_names, last_names, words_dictionary, industry_category_dictionary):
    """ We process the data to insert in the database """
    # We create the arrays for inserting the data
    workers_to_insert = []
    debtors_to_insert = []
    cases_to_insert = []
    payments_to_insert = []

    workers_to_insert_count = 0
    debtors_to_insert_count = 0
    cases_to_insert_count = 0
    payments_to_insert_count = 0

    return tuple((workers_to_insert_count, debtors_to_insert_count, cases_to_insert_count, payments_to_insert_count))







def process_config_values(value) -> list | int:
    """ We produce a list of integers from a string of comma separated values
    In case the value doesn't contain a comma, we return a single value as an integer """
    if ',' in value:
        return [int(x) for x in value.split(',')]
    else:
        return int(value)

# Main program
if __name__ == "__main__":
    # We initialize the timer
    time_start = perf_counter()
    try:
        engine = create_engine(
            f"mysql+pymysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@{config('MYSQL_DATABASE_HOST')}:{config('MYSQL_DATABASE_PORT')}/{config('MYSQL_DATABASE')}",
            pool_size=20, max_overflow=10)
    except Exception as err:
        print(f"Error trying to create the engine, error: {err}")
        raise Exception(err)
    else:
        print("created the engine")

    # We load a json with sample data
    first_names = None
    with open(r"resources/first_names.json", 'r') as json_file:
        first_names = list(json.load(json_file))
    last_names = None
    with open(r"resources/last_names.json", 'r') as json_file:
        last_names = list(json.load(json_file))

    # We initialize the counters
    workers_to_insert = 0
    debtors_to_insert = 0
    cases_to_insert = 0
    payments_to_insert = 0

    # We load the configuration
    WORKERS = process_config_values(config('WORKERS'))
    DEBTORS_PER_WORKER = process_config_values(config('DEBTORS_PER_WORKER'))
    CASES_PER_DEBTOR = process_config_values(config('CASES_PER_DEBTOR'))
    PAYMENTS_PERCENTAGES = process_config_values(config('PAYMENTS_PERCENTAGES'))
    PAYMENTS_FAILED_PERCENTAGE = process_config_values(config('PAYMENTS_FAILED_PERCENTAGE'))

    # We create the scoped session
    session_factory = sessionmaker(bind=engine)

    data_generator = DataGenerator(
                        first_names, 
                        last_names,
                        DEBTORS_PER_WORKER,
                        CASES_PER_DEBTOR,
                        PAYMENTS_PERCENTAGES,
                        PAYMENTS_FAILED_PERCENTAGE
                    )

    # We use multithreading for each of the workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        data_insertion = [executor.submit(data_generator.process_generated_data, session_factory) for _ in range(0, WORKERS)]

    for result in concurrent.futures.as_completed(data_insertion):
        workers_to_insert += result.result()[0]
        debtors_to_insert += result.result()[1]
        cases_to_insert += result.result()[2]
        payments_to_insert += result.result()[3]

    print(f"We have inserted {workers_to_insert} workers")
    print(f"We have inserted {debtors_to_insert} debtors")
    print(f"We have inserted {cases_to_insert} cases")
    print(f"We have inserted {payments_to_insert} payments")
    time_transcurred = perf_counter() - time_start
    print(f"Finished the program, it took {round(time_transcurred, 2)} seconds")
