import re
from unittest import result
from django.shortcuts import render
from .models import Tickets
#ticket0s.objects.all(0)
# Tickets.objects.filter(passenger_name = ).only:
# Tickets.objects.exclude()

'''TicketFlights
Seats
Flights
Bookings
BoardingPasses
AirportsData
AircraftsData
Tickets'''

'''Select passenger_name, contact_data,
departure_airport, arrival_airport, da.airport_name, aa.airport_name
from
tickets join ticket_flights on tickets.ticket_no=ticket_flights.ticket_no
join flights on ticket_flights.flight_id=flights.flight_id
join airports_data da on flights.departure_airport=da.airport_code
join airports_data aa on flights.arrival_airport=aa.airport_code
WHERE book_ref like 'D97558';'''
# test = Tickets.objects.prefetch_related().filter(book_ref = 'D97558'))
# test.values('book_ref', 'ticketflights__flight__departure_airport__airport_name', 'ticketflights__flight__arrival_airport').filter(book_ref = 'D97558')

def source(requests):
    return render(requests, 'index.html')

def person(requests):
    print(requests.GET)
    tmp = Tickets.objects.prefetch_related().filter(book_ref = requests.GET['name'])
    lst = tmp.values('book_ref','passenger_name', 'ticketflights__flight__departure_airport__airport_name', 'ticketflights__flight__arrival_airport__airport_name')
    for item in lst:
        book_ref = item['book_ref']
        pass_name = item['passenger_name']
        da_airname = item['ticketflights__flight__departure_airport__airport_name']
        aa_airname = item['ticketflights__flight__arrival_airport__airport_name']
        resoult = {
            'book_ref': book_ref,
            'pass_name': pass_name,
            'da_airname': da_airname,
            'aa_airname': aa_airname
        }
    print(resoult)
    return render(requests, 'test.html', {"resoult": resoult})



''' for item in lst:
        book_ref = item[0]
        pass_name = item[1]
        da_airname = item[2]
        aa_airname = item[3]
        resoult = {
            'book_ref': book_ref,
            'pass_name': pass_name,
            'da_air' : da_airname,
            'aa_air' : aa_airname
        }'''
    
