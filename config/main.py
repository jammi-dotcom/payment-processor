import logging
import os
from payment_processor.config import Config
from payment_processor.payment_gateway import PaymentGateway
from payment_processor.payment_processor import PaymentProcessor

def main():
    logging.basicConfig(level=logging.INFO)
    config = Config(os.environ.get('CONFIG_FILE', 'config.json'))
    payment_gateway = PaymentGateway(config.payment_gateway_url)
    payment_processor = PaymentProcessor(payment_gateway, config)

    try:
        payment_processor.process_payments()
    except Exception as e:
        logging.error(f"Error processing payments: {str(e)}")

if __name__ == "__main__":
    main()