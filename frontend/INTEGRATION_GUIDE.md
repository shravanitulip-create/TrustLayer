# Integration Guide for Frontend with Python Smart Contract

## 1. Integration with Python Smart Contract

### Step 1: Install Required Packages
To begin integrating the frontend with the Python smart contract, ensure that the necessary packages are installed. You can use the following command:
```bash
npm install <required-packages>
```

### Step 2: Connect to the Smart Contract
Use the ABI and the contract address to connect your frontend to the Python smart contract. Add the following snippet to your code:
```javascript
const contract = new web3.eth.Contract(ABI, contractAddress);
```

### Step 3: Interacting with the Contract
To call a method from the smart contract, use the following syntax:
```javascript
contract.methods.methodName(parameters).send({ from: userAddress });
```

## 2. Updating App ID after TestNet Deployment

### Step 1: Locate Configuration Files
Find the configuration files where the App ID is specified, usually located in `frontend/config.js`.

### Step 2: Update the App ID
Once the deployment on TestNet is done, update the App ID:
```javascript
const APP_ID = 'new_app_id_here';
```

### Step 3: Deploy Changes
After making changes, don’t forget to redeploy your frontend application:
```bash
npm run build
```

## 3. Setting Up the Complete Environment

### Step 1: Clone the Repository
If you haven't already, clone the repository:
```bash
git clone https://github.com/shravanitulip-create/TrustLayer.git
```

### Step 2: Install Dependencies
Navigate to the cloned directory and install dependencies:
```bash
cd TrustLayer/frontend
npm install
```

### Step 3: Set Up Environment Variables
Create a `.env` file at the root of the frontend folder and add necessary variables:
```
REACT_APP_SMART_CONTRACT_ADDRESS=your_smart_contract_address
REACT_APP_APP_ID=your_app_id
```

### Step 4: Start the Development Server
Finally, start the development server:
```bash
npm start
```