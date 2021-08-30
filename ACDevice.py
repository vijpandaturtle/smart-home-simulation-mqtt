import json
import paho.mqtt.client as mqtt


HOST = "localhost"
PORT = 1883
    
class AC_Device():
    
    _MIN_TEMP = 18  
    _MAX_TEMP = 32  

    def __init__(self, device_id, room):
        self._device_id = device_id
        self._room_type = room
        self._temperature = 22
        self._device_type = "ac"
        self._device_registration_flag = False
        self.client = mqtt.Client(self._device_id)  
        self.client.on_connect = self._on_connect  
        self.client.on_message = self._on_message  
        self.client.on_disconnect = self._on_disconnect  
        self.client.connect(HOST, PORT, keepalive=60)  
        self.client.loop_start()  
        self._register_device(self._device_id, self._room_type, self._device_type)
        self._switch_status = "OFF"

    # calling registration method to register the device
    def _register_device(self, device_id, room_type, device_type):
        reg_msg = json.dumps({
            "device_id" : device_id,
            "device_type" : self._device_type,
            "room_type" : room_type,
            "device_type" : device_type
        })
        self.client.publish(f"devices/{room_type}/{device_type}/{device_id}/REG", reg_msg)
        
    # Connect method to subscribe to various topics. 
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe(f"devices/+/{self._device_type}/{self._device_id}/#")

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg): 
        print(f'{msg.topic} {msg.qos} {msg.payload}')
        if msg.topic.find("/GETSTAT") != -1:
            status_msg = json.dumps({
            "device_id" : self._device_id,
            "device_type" : self._device_type,
            "room_type" : self._room_type,
            "switch_status" : self._get_switch_status()
            })
            self.client.publish(f"devices/{self._room_type}/{self._device_type}/{self._device_id}/STAT", status_msg)
        if msg.topic.find("/GETCOMMAND") != -1:
            cmd_msg = json.dumps({
            "device_id" : self._device_id,
            "device_type" : self._device_type,
            "room_type" : self._room_type,
            "command_status" : self._get_temperature()
            })
            self.client.publish(f"devices/{self._room_type}/{self._device_type}/{self._device_id}/COMMAND", cmd_msg)    
        if msg.topic.find("/SETSTAT") != -1: 
            msg_json = json.loads(msg.payload)
            switch_state = msg_json["switch_status"]
            status_msg = json.dumps({
            "device_id" : self._device_id,
            "device_type" : self._device_type,
            "room_type" : self._room_type,
            "switch_status" : self._set_switch_status(switch_state)
            })
            self.client.publish(f"devices/{self._room_type}/{self._device_type}/{self._device_id}/STAT", status_msg)
        if msg.topic.find("/SETCOMMAND") != -1: 
            msg_json = json.loads(msg.payload)
            command_state = msg_json["command_status"]
            cmd_msg = json.dumps({
            "device_id" : self._device_id,
            "device_type" : self._device_type,
            "room_type" : self._room_type,
            "command_status" : self._set_temperature(command_state)
            })
            self.client.publish(f"devices/{self._room_type}/{self._device_type}/{self._device_id}/COMMAND", cmd_msg)
            
    # Getting the current switch status of devices 
    def _get_switch_status(self):
        return self._switch_status

    # Setting the the switch of devices
    def _set_switch_status(self, switch_state):
        self._switch_status = switch_state
        return self._switch_status

    # Getting the temperature for the devices
    def _get_temperature(self):
        return self._temperature

    # Setting up the temperature of the devices
    def _set_temperature(self, temperature):
        if self._MIN_TEMP < int(temperature) < self._MAX_TEMP: 
            self._temperature = temperature
        else:
            print("Please enter a temperature value between 18 and 32")
        return self._temperature

    # Performing disconnect operation
    def _on_disconnect(self, client, userdata, result_code):
        self.client.loop_stop()
        print(f'Disconnected {self._device_type}_MQTT_instance "{self._device_id}" with result code={str(result_code)}')
        
