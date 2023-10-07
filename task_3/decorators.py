import time
import functools


def retry(*exceptions, attemtps: int = 1, delay: float = 1, backoff: float = 0):
    if not exceptions:
        raise ValueError("Must specify at least one exception type to catch")

    if delay < 0 or backoff < 0:
        raise ValueError("Delay and backoff must be greater than 0")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            local_delay = delay

            for attempt in range(attemtps):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == attemtps - 1:
                        raise ValueError("All attempts failed")

                    print(
                        f"{time.time()} Attempt {attempt + 1} failed with {type(e).__name__}: {e}. Retrying in {local_delay} seconds..."
                    )

                    time.sleep(local_delay)
                    local_delay += backoff

        return wrapper

    return decorator
