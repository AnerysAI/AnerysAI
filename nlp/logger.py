import logging
import os
from datetime import datetime

class ChatLogger:
    """Logger untuk tracking conversation dan performance"""
    
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Setup file logging
        log_file = os.path.join(
            log_dir, 
            f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def log_prediction(self, text, intent, confidence):
        """Log prediction result"""
        self.logger.info(f"Input: '{text}' | Intent: {intent} | Confidence: {confidence:.4f}")
    
    def log_error(self, error_msg):
        """Log error"""
        self.logger.error(f"Error: {error_msg}")
    
    def log_conversation(self, user_msg, bot_response, intent, confidence):
        """Log full conversation turn"""
        self.logger.info(f"USER: {user_msg} | BOT: {bot_response} | Intent: {intent} ({confidence:.2%})")
