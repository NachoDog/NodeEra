#!/usr/bin/env python3
"""
 
Copyright 2018-2020 SingerLinks Consulting LLC 

This file is part of NodeEra.

NodeEra is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

NodeEra is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with NodeEra. If not, see <https://www.gnu.org/licenses/>.
 
"""
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class loadJobError(Error):
    """
    Exception raised during load job processing
    Attributes:
        logfile -- the logfile name and directory based on log directory commmand line parameter and file name generated by the program
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        
class loggingsetupError(Error):
    """
    Exception raised when logging setup fails
    Attributes:
        logfile -- the logfile name and directory based on log directory commmand line parameter and file name generated by the program
        message -- explanation of the error
    """

    def __init__(self, logfile, message):
        self.logfile = logfile
        self.message = message
        
class inifileError(Error):
    """
    Exception raised when inifile processing fails
    Attributes:
        inifile -- name of the ini file specified on the command line.  
        message -- explanation of the error
    """

    def __init__(self, inifile, message):
        self.inifile = inifile
        self.message = message

class CSVFileError(Error):
    """
    Exception raised during processing of the CSV file parameters in the run file
    Attributes:  
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message

class neo4jError(Error):
    """
    Exception raised during processing of neoCon methods.
    Attributes:  
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message