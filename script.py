import requests
import argparse

def check_headers(url):
    try:
        r = requests.get(url)
        headers = r.headers

        print("Security Headers for ",url)
        print(f"Strict-Transport-Security: {headers.get('Strict-Transport-Security', 'Not Set')}")
        print(f"X-Content-Type-Options: {headers.get('X-Content-Type-Options', 'Not Set')}")
        print(f"X-Frame-Options: {headers.get('X-Frame-Options', 'Not Set')}")
        print(f"X-XSS-Protection: {headers.get('X-XSS-Protection', 'Not Set')}")
        print(f"Content-Security-Policy: {headers.get('Content-Security-Policy', 'Not Set')}")
        print(f"Referrer-Policy: {headers.get('Referrer-Policy', 'Not Set')}")
        print(f"Feature-Policy: {headers.get('Feature-Policy', 'Not Set')}")
        print(f"Expect-CT: {headers.get('Expect-CT', 'Not Set')}")
        print(f"Public-Key-Pins: {headers.get('Public-Key-Pins', 'Not Set')}")
        print(f"Public-Key-Pins: {headers.get('Public-Key-Pins', 'Not Set')}")
        print(f"Permissions-Policy: {headers.get('Permissions-Policy', 'Not Set')}")
        print(f"Cross-Origin-Embedder-Policy: {headers.get('Cross-Origin-Embedder-Policy', 'Not Set')}")
        print(f"Cross-Origin-Opener-Policy: {headers.get('Cross-Origin-Opener-Policy', 'Not Set')}")
        print(f"Cross-Origin-Resource-Policy: {headers.get('Cross-Origin-Resource-Policy', 'Not Set')}")
        print(f"Cross-Origin-Script-Access: {headers.get('Cross-Origin-Script-Access', 'Not Set')}")
        print(f"Cache-Control (no-store): {headers.get('Cache-Control', 'Not Set')}")
        print(f"Cache-Control (no-cache): {headers.get('Cache-Control', 'Not Set')}")
        print(f"Cache-Control (private): {headers.get('Cache-Control', 'Not Set')}")
        print(f"Cache-Control (public): {headers.get('Cache-Control', 'Not Set')}")
        print(f"Cache-Control (max-age): {headers.get('Cache-Control', 'Not Set')}")

    except r.RequestException as e:
        print(e)


parser = argparse.ArgumentParser()
parser.add_argument('--url','-u',required=True)
args = parser.parse_args()
check_headers(args.url)

