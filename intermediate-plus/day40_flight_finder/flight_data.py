class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flights: list, max_stops: int):
        self.flights = flights
        self.lowest_flight = {}
        self.lowest_price()
        self.price = self.lowest_flight['price']
        self.stopovers = max_stops
        if self.stopovers == 0:
            # Set attributes in the 0 stopovers case
            self.from_city = self.lowest_flight['cityFrom']
            self.to_city = self.lowest_flight['cityTo']
            self.depart = str(self.lowest_flight['local_departure']).split('T')[0]
            self.nights = self.lowest_flight['nightsInDest']
            self.via_city = ''
        else:
            # Set attributes in the multiple stopovers case
            self.from_city = self.lowest_flight['route'][0]['cityFrom']
            self.to_city = self.lowest_flight['route'][0]['cityTo']
            self.depart = str(self.lowest_flight['route'][0]['local_departure']).split('T')[0]
            self.nights = self.lowest_flight['route'][0]['nightsInDest']
            self.via_city = self.lowest_flight['route'][0]['via_city']

    def lowest_price(self):
        # Find the lowest price flight
        self.lowest_flight = self.flights[0]
        for flight in self.flights:
            if flight['price'] < self.lowest_flight['price']:
                self.lowest_flight = flight
