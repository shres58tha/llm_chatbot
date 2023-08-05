@echo off

REM Activate the virtual environment
call Script/activate
IF %ERRORLEVEL% EQU 0 (
    echo virtual env in the current directory successful.
) ELSE (
    echo Setting up virtual env in the current directory
    python virtual_env.py
    pip install --upgrade pip
)

REM Run llm command
llm -m orca-mini-3b "What is the capital of nepal?"
IF %ERRORLEVEL% EQU 0 (
    echo llm installed succeeded.
) ELSE (
    echo llm install llm-gpt4all
    llm install llm-gpt4all
)

REM Run the Python script
python chatshell.py
