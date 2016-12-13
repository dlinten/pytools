# pytools
Set of Python libraries to make life easy
**Note: This is a starting point for python helper libraries and is not to be used in production systems without modification.**
##async_runner
###Execute
####execute_with_info_async(cmd: str) -> str
Executes a process with information returned from stdout and information about the success or failure of a call. 
```python
for line in Execute.execute_with_info_async('ls -la'):
    print(line)
```
####execute_async(cmd: str) -> str
Executes a process with information returned from stdout
```python
for line in Execute.execute_async('ls -la'):
    print(line)
```
##fancy_message
###Message
####header(message: str, ending='\n'), info(message: str, ending='\n'), warn(message: str, ending='\n'), error(message: str, ending='\n'), output(message: str, ending='\n')
```python
Message.header('This is a Message.header() test')
Message.info('This is a Message.info() test')
Message.warn('This is a Message.warn() test')
Message.error('This is a Message.error() test')
Message.output('This is a Message.output() test')
```
##git_tools
####local_commit_ref(repo_path: str) -> str
Gets the local Git commit Ref for HEAD for a given repository directory
```python
local_commit_ref('./test_resources/test-project-1')
```
####is_path_a_repo(repo_path: str) -> bool
Tests if a given directory is a Git Repository 
```python
is_path_a_repo('./test_resources')
```