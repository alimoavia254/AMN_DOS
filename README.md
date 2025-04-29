🛠️ AMN-DOS: Advanced Multi-layer Attack Tool

AMN-DOS is a powerful multi-threaded stress testing and DoS simulation tool designed for educational and research purposes. Developed in Python, this tool allows users to test the resilience of web servers and applications against different types of simulated attacks.
👨‍💻 Developed By

    Ali Moavia

    Mehwish Naz

⚙️ Features

    🔥 HTTP Flood Attack – Generates massive volumes of HTTP GET requests with randomized headers and IP spoofing.

    🐌 Slowloris Attack – Simulates the Slowloris DoS technique by keeping multiple connections open to exhaust server resources.

    🌐 TCP SYN Flood Attack – Sends repeated SYN packets to simulate basic TCP-based denial-of-service.

    🌈 Color-coded CLI Output – Real-time feedback for each request/packet sent.

    🧵 Multi-threading Support – Launch multiple threads for simultaneous, high-speed attack simulations.

🧪 Usage

$ python3 -m venv amn-env
$ source amn-env/bin/activate
$ pip install colorama
$ pip install requests
$ python3 amn-dos.py


You'll be prompted to:

    Enter the target URL

    Choose the attack mode (http, slowloris, tcp)

    Specify the number of threads

⚠️ Disclaimer

This tool is intended strictly for educational and authorized security testing purposes only. Performing DoS attacks on servers without permission is illegal and unethical. Always ensure you have proper authorization before running any test.
