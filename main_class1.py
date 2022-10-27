from api_utils import *


class Create(object):
    def __init__(self):
        self.pod_id = 0
        self.pod_location_id = 0
        self.post_pod_id = 0
        self.enter_id = 0
        self.pod_location_name = ""
        self.pod_status = ""
        self.location_record_id = 0
        self.users_record_id = 0
        self.unique_id = ""
        self.users_user_id = 0
        self.users_location_id = 0
        self.location_record_id = 0
        self.door_record_id = 0
        self.door_list = []
        self.reservation_id = 0
        self.reserve_id = 0
        self.id_list = []
        self.reserve_id_list = []
        self.ph_number = 0
        self.reservation_otp_type = 0
        self.user_phone = "7352334273"
        self.otp_text = "334273"
        self.validate_id = 0
        self.validate_user_type = ""
        self.validate_username = ""
        self.spot_name = ""
        self.spots_record_id = 0
        self.spot_location_id = 0
        self.filename_id = ""
        self.new_token = ""
        self.number_of_doors = 0

    def get_pod_details(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'pods/', token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                print("------------------get_pods_detail---------------------------")
                self.pod_location_id = items["location_id"]
                pod_location_name = items["location_name"]
                pod_status = items["status"]
                self.pod_id = items["id"]
                print("Pod id :", self.pod_id)
                print("Status :", pod_status)
                print("Location_name :", pod_location_name)
                print("Location_id :", self.pod_location_id)
                break
        else:
            print("Test Failed :", response)
        return True

    def get_pod_detail_by_id(self, enter_id=None, pod_id=None):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'pods/' + str(enter_id or self.pod_id))
        if response["success"] is True:
            for items in response["records"]:
                print("-------------------get_pod_detail_by_id-----------------------")
                self.pod_location_id = items["location_id"]
                self.pod_location_name = items["location_name"]
                self.pod_id = items["id"]
                print("Pod id :", self.pod_id)
                print("Location_id :", self.pod_location_id)
                print("Location_name :", self.pod_location_name)

        else:
            print("Test Failed :", response)
        return True

    def get_pod_doors_by_id(self):

        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'pods/doors/' + str(self.pod_id), token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                print("-------------------get_pod_doors_by_id------------------------")
                print(" record id : ", items["id"])
                print("door number : ", items["door_number"])
                print("door status : ", items["door_status"])
                print("door_availability : ", items["door_availability"])
                break
            else:
                print("Test Failed :", response)
        return True

    def get_pod_location_by_id(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'pods/location/spots?location_id=' + str(self.pod_location_id), token=self.new_token)
        if response["success"] is True:
            for item in response["records"]:
                print("-----------------------get_pod_location_by_id---------------------------")
                print(item)
                break
        else:
            print("Test Failed :", response)

        return True

    def post_pod(self, p_id):
        self.post_pod_id = p_id
        self.get_pod_detail_by_id()
        pod_data = {"id": p_id, "pod_numtotaldoors": 2, "pod_name": "QP RK NAME", "location_id": self.location_record_id}
        response = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'pods/', data=json.dumps(pod_data), token=self.new_token)
        print("-------------------------post pod details----------------------")
        if response["success"] is True:
            for item in response["records"]:
                self.pod_id = item["id"]
                self.number_of_doors = item["pod_numtotaldoors"]
                self.pod_location_id = item["location_id"]
                print("Created Pod id : ", self.pod_id)
                print("Location_id :", self.pod_location_id)
                print("No of door created :", self.number_of_doors)

        else:
            print("Test Failed :", response)
        return True

    def patch_pod(self, param=None):
        todo = {"pod_name": "QIKPOD TEST NAME"}
        response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'pods/' + str(self.pod_id) + '?verbose=true', data=json.dumps(todo), token=self.new_token)
        if response["success"] is True:
            print("----------------------patch pod data-----------------------------")
            for items in response["records"]:
                self.pod_location_id = items["location_id"]
                pod_status = items["status"]
                pod_id = items["id"]
                state = items["pod_state"]
                pod_name = items["pod_name"]
                print("Pod id :", pod_id)
                print("Pod name :", pod_name)
                print("Status :", pod_status)
                print("pod state :", state)
                print("Location_id :", self.pod_location_id)
        else:
            print("Test Failed :", response)

        return True

    def delete_pod(self):
        response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'pods/' + str(self.pod_id), token=self.new_token)
        print("pods data deleted :", response)

        return True

    def get_location_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'locations/', token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                print("------------------------------get_location_detail----------------------------")
                self.location_record_id = items["id"]
                loc_name = items["location_name"]
                print("record id :", self.location_record_id)
                print("location details :", loc_name)
                break
        else:
            print("Test Failed :", response)

        return True

    def get_location_by_id(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'locations/' + str(self.location_record_id or self.pod_location_id), token=self.new_token)
        print("------------------------------get_location_by_id-------------------------------")
        if response["success"] is True:
            for items in response["records"]:
                loc_address = items["location_address"]
                self.location_record_id = items["id"]
                print("Location address :", loc_address)
                print("location id  :", self.location_record_id)
        else:
            print("Test Failed :", response)

        return True

    def get_locations_site_admin(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'locations/' + str(self.location_record_id), token=self.new_token)
        print("------------------------get_locations_site_admin-------------------------")
        if response["success"] is True:
            for items in response["records"]:
                loc_address = items["location_address"]
                self.location_record_id = items["id"]
                print("Location address :", loc_address)
                print("location id  :", self.location_record_id)
        else:
            print("Test Failed :", response)
        return True

    def post_locations(self):
        data = {"location_name": "QikPod-HW-A", "location_address": "CV Raman Nagar ", "location_pincode": "560093"}
        response = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'locations', data=json.dumps(data), token=self.new_token)
        for item in response["records"]:
            if response["success"] is True:
                print("--------------------------post_locations--------------------------------")
                self.location_record_id = item["id"]
                print("location record id :", self.location_record_id)
            else:
                print("test failed")
        return True

    def patch_location(self):
        todo = {"location_name": "RK NAME"}
        response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'locations/' + str(self.location_record_id), data=json.dumps(todo), token=self.new_token)
        if response["success"] is True:
            print("--------------------------patch_location------------------------")
            for item in response["records"]:
                location_name = item["location_name"]
                print("location_name  :", location_name)
        return True

    def delete_location(self):
        response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'locations/' + str(self.location_record_id), token=self.new_token)
        print("location deleted :", self.location_record_id, response)
        return True

    def get_users_detail(self):

        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'users/', token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                print("---------------------------------get_users_detail----------------------------")
                self.users_record_id = items["id"]
                print("record id :", self.users_record_id)
                break
        else:
            print("Test Failed :", response)
        return True

    def get_user_by_id(self):
        self.users_record_id = self.pod_location_id
        print("----------------------------get_user_by_id--------------------------")
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'users/' + str(self.users_record_id), token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                self.users_user_id = items["id"]
                u_type = items["user_type"]
                print("user_id:", self.users_user_id)
                print("User Type :", u_type)
        return True

    def get_user_location(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'users/locations/', token=self.new_token)
        if response["success"] is True:
            for items in response["records"]:
                print("---------------------------------get_users_location----------------------------")
                self.users_location_id = items["location_id"]
                self.users_user_id = items["user_id"]
                print("location id :", self.users_location_id)
                print("user id :", self.users_user_id)
                break
        else:
            print("Test Failed :", response)
        return True

    def post_user(self):
        user_data = {"user_phone": "0333010555", "user_name": "RP USER NAME", "user_type": "QPStaff", "location_id": self.pod_location_id}
        response = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'users/', data=json.dumps(user_data), token=self.new_token)
        print("----------------------post_user data-----------------------------")
        if response["success"] is True:
            for items in response["records"]:
                self.users_record_id = items["id"]
                user_name = items["user_name"]
                print("user_id :", self.users_record_id)
                print("User name :", user_name)
        else:
            print("test failed :", response)
        return True

    def patch_user(self):
        todo = {"user_name": "RP QP NAME"}
        response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'users/' + str(self.users_record_id), data=json.dumps(todo), token=self.new_token)
        print("----------------------patch user data-----------------------------")
        if response["success"] is True:
            for item in response["records"]:
                self.users_record_id = item["id"]
                user_name = item["user_name"]
                print("patch users : ", self.users_record_id)
                print("User name :", user_name)
        else:
            print("Test failed :", response)
        return True

    def delete_user(self):
        response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'users/' + str(self.users_record_id), token=self.new_token)
        print("----------------------user data deleted-----------------------------")
        print("users data deleted :", self.users_user_id, response)
        return True

    def get_doors_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'doors/?pod_id=' + str(1001552), token=self.new_token)
        print("-------------------------------get_doors_detail----------------------------")
        if response["success"] is True:
            for items in response["records"]:
                self.door_record_id = items["id"]
                door_availability = items["door_availability"]
                door_n = items["door_number"]
                print("door number", door_n)
                print("record id :", self.door_record_id)
                print("door_availability", door_availability)
                self.door_list.append(self.door_record_id)
                print("door id list :", self.door_list)
                break
        else:
            print("Test Failed :", response)

        return True

    def get_door_details_by_id(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'doors/' + str(self.door_record_id), token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("------------------------ get_door_details_by_id----------------------------------")
                self.door_record_id = items["id"]
                door_availability = items["door_availability"]
                self.pod_id = items["pod_id"]
                print("Pod id :", self.pod_id)
                print("record_id : ", self.door_record_id)
                print("door_availability :", door_availability)
                self.door_list.append(self.door_record_id)
                print("list of door :", self.door_list)
            else:
                print("Test Failed :", response)
        return True

    def post_door(self):
        door_data = {"door_size": "Auto", "door_status": "Open", "pod_id": self.post_pod_id, "door_availability": "Reserved"}
        post_door_data = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'doors/', data=json.dumps(door_data), token=self.new_token)
        for items in post_door_data["records"]:
            print("----------------------post door data-----------------------------")
            self.door_record_id = items["id"]
            door_availability = items["door_availability"]
            print("Pod id :", self.post_pod_id)
            print("record_id : ", self.door_record_id)
            print("door_availability :", door_availability)
            self.door_list.append(self.door_record_id)
            print("list of door :", self.door_list)
        return True

    def patch_door(self):
        todo = {"door_size": "Medium"}
        response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'doors/' + str(self.door_record_id), data=json.dumps(todo), token=self.new_token)
        for items in response["records"]:
            print("---------------------------patch_door-----------------------------")
            print("door size :", items["door_size"])
        return True

    def delete_door(self):
        for item in self.door_list:
            response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'doors/' + str(item), token=self.new_token)
            print("---------------------------Delete door data-----------------------------")
            print("delete_doors_data :", item, response)
        return True

    def get_reservation_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/?location_id=' + str(self.pod_location_id), token=self.new_token)
        print("------------------------get_reservation_detail---------------------------------")
        count = 0
        if response["success"] is True:
            for items in response["records"]:
                stat = items["status"]
                if stat == "active":
                    pending = items["reservation_status"]
                    drop_otp = items["drop_otp"]
                    res_id = items["id"]
                    loc_name = items["location_name"]
                    pod_name = items["pod_name"]
                    pod_id = items["pod_id"]
                    print("status :", pending)
                    print("Drop OTP :", drop_otp)
                    if pending == "PickupPending":
                        pickup = items["pickup_otp"]
                        print("pickup OTP :", pickup)
                    print("Reservation id :", res_id)
                    print("Location name :", loc_name)
                    print("Pod name :", pod_name)
                    print("Pod id :", pod_id)
                    count = count + 1
                    print("records number:", count)
                    print("----------------------------------------------------------")
                    print("----------------------------------------------------------")
                    print("----------------------------------------------------------")

        else:
            print("Test Failed :", response)

        return True

    def get_reservation_by_id(self, pod_id):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/?active_only=true&pod_id=' + str(pod_id), token=self.new_token)
        print("---------------------get_reservation_by_id------------------------")
        if response["success"] is True:
            for items in response["records"]:
                if items["reservation_status"] == "RTOPending":
                    res_id = items["id"]
                    p_id = items["pod_id"]
                    door_n = items["door_number"]
                    door_av = items["door_availability"]
                    rto_otp = items["rto_otp"]
                elif items["reservation_status"] == "DropPending":
                    res_id = items["id"]
                    p_id = items["pod_id"]
                    door_n = items["door_number"]
                    door_av = items["door_availability"]
                    drop_otp = items["drop_otp"]
                    pick_otp = items["pickup_otp"]
                elif items["reservation_status"] == "PickupPending":
                    res_id = items["id"]
                    p_id = items["pod_id"]
                    door_n = items["door_number"]
                    door_av = items["door_availability"]
                    pick_otp = items["pickup_otp"]





            else:
                print("Test Failed :", response)
        return True

    def get_reservations_resend_otp(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/resend_otp/?reservation_id=' + str(self.reservation_id) + '&otp_type=' + str(self.reservation_otp_type), token=self.new_token)
        print("--------------------------get_reservations_resend_otp----------------------------")
        if response["success"] is True:
            print("reservation :", response)
        else:
            print("Test Failed :", response)
        return True

    def get_reservations_parcels(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/parcels?user_id=' + str(self.users_user_id), token=self.new_token)
        print("--------------------------get_reservations_parcels----------------------------")
        if response["success"] is True:
            print(response)
        else:
            print("Test Failed :", response)
        return True

    def create_reservation(self, no_of_reservation=None):
        flag = True
        print("-------------------------Reservation created-------------------------")
        data1 = {"createdby_phone": "9752111844", "dropby_phone": "9752111844", "pickupby_phone": "9752111844", "pod_id": self.pod_id, "location_id": self.pod_location_id}
        if no_of_reservation is not None:
            num = no_of_reservation
        else:
            num = self.number_of_doors
            i = 1
            while i <= num:
                response = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/create', data=json.dumps(data1), token=self.new_token)
                if response["success"] is True:
                    self.reservation_id = response["reservation_id"]
                    self.reserve_id_list.append(self.reservation_id)
                    print("reservation id :", self.reservation_id)
                    i += 1
                    print("list of Reservation id :", self.reserve_id_list)
                else:
                    flag = False
                    print("test failed")
                    break
        return flag

    def patch_reservation(self):
        print("-------------------------Reservation Patched-------------------------")
        for i in self.reserve_id_list:
            response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/cancel/' + str(i), token=self.new_token)
            print("patch users : ", i, response)
        return True

    def delete_reservation(self):
        print("-------------------------Reservation Deleted-------------------------")
        for i in self.reserve_id_list:
            response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'reservations/' + str(i), token=self.new_token)
            print("delete_reservation :", i, response)
        return True

    def get_test_sms(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'send_test_sms?user_phone=' + str(self.user_phone) + '&otp_text=' + str(self.otp_text), token=self.new_token)
        print("----------------------get_test_sms----------------------------")
        print(response)
        return True

    def get_generate_otp(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'generate_otp?user_phone=' + str(self.user_phone), token=self.new_token)
        if response["success"] is True:
            print("----------------------get_generate_otp---------------------")
            print(response)
        else:
            print("Test Failed :", response)
        return True

    def get_validate_otp(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'validate_otp?user_phone=' + str(self.user_phone) + '&otp_text=' + str(self.otp_text), token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("------------------------get_validate_otp---------------------------")
                self.validate_id = items["id"]
                self.validate_username = items["user_name"]
                self.validate_user_type = items["user_type"]
                print("id", self.validate_id)
                print("username", self.validate_username)
                print("user_type", self.validate_user_type)
            else:
                print("Test Failed :", response)
        return True

    def get_map_otp_to_door(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'map_otp_to_door?otp_text=' + str(self.otp_text), token=self.new_token)
        print("-------------------------get_map_otp_to_door--------------------------------")
        print(response)
        return True

    def get_spots_detail(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'spots/', token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("-------------------------get_spots_detail-----------------")
                self.spots_record_id = items["id"]
                self.spot_location_id = items["location_id"]
                print("record id :", self.spots_record_id)
                print("spot_location_id :", self.spot_location_id)
                break
            else:
                print("Test Failed :", response)
        return True

    def get_spots_by_id(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'spots/' + str(self.spots_record_id), token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("-------------------get_spots_by_id----------------------")
                self.spot_name = items["spot"]
                print("spots_record_id :", self.spots_record_id)
                print("spot_name :", self.spot_name)
            else:
                print("Test Failed :", response)
        return True

    def post_spot(self):
        data = {"location_id": self.pod_location_id, "spot": "Rear Entrance"}
        response = call_rest_api(request_type='post', endpoint=PODAPI_SERVER_ADDRESS + 'spots/', data=json.dumps(data), token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("-------------------------post spot----------------------------------")
                self.spots_record_id = items["id"]
                print("record id :", self.spots_record_id)
            else:
                print("test failed")
        return True

    def patch_spot(self):
        todo = {"spot": "AUTO SPOT NAME"}
        response = call_rest_api(request_type='patch', endpoint=PODAPI_SERVER_ADDRESS + 'spots/' + str(self.spots_record_id), data=json.dumps(todo), token=self.new_token)
        print("------------------------------patch_spot---------------------------------")
        for item in response["records"]:
            spot_name = item["spot"]
            print("patch users : ", self.spots_record_id, response)
            print("spot name :", spot_name)
        return True

    def delete_spot(self):
        response = call_rest_api(request_type='delete', endpoint=PODAPI_SERVER_ADDRESS + 'spots/' + str(self.spots_record_id), token=self.new_token)
        print("------------------------------delete spot---------------------------------")
        print(" spot_data deleted :", self.location_record_id, response)
        return True

    def get_filetore(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'filestore/info/', token=self.new_token)
        for items in response["records"]:
            if response["success"] is True:
                print("---------------------get_filetore--------------------------")
                self.filename_id = items["filename"]
                print("filename :", self.filename_id)
                break
            else:
                print("Test Failed :", response)
        return True

    def get_file_store_response(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'filestore/' + str(self.filename_id), token=self.new_token)
        print("------------------get_file_store_response----------------------------")
        if response["success"] is True:
            print(response)
        else:
            print("Test Failed :", response)
        return True

    def get_misc(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'echo/', token=self.new_token)
        print("-----------------------Misc-echo/-----------------------")
        print(response)
        return True

    def get_generate_token(self, token_num):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'generate_new_token/?pass_phase=' + str(token_num), token=self.new_token)
        print("-----------------------get_generate_token-----------------------")
        self.new_token = response["access_token"]
        print("generated token:", self.new_token)
        return True

    def get_generated_refresh_token(self):
        response = call_rest_api(request_type='get', endpoint=PODAPI_SERVER_ADDRESS + 'generate_refresh_token/', token=self.new_token)
        print("----------------get_generated_refresh_token-------------------")
        print("generated_refresh_token :", response)
        return True


a = Create()
a.get_generate_token("765432")
a.get_doors_detail()

# 1552 1554 1553 1549 1474 1428

1552
RTOPending
door_number: 1
478891
