## Reminder
A python script that reminds of the weather every day,in this project i have used the Longitude and Latitude of the City of Nairobi .

## Installations
- Schedule - a process scheduler for periodic jobs that use the builder pattern for configuraation(tasks are scheduled at a particular time or day of the week or 24 hours format)

- Use $ pip install schedule   to install it


## Schedule.Scheduler class

    - schedule.every(interval=1) : Calls every on the default scheduler instance. Schedule a new periodic job.
    - schedule.run_pending() : Calls run_pending on the default scheduler instance. Run all jobs that are scheduled to run.
    - schedule.run_all(delay_seconds=0) : Calls run_all on the default scheduler instance. Run all jobs regardless if they are scheduled to run or not.
    - schedule.idle_seconds() : Calls idle_seconds on the default scheduler instance.
    - schedule.next_run() : Calls next_run on the default scheduler instance. Datetime when the next job should run.
    - schedule.cancel_job(job) : Calls cancel_job on the default scheduler instance. Delete a scheduled job.

   ## Basic methods for Schedule.job
 

    - at(time_str) : Schedule the job every day at a specific time. Calling this is only valid for jobs scheduled to run every N day(s).
    Parameters: time_str – A string in XX:YY format. 
    Returns: The invoked job instance
    - do(job_func, *args, **kwargs) : Specifies the job_func that should be called every time the job runs. Any additional arguments are passed on to job_func when the job runs.
    Parameters: job_func – The function to be scheduled 
    Returns: The invoked job instance
    - run() : Run the job and immediately reschedule it. 
    Returns: The return value returned by the job_func
    - to(latest) : Schedule the job to run at an irregular (randomized) interval. For example, every(A).to(B).seconds executes the job function every N seconds such that A <= N <= B.

## Data source
Open-Meteo weather forecast APIs use weather models from multiple national weather providers.