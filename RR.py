from queue import Queue


def main():
    tq = int(input("Enter time quantum: "))
    n = int(input("Enter number of processes: "))
    arrival = [0] * n
    burst = [0] * n
    wait = [0] * n
    turn = [0] * n
    temp_burst = [0] * n
    complete = [False] * n
    timer = 0
    max_process_index = 0
    avg_wait = 0
    avg_tt = 0

    print("Enter arrival times of the processes:")
    for i in range(n):
        arrival[i] = int(input())

    print("Enter burst times of the processes:")
    for i in range(n):
        burst[i] = int(input())
        temp_burst[i] = burst[i]

    while timer < arrival[0]:
        timer += 1

    q = Queue()
    q.put(0)

    while not all(complete):
        current_process = q.get()


        processed_units = 0
        while processed_units < tq and temp_burst[current_process] > 0:
            temp_burst[current_process] -= 1
            timer += 1
            processed_units += 1


            for i in range(max_process_index + 1, n):
                if arrival[i] <= timer and i not in q.queue:
                    max_process_index = max(max_process_index, i)
                    q.put(i)

        if temp_burst[current_process] == 0 and not complete[current_process]:
            turn[current_process] = timer
            complete[current_process] = True

        if temp_burst[current_process] > 0:
            q.put(current_process)

    for i in range(n):
        turn[i] = turn[i] - arrival[i]
        wait[i] = turn[i] - burst[i]

    print("\nProgram No.\tArrival Time\tBurst Time\tWait Time\tTurnAround Time")
    for i in range(n):
        print(f"{i + 1}\t\t\t\t{arrival[i]}\t\t\t\t{burst[i]}\t\t\t{wait[i]}\t\t\t\t{turn[i]}")

    avg_wait = sum(wait) / n
    avg_tt = sum(turn) / n

    print(f"Average wait time: {avg_wait}\nAverage Turn Around Time: {avg_tt}")


if __name__ == "__main__":
    main()
