import os
import subprocess
import logging
from datetime import datetime

class AutoZone:
    def __init__(self):
        self.logger = self.setup_logger()
        self.logger.info("AutoZone initialized.")

    def setup_logger(self):
        logger = logging.getLogger('AutoZoneLogger')
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler('autozone.log')
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def check_for_updates(self):
        self.logger.info("Checking for updates...")
        try:
            result = subprocess.run(['powershell', 'Get-WindowsUpdate'], capture_output=True, text=True)
            self.logger.info("Updates check completed.")
            return result.stdout
        except Exception as e:
            self.logger.error(f"Error checking for updates: {e}")
            return None

    def install_updates(self):
        self.logger.info("Installing updates...")
        try:
            result = subprocess.run(['powershell', 'Install-WindowsUpdate', '-AcceptAll'], capture_output=True, text=True)
            self.logger.info("Updates installation completed.")
            return result.stdout
        except Exception as e:
            self.logger.error(f"Error installing updates: {e}")
            return None

    def restart_system(self):
        self.logger.info("Restarting system...")
        try:
            os.system("shutdown /r /t 0")
            self.logger.info("System restart initiated.")
        except Exception as e:
            self.logger.error(f"Error restarting system: {e}")

    def run(self):
        updates = self.check_for_updates()
        if updates:
            self.logger.info("Available updates: \n" + updates)
            self.install_updates()
            self.restart_system()
        else:
            self.logger.info("No updates available.")

if __name__ == "__main__":
    autozone = AutoZone()
    autozone.run()