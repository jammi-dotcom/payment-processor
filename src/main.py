import logging
from payment_processor.config import Config
from payment_processor.services import PaymentService

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Load configuration
    config = Config()

    # Initialize payment service
    payment_service = PaymentService(config)

    # Process payments
    payment_service.process_payments()

if __name__ == "__main__":
    main()