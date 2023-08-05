bash source bin/activate
if [ $? -eq 0 ]; then
    echo "virtual env in current directory sucessful."
else
    echo setting up virtual env in current directory
    python virtual_env.py
    pip install --upgrade pip
fi



llm -m orca-mini-3b 'What is the capital of nepal?'

if [ $? -eq 0 ]; then
    echo "llm installed succeeded."
else
    echo llm install llm-gpt4all
    llm install llm-gpt4all
fi

python test.py
