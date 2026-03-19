import logging
from payment_processor.config import Config
from payment_processor.payment_gateway import PaymentGateway
from payment_processor.database import Database

def main():
    logging.basicConfig(level=logging.INFO)

    config = Config()
    database = Database(config.database_url)
    payment_gateway = PaymentGateway(config.payment_gateway_url)

    while True:
        try:
            logging.info("Processing payments...")
            payment_gateway.process_payments()
            database.commit()
        except Exception as e:
            logging.error(f"Error processing payments: {e}")
            database.rollback()

if __name__ == "__main__":
    main()