import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery

# Set up Google Drive API scopes and credentials
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
CLIENT_SECRETS_FILE = "client_secrets.json"  # Path to your downloaded OAuth 2.0 credentials JSON file

# Function to authenticate user and get credentials
def authenticate_google_drive():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    return credentials

def main():
    st.title("Google Drive Authentication with Level-pack")

    # Add a "Login" button
    if st.button("Login"):
        # Authenticate user and get credentials
        credentials = authenticate_google_drive()

        # Create a Google Drive API client
        drive_service = googleapiclient.discovery.build("drive", "v3", credentials=credentials)

        st.write("Authenticated successfully!")

        # You can now use the 'drive_service' to interact with the authenticated user's Google Drive

if __name__ == "__main__":
    main()
