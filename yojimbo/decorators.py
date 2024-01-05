import multiprocessing

from yojimbo.main import run_yojimbo, stop_yojimbo


# def terminate_process(process):
#     if process.is_alive():
#         process.terminate()
#         process.join()


# def yojimbo(func):
#     """
#     Decorator function that intercepts and modifies API calls
#     """
#     def wrapper(*args, **kwargs):
#         run_yojimbo()
#
#         func(*args, **kwargs)
#         #
#         # try:
#         #
#         # except Exception as e:
#         #     print(f"Error while running the test {e}")
#         # finally:
#         #     terminate_process(process)
#
#         stop_yojimbo()
#         # return result
#
#     return wrapper

def yojimbo(func):
    """
    Decorator function that intercepts and modifies API calls
    """
    def wrapper(*args, **kwargs):
        run_yojimbo()

        try:
            result = func(*args, **kwargs)
            assert result == {"data": "cool data"}  # Example assertion
            print("Asserted successfully")
        except Exception as e:
            print(f"Error while running the test: {e}")
        finally:
            stop_yojimbo()

    return wrapper
