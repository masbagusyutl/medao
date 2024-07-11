import requests
import time
from datetime import datetime, timedelta

# Function to read Telegram-Init-Data from data.txt
def read_telegram_init_data(file_path):
    with open(file_path, 'r') as file:
        telegram_init_data = [line.strip() for line in file.readlines() if line.strip()]
    return telegram_init_data

# Function to claim using Telegram-Init-Data
def claim_rewards(telegram_init_data):
    url = 'https://zavod-api.mdaowallet.com/user/claim'
    headers = {
        'Telegram-Init-Data': telegram_init_data
    }
    response = requests.post(url, headers=headers)
    return response.status_code

# Function to display countdown
def display_countdown(seconds):
    while seconds > 0:
        countdown = str(timedelta(seconds=seconds))
        print(f"\rNext claim in: {countdown}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n")

# Function to process accounts and claim rewards
def process_accounts(file_path):
    telegram_init_data_list = read_telegram_init_data(file_path)
    total_accounts = len(telegram_init_data_list)
    print(f"Total accounts in data.txt: {total_accounts}")
    
    for idx, telegram_init_data in enumerate(telegram_init_data_list, start=1):
        print(f"Processing account {idx} out of {total_accounts}")
        print("Claiming rewards...")
        status_code = claim_rewards(telegram_init_data)
        print(f"Claim status: {status_code}")
        
        # Wait for 3 seconds before processing the next account
        if idx < total_accounts:
            print(f"Waiting for 3 seconds before processing the next account...")
            time.sleep(3)
    
    # Countdown for next claim in 2 hours after processing all accounts
    countdown_seconds = 2 * 60 * 60  # 2 hours in seconds
    print("Next claim countdown starts now:")
    display_countdown(countdown_seconds)

# Example usage:
if __name__ == "__main__":
    data_file = 'data.txt'
    
    while True:
        process_accounts(data_file)
        print("Restarting process after 2 hours...")
