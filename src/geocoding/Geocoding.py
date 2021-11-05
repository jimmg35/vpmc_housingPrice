import json
import requests
import xml.etree.ElementTree as ET

class GeoCoder():

    def __init__(self, configFile):

        with open(configFile) as f:
            configFile = json.load(f)
            self.oAppId = configFile["oAppId"]
            self.oAPIKey = configFile["oAPIKey"]
            self.serviceURL = configFile["serviceURL"]
    
    def address2Geolocation(self, address):

        payload='oAPPId={}&oAPIKey={}&oAddress={}&oSRS=EPSG%3A4326&oFuzzyType=0&oResultDataType=JSON&oFuzzyBuffer=0&oIsOnlyFullMatch=false&oIsLockCounty=false&oIsLockTown=false&oIsLockVillage=false&oIsLockRoadSection=false&oIsLockLane=false&oIsLockAlley=false&oIsLockArea=false&oIsSameNumber_SubNumber=false&oCanIgnoreVillage=false&oCanIgnoreNeighborhood=false&oReturnMaxCount=0'.format(
            self.oAppId,
            self.oAPIKey,
            address
        )

        try:
            response = requests.request(
                "POST", 
                self.serviceURL, 
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                }, 
                data=payload.encode()
            )
        except:
            return None, None

        # 解讀XML
        
        data = None
        # 解讀JSON
        try:
            tree = ET.ElementTree(ET.fromstring(response.text))
            root = tree.getroot()
            data = json.loads(root.text)
        except:
            return None, None
            
        if len(data["AddressList"]) == 0:
            return None, None
        
        return data["AddressList"][0]["X"], data["AddressList"][0]["Y"]


if __name__ == "__main__":

    
    gc = GeoCoder()

    x, y = gc.address2Geolocation("桃園市桃園區國際路二段27-1號")

    print(x, y)
