'''
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
"192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can
be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. 
You may return the valid IP addresses in any order.

 
'''

class Solution:
    result = []
    def validate_ip(self, ip: List[str]):
        for i in ip:
            
            if len(i) == 0:
                return False

            if i[0] == '0' and len(i) > 1:
                return False

            if not 0 <= int(i) <= 255:
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        size = len(s)
        for i in range(0, size):
            for j in range(i+1, size):
                for k in range(j+1, size):
                    try:
                        ip = [s[0:i+1], s[i+1:j+1], s[j+1:k+1], s[k+1:]]
                        # print (f'debug -> {".".join(ip)}')
                        if self.validate_ip(ip):
                            self.result.append(".".join(ip))
                    except:
                        continue
        
        return self.result
                    
