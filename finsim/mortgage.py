class Mortgage():
    """
    principal: integer value of loan amount
    interest:  APR - e.g 5.6 -> 1.056 APR
    """

    def __init__(self, principal, interest, payments=30*12):
        self.principal = principal
        self.interest = interest
        self.payments = payments


    def monthly_rate(self):
        return self.interest/12.0/100


    def calc_payment(self):
        rate = self.monthly_rate()

        return((
            rate
            + (rate / ((1 + rate) ** (self.payments) - 1))
        ) * self.principal)


    def calc_total_cost(self):
        return(self.calc_payment() * self.payments)

    
    def custom_payoff_cost(self, payment, lumps={}):
        bal = self.principal
        payment_cnt = 0
        total_cost = 0
        next_payment = payment + lumps.get(payment_cnt, 0)

        while bal > next_payment and payment_cnt < (1000 * 12):
            bal *= 1 + self.monthly_rate()
            total_cost += next_payment
            bal -= next_payment
            payment_cnt += 1
            next_payment = payment + lumps.get(payment_cnt, 0)

        total_cost += bal

        return(total_cost, payment_cnt)
