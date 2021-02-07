'''
Accepted 02/07/2021 14:59; runtime 20 ms, memory 14.1 MB.
'''


class Solution:
    def maskPII(self, S: str) -> str:
        indexOfAt = S.find('@')
        isEmail = indexOfAt != -1
        if isEmail:
            emailName = S[0: indexOfAt]
            domainName = S[indexOfAt:]
            maskedEmail = ''
            maskedEmail += emailName[0].lower()
            maskedEmail += '*****'
            maskedEmail += emailName[-1].lower()
            maskedEmail += domainName.lower()
            return maskedEmail
        else:
            phoneNumber = ''
            maskedPhoneNumber = ''
            for digit in S:
                if digit.isdigit():
                    phoneNumber += digit
            length = len(phoneNumber)
            hasCountryCode = length > 10
            maskedPhoneNumber = '***-***-'
            maskedPhoneNumber += phoneNumber[-4:]
            if hasCountryCode:
                prefix = '+'
                prefix += '*' * (length - 10)
                prefix += '-'
                maskedPhoneNumber = prefix + maskedPhoneNumber
            return maskedPhoneNumber


testCases = ["LeetCode@LeetCode.com",
             "AB@qq.com",
             "1(234)567-890",
             "86-(10)12345678"]

for each in testCases:
    print(Solution.maskPII(None, each))
