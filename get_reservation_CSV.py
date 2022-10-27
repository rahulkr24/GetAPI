import csv
from api_utils import *


class Create(object):
    def __init__(self):
        self.new_token = ""

    def get_generate_token(self, token_num):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'generate_new_token/?pass_phase=' + str(token_num), token=self.new_token)
        self.new_token = response["access_token"]
        print("generated token:", self.new_token)
        return True

    def get_reservation_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/', token=self.new_token)

        complete = csv.writer(open("Pickup_completed.csv", 'w'), lineterminator='\n')
        pickup_p = csv.writer(open("Pickup_Pending.csv", 'w'), lineterminator='\n')
        drop_p = csv.writer(open("Drop_Pending.csv", 'w'), lineterminator='\n')
        drop_c = csv.writer(open("Drop_Cancelled.csv", 'w'), lineterminator='\n')
        rto_p = csv.writer(open("RTO_Pending.csv", 'w'), lineterminator='\n')
        complete.writerow(response["records"][0])
        pickup_p.writerow(response["records"][0])
        drop_p.writerow(response["records"][0])
        drop_c.writerow(response["records"][0])
        rto_p.writerow(response["records"][0])

        press = int(input("Enter 1 ---> PickupCompleted\nEnter 2 ---> PickupPending\nEnter 3 ---> DropCancelled\nEnter 4 ---> DropPending\nEnter 5 ---> RTO_Pending \n"))
        match press:
            case 1:
                for line in response["records"]:
                    if line["reservation_status"] == "PickupCompleted":
                        complete.writerow(line.values())

            case 2:
                for line in response["records"]:
                    if line["reservation_status"] == "PickupPending":
                        pickup_p.writerow(line.values())

            case 3:
                for line in response["records"]:
                    if line["reservation_status"] == "DropCancelled":
                        drop_c.writerow(line.values())

            case 4:
                for line in response["records"]:
                    if line["reservation_status"] == "DropPending":
                        drop_p.writerow(line.values())

            case 5:
                for line in response["records"]:
                    if line["reservation_status"] == "RTOPending":
                        rto_p.writerow(line.values())
            case _:
                print("Wrong Input")

    def get_reservation_by_id(self):
        pod_id = input("Enter Pod ID for Reservation Details\n")
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/?active_only=true&pod_id=' + str(pod_id), token=self.new_token)
        rto_filed = ["id", "pod_id", "reservation_status", "door_number", "rto_otp"]
        field = ["id", "pod_id", "reservation_status", "door_number", "drop_otp", "pickup_otp"]
        cs = csv.writer(open("get_reservation_id.csv", 'w'))
        cs.writerow(rto_filed)
        for items in response["records"]:
            if items["reservation_status"] == "RTOPending":
                detail = (items["id"], items["pod_id"], items["reservation_status"], items["door_number"], items["rto_otp"])
                cs.writerow(detail)

        cs.writerow(field)
        for items in response["records"]:
            if items["reservation_status"] == "DropPending":
                detail = (items["id"], items["pod_id"], items["reservation_status"], items["door_number"], items["drop_otp"], items["pickup_otp"])
                cs.writerow(detail)

        cs.writerow(field)
        for items in response["records"]:
            if items["reservation_status"] == "PickupPending":
                detail = (items["id"], items["reservation_status"], items["pod_id"], items["door_number"], items["pickup_otp"])
                cs.writerow(detail)

        print("Successfully data in inserted in ", 'get_reservation_id.csv')


a = Create()
a.get_generate_token("765432")
a.get_reservation_detail()
a.get_reservation_by_id()
