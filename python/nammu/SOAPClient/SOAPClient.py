import requests
import logging
import xml.etree.ElementTree as ET
import httplib as http_client
from HTTPRequest import HTTPRequest

class SOAPClient(object):
    """
    Sends and retrieves information to and from the ORACC SOAP server.
    """
    def __init__(self, url, method):
        self.url = url
        self.method = method
        logging.basicConfig()
        self.logger, self.request_log = self.setup_logger()

    def setup_logger(self):
        """
        Creates logger to debug HTTP messages sent and responses received.
        Output should be sent to Nammu's console.
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        request_log = logging.getLogger("requests.packages.urllib3")
        request_log.setLevel(logging.DEBUG)
        request_log.propagate = True
        return logger, request_log

    def create_request(self, **kwargs):
        request = HTTPRequest(self.url, self.method, **kwargs)
        self.request = request

    def send(self):
        """
        Elaborate HTTP POST request and send it to ORACC's server.
        """
        self.request

        url = "http://oracc.museum.upenn.edu:8085"
        headers = dict(self.request.mtompkg.items())
        body = self.request.mtompkg.as_string().split('\r\n', 1)[0]
        body = body.replace('\r\n', '\n')
        body = body.replace('\n', '\r\n')
        self.response = requests.post(url, data=body, headers=headers)
        # try:
        #    response = requests.post(url, data=body, headers=headers, timeout=10)
        # except ReadTimeout:
        #          print "Timed out!"

    def get_response_text(self):
        return self.response.text

    def get_response_id(self):
        xml_root = ET.fromstring(self.response.text)
        # This should be done with xpath. See XPath and namespaces sections
        # here: https://docs.python.org/2/library/xml.etree.elementtree.html
        return xml_root[0][0][0][0].text

    def wait_for_response(self, id):
        """
        Check for a response to the request and obtain response zip file.
        """
        while True:
            print "Hey"
            ready_response = requests.get('http://oracc.museum.upenn.edu/p/' + id)
            if ready_response.text == "done\n":
                return

    def parse_response(self):
        """
        Extract information sent in server response.
        """
        pass

    def _check_response_ready(self, id):
        """
        Send a HTTP GET request to ORACC's server and retrieve status.
        """
        pass

    def create_request_zip(self):
        """
        Pack attachment in a zip file.
        """
        pass
