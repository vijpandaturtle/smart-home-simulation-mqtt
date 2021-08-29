## IOT Smart Home Project 

The aim of this project is to simulate a basic IOT smart home environment using a number of Light and ACDevices an Edge Server and an MQTT broker using software packages and scripts. 

**Requirements Discussion**
1. Rooms : Kitchen, BR1, BR2, Living 
2. Device type : LightDevice, ACDevice 
3. Light Device State : on/off and low/medium/high 
4. AC Device State : on/off and temperature control (18C - 32C)
5. Edge Server Capabilities : Device Registration, Send command to device, GET Device Status 
6. Main Class in Edge Server to show capabilities 

**Demonstration**
1. 3 Light Devices & 2 AC Device 
2. Various Operations 

**Design Decisions** 
1. Single Topic vs Multilevel Topic

**Topic Design**
1. Main Topic : Devices/*
2. Issuing Registration Request : Devices/device_id/REG
3. Registration Confirmation : Devices/device_id/CONFREG
4. Issuing request for device status : Devices/device_id/GETSTATUS  
5. Device posting status : Devices/device_id/STATUS
6. Issuing request for setting device status : Devices/device_id/SETSTATUS
7. Issuing request for device parameters : Devices/device_id/GETCOMMAND
8. Device posting device parameters : Devices/device_id/COMMAND
8. Issuing request for setting device parameters : Devices/device_id/SETCOMMAND
