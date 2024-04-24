from mpi4py import MPI

def distribute_array(arr, comm):
    rank = comm.Get_rank()
    size = comm.Get_size()
    chunk_size = len(arr) // size
    start = rank * chunk_size
    end = start + chunk_size if rank < size - 1 else len(arr)
    return arr[start:end]

def compute_sum(arr):
    return sum(arr)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Define the array to be summed (Assuming same array on all processors)
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Distribute the array among processors
    local_array = distribute_array(array, comm)

    # Compute local sum
    local_sum = compute_sum(local_array)

    # Gather all local sums on root process (rank 0)
    all_sums = comm.gather(local_sum, root=0)

    # Display intermediate sums calculated at different processors
    print("Processor", rank, "computed local sum:", local_sum)

    # Root process combines sums to get the final result
    if rank == 0:
        final_sum = sum(all_sums)
        print("Final Sum:", final_sum)

if __name__ == "__main__":
    main()


