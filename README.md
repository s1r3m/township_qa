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

#### Contributing

To run all linters:
```bash
make lint
```

To fix code style:
```bash
make style
```

#### Emulators

You can set the device's info for tests in Makefile or in terminal by setting the env variables:
```bash
DEVICE_NAME="your_device"
DEVICE_UDID="your_udid"
PLATFORM_NAME="Android"
PLATFORM_VERSION="12.1"
```
For other variables and settings check `settings.py`. 

To start emulator automatically you have to implement the target "emulator".
Also, the installation of the app in test could be done in "start".
