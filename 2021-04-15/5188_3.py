def find(row, col, midV):
    global minV

    if row == N-1 and col == N-1:
        return
    if col+1 < N:
        find(row, col+1, midV+ARR[row][col+1])
    if row+1 < N:
        find(row+1, col, midV+ARR)