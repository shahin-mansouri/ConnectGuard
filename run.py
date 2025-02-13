import os
import threading
import multiprocessing


def set_proxy_setting(mode=True):
    if mode == "auto":
        os.system("clear && gsettings set org.gnome.system.proxy mode 'auto'")
        # print("Change system proxy to Automatic...")
        os.system("jcal")
        os.system('cowsay -f moose "Change system proxy to Automatic..." | lolcat')
    elif mode == "off":
        os.system("clear && gsettings set org.gnome.system.proxy mode 'none'")
        # print("Change system proxy to off...")
        os.system("jcal")
        os.system("cowsay -f moose 'Change system proxy to off...' | lolcat")
    else:
        os.system("clear && gsettings set org.gnome.system.proxy mode 'manual'")
        # print("Change system proxy to manual...")
        os.system("jcal")
        os.system("cowsay -f moose 'Change system proxy to manual...' | lolcat")


def vpn():
    os.system("/home/shahin/Desktop/VPN//v2ray run > /dev/null 2>&1")
    # os.system("clear && /home/shahin/Desktop/VPN/v2ray run | lolcat")


def mode():
    question = input("mode: 'off' or 'auto' or 'manual' or '-1' to exit ? \n")

    match question:
        case "-1":
            set_proxy_setting("off")
            print("Exiting ...")
            thread1.terminate()
            return

        case "off":
            set_proxy_setting(question)
            return mode()

        case "auto":
            set_proxy_setting(question) 
            return mode()

        case "manual":
            set_proxy_setting(question)  
            return mode()

        case _:
            return mode()



set_proxy_setting(True)
thread1 = multiprocessing.Process(target=vpn, args=())
thread1.start()


thread2 = threading.Thread(target=mode, args=())
thread2.start()


thread1.join()
thread2.join()


print('Finished program.')
os.system("clear")

