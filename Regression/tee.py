"""
This implements a functionality similar to POSIX's tee application

"""

import subprocess
import os
import sys

def bytes_available(file_object):
    """ 
    This will determine if any bytes are available for reading from a file
    
    Works for any file-like object that implements seek and tell, like the
    pipe that comes from subprocess Popen's process.stdout and process.stderr
    """
    
    current_location = file_object.tell()
    file_object.seek(0,os.SEEK_END)
    end_location = file_object.tell()
    file_object.seek(current_location)
    return end_location - current_location
    
def tee_pipe(pipe_stream, first_output, second_output):
    """
    This will tee the data coming from the stream to two different outputs
    
    By making one of the outputs sys.stdout/stderr and the second a file
    you are reproducing the standard POSIX tee.
    """
    available = bytes_available(stream)
    if available:
        data = stream.read(available)
        if first_output and hasattr(first_output, 'write'):
            first_output.write(data)
        if second_output and hasattr(second_output, 'write'):
            second_output.write(data)
    
def tee_process(process, stdout_file, stderr_file):
    """
    Will write the output of a process to file and stdout/stderr
    
    It takes in a process that has already been opened by subprocess.Popen, 
    with the paramaters stdout=subprocess.PIPE and stderr.PIPE and sends the
    output of stdout and stderr to the specified file-like objects AND to the
    sys.stdout and sys.stderr endpoints.
    """
    output_value = None
    
    while True:
        tee_pipe(process.stdout, sys.stdout, stdout_file)
        tee_pipe(process.stderr, sys.stderr, stderr_file)
        
        if output_value:
            return output_value

        # This is after the return value, so that we will get one extra loop 
        # to get any output that has happened between the last .read() and
        # the .poll()
        output_value = process.poll()

