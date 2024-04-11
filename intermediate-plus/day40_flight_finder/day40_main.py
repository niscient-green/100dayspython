# Check for cheap flights that cost less than the threshold, pull from GSheet
import data_manager
import flight_data
import flight_search
import notification_manager

# Set globals, constants -----------------------------------------------------------------------------------------------
FROM_CODE = 'BOS'


# Main program ---------------------------------------------------------------------------------------------------------
def found_flight(flights, max_stops):
    # Structure data, get lowest flight
    lowest_flight = flight_data.FlightData(flights=flights, max_stops=max_stops)
    row['lowestPrice'] = lowest_flight.price
    gsheet_prices.update_prices(row)
    # Send SMS
    notification = notification_manager.NotificationManager(lowest_flight=lowest_flight, max_stops=max_stops,
                                                            via_city=lowest_flight.via_city)
    notification.send_sms()
    notification.send_emails(users)


# Create new class objects to handle flights, data
gsheet_prices = data_manager.DataManager()
flight_thresholds = gsheet_prices.get_prices()
flight_search = flight_search.FlightSearch()

# Get user data
gsheet_users = data_manager.DataManager()
users = gsheet_users.get_users()

# Check for missing IATA codes, update if needed
for row in flight_thresholds:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata(row['city'])
        gsheet_prices.update_prices(row)

# Pull flights for each destination city
for row in flight_thresholds:
    flights = flight_search.find_flights(from_code=FROM_CODE, to_code=row['iataCode'],
                                         lowest_price=row['lowestPrice'] - 1)
    # If a flight was not found lower than current lowestPrice, list will be empty
    if flights:
        found_flight(flights=flights, max_stops=0)
    else:
        # If flight was not found, try finding one with 1 stopover
        flights = flight_search.find_flights(from_code=FROM_CODE, to_code=row['iataCode'],
                                             lowest_price=row['lowestPrice'] - 1, max_stops=1)
        if flights:
            found_flight(flights=flights, max_stops=1)
