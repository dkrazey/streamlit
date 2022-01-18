import requests, json
import streamlit as st
from web3 import Web3
import pandas as pd

url = "https://api.opensea.io/api/v1/events"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "a156e53acdfc46e09f5ba654af640f50"
}

r = requests.request("GET", url, headers=headers)

st.sidebar.header("Endpoints")
endpoint_choices = ['Assets', 'Events', 'Rarity']
endpoint = st.sidebar.selectbox("Choose an Endpoint", endpoint_choices)

st.title(f"OpenSea API Explorer - {endpoint}")

if endpoint == 'Events':
    collection = st.sidebar.text_input("Collection")
    asset_contract_address = st.sidebar.text_input("Contract Address")
    token_id = st.sidebar.text_input("Token ID")
    event_type = st.sidebar.selectbox("Event Type", ['offer_entered', 'cancelled', 'bid_withdrawn', 'transfer', 'approve', 'successful'])
    params = {}
    if collection:
        params['collection_slug'] = collection
    if asset_contract_address:
        params['asset_contract_address'] = asset_contract_address
    if token_id:
        params['token_id'] = token_id
    if event_type:
        params['event_type'] = event_type
   

print(r.json)


events = r.json()
event_list = []
for event in events['asset_events']:
        if event_type == 'successful':
            if event['bid_amount']:
                bid_amount = Web3.fromWei(int(event['bid_amount']), 'ether')
            if event['from_account']['user']:
                bidder = event['from_account']['user']['username']
            else:
                bidder = event['from_account']['address']

            event_list.append([event['created_date'], bidder, float(bid_amount), event['asset']['collection']['name'], event['asset']['token_id']])

df = pd.DataFrame(event_list, columns=['time', 'bidder', 'bid_amount', 'collection', 'token_id'])



st.write(df)
st.write(events)