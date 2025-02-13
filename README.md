# ConnectGuard
v2ray Connect Guard 


# Guide to Using the VPN Script with V2Ray on Linux

This Python script allows you to establish a VPN connection using the `v2ray` program and proxy settings on Linux. The script automatically changes proxy settings and can operate in different modes (auto, manual, off).

## Prerequisites

Before running the script, ensure you have installed the following:

1. **V2Ray**: The `v2ray` executable must be available on your system. In this example, the `v2ray` file is located at `/home/user/Desktop/VPN/`.

2. **cowsay**: For displaying fancy messages in the terminal.
   ```bash
   sudo apt-get install cowsay
   ```

3. **lolcat**: For coloring text output in the terminal.
   ```bash
   sudo apt-get install lolcat
   ```

4. **jcal**: For displaying the Jalali calendar in the terminal (optional).
   ```bash
   sudo apt-get install jcal
   ```

## How to Run the Script

1. First, ensure you have saved the Python file on your system. For example, the file can be named `run.py`.

2. Run the script using the following command:
   ```bash
   python3 run.py
   ```

3. After running the script, you will be prompted to choose the proxy mode. The available options are:
   - **off**: Disable the proxy.
   - **auto**: Set the proxy to automatic mode.
   - **manual**: Set the proxy to manual mode.
   - **-1**: Exit the script.

4. After selecting the mode, the script will automatically change the proxy settings and establish the VPN connection.

## Code Explanation

- **set_proxy_setting(mode)**: This function changes the system's proxy settings. The `mode` parameter can be one of `auto`, `off`, or `manual`.

- **vpn()**: This function runs the `v2ray` executable to establish the VPN connection.

- **mode()**: This function prompts the user to select the proxy mode and calls the `set_proxy_setting` function based on the user's choice.

- **thread1**: A separate process is created to run the `vpn()` function.

- **thread2**: A separate thread is created to run the `mode()` function.

## Exiting the Script

To exit the script, you can select the `-1` option. This will change the proxy settings to `off` and automatically terminate the script.

## Important Notes

- Ensure the path to the `v2ray` file in the `vpn()` function is correctly set.
- This script is designed for GNOME-based environments. If you are using a different desktop environment, you may need to modify the `gsettings` commands.

## Potential Issues

- If the script does not work properly, ensure all prerequisites are installed and you have the necessary permissions.
- If you are using a desktop environment other than GNOME, you may need to adjust the proxy settings commands.

## Author

This script was developed by **Shahin Mansouri**. For more information, you can contact [mansouri.math.kntu@gmail.com](mailto:mansouri.math.kntu@gmail.com).

---

I hope this guide helps you easily run and manage your VPN script. If you have any questions or suggestions, I'd be happy to hear them!
