import random
import uuid

## Generate a UUID based unique key
def generate_short_key():
    return str(uuid.uuid4())[:8]  # First 8 characters of a UUID


## Generate random list of n-bit strings of length atmost 4
def generate_random_n_bit_strings(n):
    # Step 1: Generate a random number x less than 4
    if n<=3:
        x = 1
    else:
        x = random.randint(1, 4)
    
    # Step 2: Generate x random n-bit binary strings
    n_bit_strings = [format(random.randint(0, 2**n - 1), f'0{n}b') for _ in range(x)]
    
    return n_bit_strings


# Update output dataframe with job results if completed
def update_dataframe_with_job_results(service, df, device):
    for index, row in df.iterrows():
        if row['device_name'] != device:
            continue 
        
        job_id = row['job_id']
        try:
            # Fetch the job from Qiskit Runtime Service
            job = service.job(job_id)
            
            # Check if the job is complete
            if job.status() == 'DONE':
                # Get job results
                result = job.result()
                counts = result.get_counts()
                execution_time = result.time_taken
                
                # Update the DataFrame
                df.at[index, 'counts'] = counts
                df.at[index, 'execution_time'] = execution_time
                
                print(f"Updated job {job_id}: Counts = {counts}, Execution Time = {execution_time} seconds")
            else:
                print(f"Job {job_id} is not completed yet. Current status: {job.status()}")
        except Exception as e:
            print(f"Error fetching job {job_id}: {e}")

