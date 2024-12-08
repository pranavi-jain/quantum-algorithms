# Update output dataframe with job results if completed

def update_dataframe_with_ibm_results(service, df):
    for index, row in df.iterrows():
        if row['device_name'].startswith('ibm'):
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

