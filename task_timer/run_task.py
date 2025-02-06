import time, datetime

class Task():
    def start():
        """This grabs the starting time."""
        start_time = time.strftime("%H:%M:%S")
        print(f"Task started at {start_time}.")
        current_task()
    
    def current_task():
        while not end():
            run_time = time.strftime("%H:%M:%S") - start_time
            print(f"Task running for {current_time("%M")} minutes and {current_time("%S")} seconds.")

    def end():
        """This grabs the ending time and calculates the total time."""
        end_time = time.strftime("%H:%M:%S")
        final_time = end_time-start_time
        print(f"Task ended at {end_time}./n Task took {final_time} seconds to complete.")