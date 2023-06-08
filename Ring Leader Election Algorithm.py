import random


# This function defines the ring structure of the process
def Ring_Structure(initiator):
    ring = [initiator]
    num = 0
    while num != (len(process) - 1):
        temp = random.randrange(0, len(process))
        if process[temp] not in ring:
            ring.append(process[temp])
            num = num + 1
    return ring

# Here we define the present coordinator among the processes
def Coordinator():
    coordinator = int(input('Enter the coordinator process id: '))
    while True:
        if coordinator in process:
            return coordinator
        else:
            print("Process id is not available in the process list")
            coordinator = int(input('Enter the coordinator process id: '))


def Delete_Coordinator(request_id, coordinator):
    process.remove(coordinator)
    print(f'coordinator {coordinator} is dead. Process {request_id} finds out and initiates the election process for new co-ordinator')
    Elect_New_Coordinator(request_id, Ring_Structure(request_id))

def Coordinator_Status(request, coordinator):
    print('SELECT BELOW: (  1  for OKAY Status ) or (  0  for DEAD Status )')
    while True:
        flag = int(input('Choose one: '))
        if flag == 1:
            print(f'Process id {request} sucessefully requested the coordinator {coordinator}')
        elif flag == 0:
            Delete_Coordinator(coordinator=coordinator, request_id=request)
            return

# Elects the new coordinator
def Elect_New_Coordinator(initiator, ring_order):
    print(f'Ring order {ring_order}')
    new_coordinator = max(process)
    for i in ring_order:
        if random.randrange(0, 10) == 7:
            print("Error : declaring new coordinator")
            print("Re-election")
            Elect_New_Coordinator(initiator, ring_order)
        else:
            print(f'Message successfully sent from process {i}')
    print(f'Election Successfully :: new co-coordinator is process {new_coordinator}')



if __name__ == '__main__':
    process = []
    no_of_processes = 5
    for i in range(no_of_processes):
        temp = int(input("Enter Process ID: "))
        if temp not in process:
            process.append(temp)
            print("Process IDs are :", process)
        else:
            print("Process ID already exists... ")
            temp = int(input("Enter Process ID: "))
            process.append(temp)
    Coordinator_Status(process[1], Coordinator())
