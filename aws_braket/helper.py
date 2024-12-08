from qiskit_braket_provider import BraketProvider

# Update output dataframe with job results if completed

def update_dataframe_with_aws_results(df):
    for index, row in df.iterrows():
        if row["device_name"].startswith("aws") and len(row["job_id"]) != 0:
            device = (row["device_name"])[4:]
            task_arn = row["job_id"]
            provider = BraketProvider()
            backend = provider.get_backend(device)

            try:
                # Fetch the job from AWS Braket Provider
                retrieved_task = backend.retrieve_job(task_id=task_arn)
                status = retrieved_task.status().name

                # Check if the task is complete
                if status == "DONE":
                    # Get results
                    result = retrieved_task.result()
                    counts = result.get_counts()
                    # execution_time = result.time_taken

                    # Update the DataFrame
                    df.at[index, "counts"] = counts

                    print(f"Updated job {task_arn}: Counts = {counts}")
                else:
                    print(
                        f"Job {task_arn} is not completed yet. Current status: {status}"
                    )
            except Exception as e:
                print(f"Error fetching job {task_arn}: {e}")
