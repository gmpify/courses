class PhoneNumber:
    def __init__(self, number):
        digits = [n for n in number if n.isdigit()]

        if digits[0] == '1':
            digits = digits[1:]

        if len(digits) != 10:
            raise ValueError('Invalid number!')

        if digits[0] in ['0', '1'] or digits[3] in ['0', '1']:
            raise ValueError('Invalid number!')

        self.area_code = ''.join(digits[:3])
        self.exchange_code = ''.join(digits[3:6])
        self.subscriber_number = ''.join(digits[6:])

        self.number = self.area_code + self.exchange_code + self.subscriber_number

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
