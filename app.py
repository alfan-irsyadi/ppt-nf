import streamlit as st
import requests

st.title("File Downloader")

url = st.text_input("Enter the URL of the file you want to download:")

if st.button("Download"):
    if url:
        try:
            headers = {
                'authority': 'sip-files.sgp1.digitaloceanspaces.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://emodul.bimbelnurulfikri.id/',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers, stream=True)
            filename = response.headers.get('Content-Disposition').split('filename=')[1].strip('"\'')

            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            st.success(f"File downloaded as: {filename}")

            # Add a download button for the downloaded file
            with open(filename, "rb") as file:
                btn = st.download_button(
                        label="Download file",
                        data=file,
                        file_name=filename,
                        mime="application/octet-stream"
                    )

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a URL.")