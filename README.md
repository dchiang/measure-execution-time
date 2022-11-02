# Measure Execution Time

This is a proposed solution for the following **Project Waste Not, Inc** python coding challenge:

> Provide some Python code that can be used to measure how long a function takes to run in a friendly format. The amount of time can range from less than a second to several hours and should be easy for a human to read (for example “00:00:00:00012” is not a good output)

This proposed solution is meant to measure the execution time of virtually any python function. For it, the function will have to be expose as a python module.

## How it works?

When the project is launch, it will:
1. Create a new virtual environment.
2. Load the new virtual environment and install the module dependencies.
3. Execute the module passing the parameters specified by the user.
4. Print the total duration of the execution of the module.
5. Delete the virtual environment that was initially created.

## Install and Run

To install just pull this repository. To run this project the user must pass the following arguments:

| Arguments        | Description           | Mandatory  | Example |
| :-------------: |:-------------| :-----:| :-----|
| requirements      | Path of the file containing the list of dependencies of the module to be executed | (Depends on the module) |`--requirements ~/measure_execution_time/test_module/requirements.txt`|
| module      | Path of the module to be executed      |   Yes |`--module ~/measure_execution_time/test_module`|
| (module arguments) | Any argument that the module to be executed could requiere. It does supports `shortopts`,`longopts` and also regular arguments seprared by a white space     |    (Depends on the module) |`-x "some value" --named_arg "some other value" foo bar`|

## Examples

Assuming you want to check the total duration time of the test_module included in this repository and that you pulled this project in `/home/user/measure_execution_time`, then you should run this project from your `/home/user/` folder as:

`python3 -m measure_execution_time --requirements ~/measure_execution_time/test_module/requirements.txt --module ~/measure_execution_time/test_module`

For testing a custom module of yours that receives no extra arguments, you should run this project as:

`python3 -m measure_execution_time --requirements /path/to/your/module/requirements.txt --module /path/to/your/module`

If your custom module do not have dependencies, run it like this:

`python3 -m measure_execution_time --module /path/to/your/module `

If your custom module receives extra arguments:

`python3 -m measure_execution_time --module /path/to/your/module -x "some value" --named_arg "some other value" foo bar`
