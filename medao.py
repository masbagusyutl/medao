import requests
import time
from datetime import datetime, timedelta

# Function to read Telegram-Init-Data from data.txt
def read_telegram_init_data(file_path):
    with open(file_path, 'r') as file:
        telegram_init_data = file.read().strip()
    return telegram_init_data

# Function to claim using Telegram-Init-Data
def claim_rewards(telegram_init_data):
    url = 'https://zavod-api.mdaowallet.com/user/claim'
    headers = {
        'Telegram-Init-Data': telegram_init_data
    }
    response = requests.post(url, headers=headers)
    return response.status_code

# Function to display countdown and process information
def process_accounts(file_path):
    accounts = []
    with open(file_path, 'r') as file:
        accounts = file.readlines()
    
    total_accounts = len(accounts)
    print(f"Total accounts in data.txt: {total_accounts}")
    
    for idx, account in enumerate(accounts, start=1):
        telegram_init_data = account.strip()
        print(f"Processing account {idx} out of {total_accounts}")
        print("Claiming rewards...")
        status_code = claim_rewards(telegram_init_data)
        print(f"Claim status: {status_code}")
        
        # Countdown for next claim in 2 hours
        countdown_seconds = 2 * 60 * 60  # 2 hours in seconds
        print("Next claim in:")
        while countdown_seconds > 0:
            countdown = str(timedelta(seconds=countdown_seconds))
            print(f"\r{countdown}", end="")
            time.sleep(1)
            countdown_seconds -= 1
        print("\n")

# Example usage:
if __name__ == "__main__":
    data_file = 'data.txt'
    process_accounts(data_file)
