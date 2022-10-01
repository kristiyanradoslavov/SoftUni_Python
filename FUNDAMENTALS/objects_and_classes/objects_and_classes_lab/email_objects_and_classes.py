class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f" {self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


final_result = []
command = input()

while command != "Stop":
    comm = command.split(" ")
    send = comm[0]
    receive = comm[1]
    cont = comm[2]
    email = Email(send, receive, cont)
    final_result.append(email)

    command = input()

if command == "Stop":
    indices = list(map(int, input().split(", ")))
    for x in indices:
        final_result[x].send()

for i in final_result:
    current = i.get_info()
    print(current)


