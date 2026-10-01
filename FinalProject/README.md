# Hotel Booking System
- **Status** - In Progress - MVP v1, see completed and Known issues for whats left

Manages Life cycles of Hotel Booking System


## Problem Statement
Build Booking system for Hotel Management which handles create Booking, manage Booking (update and cancellation), view booking infomation. 

## Object / Responsibilities
- **Hotel** - Represents Hotel consists of one or multiple rooms object

- **Room** - Represents the Room consists of Guest object and Booking related information

- **Guest** - Represent Person to whom the Room is actually booked

- **Booking** - Represent the combined data related eachother of all standalone data

## Booking Statuses
- ```RESERVED```
- ```CONFIRMED```
- ```UPDATED```
- ```CANCELLED```

## Minimum Viable Version (v1)
- Create Class for Hotel, Room, Guest,Booking objects
- Create Booking feature
- Business rule implementation for conflict booking
- Manage Booking (view, update and Cancellation)
- Proper object state tracking for all the Rooms of Hotel
- All objects interacts with each other
- Summary of all booked rooms


## Completed
- Created Class for Hotel, Room, Guest,Booking objects
- Created Booking features like create booking with validations
    - Business rule implementation for conflict booking
        - ````Create Booking request with same dates or conflicting dates of booked````
- Manage Booking (view, update and Cancellation)
- Proper object state tracking for all the Rooms of Hotel
- All objects interacts with each other
- Summary of all booked rooms

## How to Run
- Navigate to the project root (`FinalProject/`)
- Run ```python main.py```


## Known Issues
- Statistics on all room occupancy
- Cleanup the way simulating Hotel Booking system

## Design Notes
- Objects for depicting data 
    - **Hotel, Room, Guest, Booking**
- Services to hold collection of data and handle actions
    - Booking Service 
        - has **List of booking** since no natural parent for holding all bookings
        - has methods **create booking, retrieve booking, update booking**
    - Room Service 
        - has methods **create room and update room**
    - Hotel Service **create hotel and update hotel**
    - Hotel Booking **Simulating hotel booking flow interation between objects**
    - Kept collection of Room objects (rooms) as set intead of dictinoary to keep it simple for updating
    - Kept collection of Booking objects (bookings) as List since same room and guest can have multiple bookings for different dates