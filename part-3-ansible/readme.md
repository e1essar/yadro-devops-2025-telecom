# Скрипт

## Цель
Автоматизировать с помощью Ansible процесс:
- Установки Docker на целевом хосте (локальном или удаленном)
- Проверки на целевом хосте работоспособность Bash-скрипта/pуthon-скрипта внутри Docker-контейнера (аналогично 2 разделу, проверка работоспособности через docker logs)
- Доп. задание, по желанию реализовать автоматическую проверку вместо docker logs нa хосте, выполнить docker logs c помощью ansible

## Описание


## Тестирование
```
ubuntu@DESKTOP-5K1CCU6:/mnt/c/Users/Igor/Desktop/TEST/yadro-devops-telecom/part-3-ansible$ ansible-playbook -i inventory --ask-become-pass playbook.yml
BECOME password:

PLAY [Install Docker And Start Script In Container] ********************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [localhost]

TASK [Install Docker using this (maybe default installing)] ************************************************************
changed: [localhost]

TASK [Verify Docker is installed] **************************************************************************************
ok: [localhost]

TASK [Fail if Docker version command failed] ***************************************************************************
skipping: [localhost]

TASK [Display installed Docker version] ********************************************************************************
ok: [localhost] => {
    "msg": "Docker version 28.1.1, build 4eba377"
}

TASK [Add user to docker group] ****************************************************************************************
ok: [localhost]

TASK [Ensure Docker service is started] ********************************************************************************
ok: [localhost]

TASK [Build Docker image] **********************************************************************************************
changed: [localhost]

TASK [Remove existing container if exists] *****************************************************************************
changed: [localhost]

TASK [Run Docker container] ********************************************************************************************
changed: [localhost]

TASK [Fail if container exited with error] *****************************************************************************
skipping: [localhost]

TASK [Show docker logs] ************************************************************************************************
ok: [localhost]

TASK [Print logs to console] *******************************************************************************************
ok: [localhost] => {
    "msg": "[2025-05-02 18:11:51,372] - INFO - URL: https://httpstat.us/101 | Status: 101 | Body: \r\n[2025-05-02 18:11:52,287] - INFO - URL: https://httpstat.us/200 | Status: 200 | Body: 200 OK\r\n[2025-05-02 18:11:53,222] - INFO - URL: https://httpstat.us/300 | Status: 300 | Body: 300 Multiple Choices\r\n[2025-05-02 18:11:54,070] - ERROR - Exception error https://httpstat.us/404: 404 Client Error: Not Found for url: https://httpstat.us/404\r\n[2025-05-02 18:11:54,967] - ERROR - Exception error https://httpstat.us/500: 500 Server Error: Internal Server Error for url: https://httpstat.us/500"
}

PLAY RECAP *************************************************************************************************************
localhost                  : ok=11   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```
