import phonenumbers
from phonenumbers import geocoder, carrier

def track_phone_number(number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number)

        # Get the country/region information
        region = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier information
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Print the results
        print(f"Phone Number: {number}")
        print(f"Region: {region}")
        print(f"Carrier: {service_provider}")

    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example: Enter a phone number in international format (+CountryCodeNumber)
    phone_number = input("Enter a phone number (with country code, e.g., +1234567890): ")
    track_phone_number(phone_number)
