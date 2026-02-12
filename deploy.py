from algosdk.v2client import algod
from algosdk import account, encoding
from algosdk.transaction import ApplicationNoOpTxn, StateSchema, OnComplete
import base64

# Connect to local Algorand node (Sandbox or TestNet later)
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

algod_client = algod.AlgodClient(algod_token, algod_address)

# Generate temporary account (for demo)
private_key, address = account.generate_account()

print("Generated Account Address:", address)

# Load TEAL files
with open("approval.teal", "r") as f:
    approval_program = f.read()

with open("clear.teal", "r") as f:
    clear_program = f.read()

print("Smart Contract Ready for Deployment.")
