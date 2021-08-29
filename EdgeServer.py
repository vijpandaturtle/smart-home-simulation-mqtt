import json
import time
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25  

class Edge_Server:
    
    def __init__(self, instance_name):        
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._registered_list = []

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        print(f'Connected Edge Server "{self._instance_id}" with result code={str(result_code)}')
        self.client.subscribe("Devices/#")
        
    # method to process the received messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        print(f'{msg.topic} {msg.qos} {msg.payload}')
        if msg.topic.find("/REG") != -1:
            msg_json = json.loads(msg.payload)
            device_id = msg_json["device_id"]
            self.client.publish(f"Devices/{device_id}/CONFREG", f"Device {device_id} successfully registered")
            self._registered_list.append(msg.payload)

        if msg.topic.find("/STATS") != -1:
            msg_json = json.loads(msg.payload)
            device_id = msg_json["device_id"]
            room_type = msg_json["room_type"]
            switch_status = msg_json["switch_status"]
            print(f"Status of device {device_id} is {switch_status}")

        if msg.topic.find("/COMMANDS") != -1:
            msg_json = json.loads(msg.payload)
            device_id = msg_json["device_id"]
            room_type = msg_json["room_type"]
            command_status = msg_json["command_status"]
            print(f"Status of device {device_id} is {command_status}")
    
    
    # Filtering the publish topics based on the diiferent type of request recieved. 
    def _filter_topics(self, publish_topic, subtopic):
        pass

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list
        
    # Getting the status for the connected devices
    def get_status(self, device_ids):
        for device_id in device_ids:
            self.client.publish(f"Devices/{device_id}/GETSTAT", f"Requesting device status of {device_id}")

    # Controlling and performing the operations on the devices
    # based on the request received
    def set_status(self, device_id, switch_state, command_type):
        if command_type == "SWITCH" :         
            set_status_msg = json.dumps({
                "device_id" : device_id,
                "switch_status" : switch_state
            })
            self.client.publish(f"Devices/{device_id}/SETSTAT", set_status_msg)
        if command_type == "COMMAND":
            set_status_msg = json.dumps({
                "device_id" : device_id,
                "command_status" : switch_state
            })
            self.client.publish(f"Devices/{device_id}/SETCOMMAND", set_status_msg)
