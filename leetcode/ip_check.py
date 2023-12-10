class Solution:

    def checkIpV4(self, octet: str) -> bool:
        try:
            o = int(octet)
            if 0 <= o <= 255 and len(str(o)) == len(octet):
                return True
        except Exception as e:
            return False

        return False

    def checkIpV6(self, octet: int) -> bool:
        print("here")
        for char in octet:
            print(char)
            if not (
                    (ord('A') <= ord(char) <= ord('F') ) or ( ord('a') <= ord(char) <= ord('f'))
                    or  (ord('0') <= ord(char) <= ord('9'))
            ):
                print("here", char)
                print (ord('0') <= ord(char) <= ord('9'))
                return False

        return True

    def validIPAddress(self, queryIP: str) -> str:

        octets = queryIP.split(".")
        octetsV6 = queryIP.split(":")

        if len(octets) == 4:
            for octet in octets:
                if not self.checkIpV4(octet):
                    return "Neither"
            return "IPv4"

        if len(octetsV6) > 4:
            for octet in octetsV6:
                if not self.checkIpV6(octet):
                    return "Neither"
            return "IPv6"

        return "Neither"
