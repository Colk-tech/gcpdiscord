from src.main_client import MainClient
from src.gcp_authenticate import gcp_authenticate


if __name__ == "__main__":
    gcp_authenticate()
    MainClient().launch()
