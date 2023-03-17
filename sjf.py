def main():
    n = int(input("Enter number of processes: "))
    pid = [0] * n
    at = [0] * n
    bt = [0] * n
    ct = [0] * n
    ta = [0] * n
    wt = [0] * n
    f = [0] * n
    st = 0
    tot = 0
    avgwt = 0
    avgta = 0

    print("Enter arrival times of the processes:")
    for i in range(n):
        at[i] = int(input())

    print("Enter burst times of the processes:")
    for i in range(n):
        bt[i] = int(input())
        pid[i] = i + 1
        f[i] = 0

    while tot < n:
        c = n
        min_bt = 999

        for i in range(n):
            if at[i] <= st and f[i] == 0 and bt[i] < min_bt:
                min_bt = bt[i]
                c = i

        if c == n:
            st += 1
        else:
            ct[c] = st + bt[c]
            st += bt[c]
            ta[c] = ct[c] - at[c]
            wt[c] = ta[c] - bt[c]
            f[c] = 1
            tot += 1

    print("\npid  arrival  burst  complete  turn  waiting")
    for i in range(n):
        avgwt += wt[i]
        avgta += ta[i]
        print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{ta[i]}\t\t{wt[i]}")

    print(f"\nAverage Turnaround Time: {avgta / n}")
    print(f"Average Waiting Time: {avgwt / n}")


if __name__ == "__main__":
    main()
