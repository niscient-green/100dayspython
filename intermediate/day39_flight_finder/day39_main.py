# Program Requirements
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
#
# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
#
# If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
#
# The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.
#
# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.


# Check for cheap flights that cost less than the threshold, pull from GSheet
import data_manager
import flight_data
import flight_search
import notification_manager

# Set globals, constants -----------------------------------------------------------------------------------------------
FROM_CODE = 'BOS'

# Main program ---------------------------------------------------------------------------------------------------------
# Create new class objects to handle flights, data
gsheet_data = data_manager.DataManager()
flight_thresholds = gsheet_data.get_gsheet()
flight_search = flight_search.FlightSearch()

# Check for missing IATA codes, update if needed
for row in flight_thresholds:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata(row['city'])
        gsheet_data.update_gsheet(row)

# Pull flights for each destination city
for row in flight_thresholds:
    flights = flight_search.find_flights(FROM_CODE, row['iataCode'], row['lowestPrice'] - 1)
    # If a flight was not found lower than current lowestPrice, list will be empty
    if flights:
        # Structure data, get lowest flight
        lowest_flight = flight_data.FlightData(flights)
        row['lowestPrice'] = lowest_flight.price
        gsheet_data.update_gsheet(row)
        # Send SMS
        notification = notification_manager.NotificationManager(lowest_flight)
