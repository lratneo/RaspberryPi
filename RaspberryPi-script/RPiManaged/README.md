# RPiManage

## *Overview*

[TOC]

## setup environment

- setup debian(Ubuntu MATE, Raspbian) apt sources.list mirror;
- setup python develop environment;
  - pipy packages source mirror (清华大学镜像源);
  - basic packages install;
  - support *virtualenvwrapper* in `~/.bashrc` (not finish yet).



## bash script manage wifi

**Verified platform    :** Respberry Pi zero W

**Platform environment :** Rasbian distribution (stretch)


 *autoSwitch-WiFi*  on  directory  `/usr/local/sbin/`



~~*rc.local*  on  directory `/etc/`~~

### how to use WiFi script
use command on your terminal:
> 
> $ sudo echo "/usr/local/sbin/autoSwitch-WiFid &" >> /etc/rc.local 
> 

#### Note:
It maybe not work, because rc.local has `exit 0` on the last line of file.

So, it will add command under `exit 0`

Use `$ cat /etc/rc.local` to check it.

If so, the best way maybe `$ sudo vim /etc/rc.local`, delete the line of `exit 0`

and add `exit 0` on the last line of this file.

----
**two files both need for WifiManage.**

