## This is a test framework and some tests.

#### Preparation
1. Install [Node.js](https://nodejs.org/en/download/prebuilt-installer/current)
and appium:
    ```bash
   npm install -g appium
    ```
   
2. Prepare your environment for tests:
   ```bash
   make install
   ```
   
3. Start the environment:
   ```bash
   make start
   ```

4. Launch tests:
    ```bash
   make tests
    ```


#### Emulators

You can set the device's info for tests in Makefile or in terminal by setting the env variables:
```bash
DEVICE_NAME="your_device"
DEVICE_UDID="your_udid"
PLATFORM_NAME="iOS"
PLATFORM_VERSION="15.1"
```

To start emulator automatically you have to implement the target "emulator".
Also, the installation of the app in test could be done in "start".
