from api_utils import *
import csv


class Main(object):
    def __init__(self):
        self.new_token = ""
        self.pod_id = 0
        self.pod_location_name = ""

    def get_generate_token(self, token_num):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'generate_new_token/?pass_phase=' + str(token_num), token=self.new_token)
        self.new_token = response["access_token"]
        print("generated token:", self.new_token)
        return True

    def get_pod_detail_by_id(self, enter_id=None, pod_id=None):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'pods/' + str(enter_id or self.pod_id))
        if response["success"] is True:
            for items in response["records"]:
                self.pod_location_name = items["location_name"]
                self.pod_id = items["id"]
        else:
            print("Test Failed :", response)
        return True

    def get_doors_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'doors/', token=self.new_token)
        field = ["id", "status", "door_number", "door_health", "door_status", "door_availability", "pod_id -->location_name"]
        field2 = ["pod_id", "door_status", "door_availability"]
        jammed = csv.writer(open("Jammed_door.csv", 'w'))
        press = int(input("Enter 1 ---> Jammed Door -----Status--->> Inuse\nEnter 2  ---> Jammed Door -----Status--->> Free\nEnter 3  ---> Jammed Door -----Pod Id---->\n"))
        match press:
            case 1:
                jammed.writerow(field)
                for i in response["records"]:
                    if i["door_status"] == "JAMMED":
                        self.pod_id = i["pod_id"]
                        a.get_pod_detail_by_id(self.pod_id)
                        if i["door_availability"] == "Inuse":
                            pod_id = i["pod_id"]
                            data = (i["id"], i["status"], i["door_number"], i["door_health"], i["door_status"], i["door_availability"], i["pod_id"] + '  ' + self.pod_location_name)
                            jammed.writerow(data)
            case 2:
                jammed.writerow(field)
                for i in response["records"]:
                    if i["door_status"] == "JAMMED":
                        self.pod_id = i["pod_id"]
                        a.get_pod_detail_by_id(self.pod_id)
                        if i["door_availability"] == "Free":
                            data = (i["id"], i["status"], i["door_number"], i["door_health"], i["door_status"], i["door_availability"], i["pod_id"] + '  ' + self.pod_location_name)
                            jammed.writerow(data)

            case 3:
                jammed.writerow(field2)
                for i in response["records"]:
                    if i["door_status"] == "JAMMED":
                        pod_id = i["pod_id"]
                        data = (i["pod_id"], i["door_status"], i["door_availability"])
                        jammed.writerow(data)

            case _:
                print("Wrong input")


a = Main()
a.get_generate_token("765432")
a.get_doors_detail()
