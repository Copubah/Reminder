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