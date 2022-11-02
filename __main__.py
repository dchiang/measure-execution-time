import getopt
import os
import shutil
import sys
from typing import List, Optional
from datetime import datetime, timedelta


def get_arguments_dict(arguments: List[str]) -> dict:
    input: dict = dict()
    try:
        options = getopt.getopt(arguments, "", ["requirements=", "module="])
        print(options)
        for option, value in options[0]:
            input[option[2:]] = value
        input["params"] = " ".join(options[1])
        if "requirements" not in input:
            input["requirements"] = ""
    except getopt.GetoptError as err:
        print(err)
    return input


def validate_input(input: dict) -> Optional[str]:
    if not input.get("module"):
        error = "missing module to be executed"
        return error
    if "~" in input.get("module", ""):
        error = "wrong input for module to be executed"
        return error
    if input.get("requirements") and not os.path.exists(input["module"]):
        error = "requirements file doesn't exist"
        return error
    if not os.path.exists(input["module"]):
        error = "the module to be executed doesn't exist"
        return error
    return None


def delete_virtual_env(environment: str) -> None:
    if os.path.exists(environment):
        print(f'deleting virtual environment {environment}')
        shutil.rmtree(environment)


def create_new_virtual_env(environment: str, requirements: str) -> None:
    delete_virtual_env(environment=environment)
    environment_command = f'python3 -m venv {environment}'
    if requirements:
        environment_command += f' && bash -c "source {environment}/bin/activate && pip3 install -r {requirements}"'
    print("creating virtual environment", environment_command)
    os.system(environment_command)


def measure_execution_time(environment: str, input: dict) -> timedelta:
    start_time = datetime.now()
    command = f'bash -c "source {environment}/bin/activate && python3 {input["module"]} {input["params"]}"'
    print("executing command:", command)
    os.system(command)
    end_time = datetime.now()
    return end_time-start_time


def pretty_format_duration(total_seconds):
    seconds, microseconds = str(total_seconds).split('.')
    days, seconds = divmod(int(seconds), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f'{days}d {hours}h {minutes}m {seconds}s {microseconds}ms'


def main(arguments: List[str]):
    ENV = ".env_measure_execution_time"
    input = get_arguments_dict(arguments)
    validation_error = validate_input(input=input)
    if validation_error:
        print(validation_error)
    else:
        create_new_virtual_env(
            environment=ENV, requirements=input["requirements"])
        delta = measure_execution_time(environment=ENV, input=input)
        print("Total duration:", pretty_format_duration(
            total_seconds=delta.total_seconds()))
        delete_virtual_env(environment=ENV)


if __name__ == '__main__':
    main(sys.argv[1:])
