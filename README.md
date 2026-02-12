# TrustLayer - Decentralized Campus Governance dApp

## Overview
TrustLayer is a decentralized application on Algorand TestNet for campus governance. It allows:
- Wallet-based identity (one-wallet-one-vote)
- Immutable vote storage on-chain
- Proposal creation
- Simple rule-based anomaly detection for suspicious votes

## Project Status
- Python smart contract written (`contracts/trustcontract.py`)
- TEAL files generated (`approval.teal` and `clear.teal`)
- deploy.py loads TEAL and generates demo accounts
- Dependencies installed (`py-algorand-sdk`)
- Ready for frontend (UI) and AI integration
- MVP focuses on voting and fraud detection logic; funding release & advanced ML excluded for feasibility

## Tech Stack
- Blockchain: Algorand TestNet, PyTeal/TEAL, Python SDK
- Frontend: HTML/JS (or React) for wallet connect and proposal display
- Backend / AI: Python for simple anomaly detection
- MVP Scope: wallet connect, proposal creation, voting, anomaly detection

## Setup
1. Install Python 3.x
2. Install dependencies:
