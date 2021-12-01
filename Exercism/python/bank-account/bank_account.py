import threading

STATUS_OPEN = 'open'
STATUS_CLOSED = 'closed'

class BankAccount:
    def __init__(self):
        self.status = STATUS_CLOSED
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status == STATUS_CLOSED:
            raise ValueError('Account is closed')

        return self.balance

    def open(self):
        if self.status == STATUS_OPEN:
            raise ValueError('Account is closed')

        self.status = STATUS_OPEN
        self.balance = 0

    def deposit(self, amount):
        if self.status == STATUS_CLOSED:
            raise ValueError('Account is closed')

        self.lock.acquire()
        if amount < 0:
            raise ValueError("Can't deposit negative value")
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if self.status == STATUS_CLOSED:
            raise ValueError('Account is closed')

        self.lock.acquire()
        if amount < 0:
            raise ValueError("Can't withdraw negative value")

        if self.balance < amount:
            raise ValueError('Not enough balance for operation')
        self.balance -= amount
        self.lock.release()

    def close(self):
        if self.status == STATUS_CLOSED:
            raise ValueError('Account is closed')

        self.status = STATUS_CLOSED
