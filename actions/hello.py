---
name: hello
pack: training
runner_type: "python-script"
description: hello python!
enable: true
entry_point: hello.py
parameters:
    message:
        type: string
        description: say hello
        required: true
        position: 1