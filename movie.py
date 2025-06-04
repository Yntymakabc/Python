class bilet:
    def __init__(self):
        self.tickets = {i:False for i in range(1,100)}

    def get_tickets(self):
        return self.tickets
    
    def reserve_ticket(self, name):
        for i in self.tickets:
            if self.tickets[i] == False:
                self.tickets[i]= name
                break

    

b = bilet()
b.reserve_ticket("akush")
print(b.get_tickets())