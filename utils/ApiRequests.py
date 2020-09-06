import json
import requests
from utils.LogInitilizer import LogInitilizer
logging=LogInitilizer.getLogger()


class ApiRequests:

    def doPost(self, url, header, payload):
        logging.info(
            "\nRequest - \nMethod - POST \n URL --------- {} \n with Header --------- {} \n Payload --------- {} ".format(
                url, header, payload))
        response = requests.post(url, headers=header, data=json.dumps(payload))
        response_status = response_payload = response_header = None
        response_status = response.status_code
        response_header = response.headers

        try:
            response_payload = response.json()
        except Exception as e:
            pass

        logging.info(
            "\nResponse -\n Status Code --------- {} \n Headers --------- {} \n Payload --------- {}".format(
                response_status,
                response_header,
                response_payload))
        return response_status, response_payload, response_header

    def doGet(self, url, header):
        logging.info("Getting resource at URL --------- {} \n Header --------- {} ".format(url, header))
        response = requests.get(url, headers=header)
        response_status = response_payload = response_header = None
        response_status = response.status_code
        response_header = response.headers

        try:
            response_payload = response.json()
        except Exception as e:
            pass

        logging.info(
            "\nResponse -\n Status Code --------- {} \n Headers --------- {} \n Payload --------- {}".format(
                response_status,
                response_header,
                response_payload))
        return response_status, response_payload, response_header

    def doPut(self, url, header, payload):
        logging.info(
            "\nRequest - \nMethod - PUT \n URL --------- {} \n with Header --------- {} \n Payload --------- {} ".format(
                url, header, payload))
        response = requests.put(url, headers=header, data=json.dumps(payload))
        response_status = response_payload = response_header = None
        response_status = response.status_code
        response_header = response.headers
        try:
            response_payload = response.json()
        except Exception as e:
            pass

        logging.info("\nResponse -\n Status Code --------- {} \n Headers --------- {} \n Payload --------- {}".format(
            response_status, response_header, response_payload))

        return response_status, response_payload, response_header

    def doDelete(self, url, header):
        logging.info("\nRequest - \nMethod - DELETE \n URL --------- {} \n Header --------- {}".format(url, header))
        response = requests.delete(url, headers=header)
        logging.info("\nResponse -\n Status Code --------- {} \n Headers --------- {} \n Payload --------- {}".format(
            response.status_code, response.headers, response.json()))
        return response.status_code, response.json(), response.headers


