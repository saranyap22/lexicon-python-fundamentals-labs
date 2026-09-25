# Hotel Booking System
Manages Life cycles of Hotel Booking


## Problem Statement
Build Booking system for Hotel Management which handles create Booking, manage Booking (update and cancellation), view booking infomation. 

## Object / Responsibilities
- **Holtel** - Represents Hotel consists of one or multiple rooms object

- **Room** - Represents the Room consists of Guest object and Booking related information

- **Guest** - Represent Person to whom the Room is actually booked

- **Gym** - Represent Gym service information

- **Meal** - Represent Meal related service information

- **Booking** - Represent the combined data related eachother of all standalone data

## Booking Statuses
- ```NEW```
- ```RESERVED```
- ```BOOKED```
- ```CANCELLED```

## Minimum Viable Version (v1)
- Create Class for Hotel, Room, Guest,Booking objects
- Create Booking feature
- Business rule implementation for conflict booking
- Manage Booking (view, update and Cancellation)
- Proper object state tracking for all the Rooms of Hotel
- All objects interacts with each other
- Summary of all booked rooms
- Statistics on all room occupancy