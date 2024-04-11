class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flights: list):
        self.flights = flights
        self.lowest_flight = {}
        self.lowest_price()
        self.price = self.lowest_flight['price']
        self.from_city = self.lowest_flight['cityFrom']
        self.to_city = self.lowest_flight['cityTo']
        self.depart = str(self.lowest_flight['local_departure']).split('T')[0]
        self.nights = self.lowest_flight['nightsInDest']

    def lowest_price(self):
        # Find the lowest price flight
        self.lowest_flight = self.flights[0]
        for flight in self.flights:
            if flight['price'] < self.lowest_flight['price']:
                self.lowest_flight = flight
